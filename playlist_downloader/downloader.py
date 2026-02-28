from yt_dlp import YoutubeDL
from json import dump, load
from multiprocessing import Queue
from re import sub

class logger:
    def __init__(self, queue: Queue):
        self.queue = queue

    def debug(self, message: str):
        self.queue.put(message)

    def info(self, message: str):
        self.queue.put(message)

    def warning(self, message: str):
        self.queue.put(message)
        
    def error(self, message: str):
        self.queue.put(message)

def download(url: str, preferred: str, quality: str, path: str, replace: bool, browser: str, queue: Queue):
    options: dict[str, str | bool | tuple[str] | list[dict[str, str] | logger]] = {
        'cookiesfrombrowser': (browser,),
        'remote_components': ['ejs:github'],
        'ignoreerrors': True,
        'logger': logger(queue),
    }
    download = preferred != 'No Downloads'
    
    if download:
        video = quality != 'Best'
        
        if video:
            format = 'bestvideo[ext=' + preferred + '][vcodec^=avc][height<=' + quality.split(' ')[-1][:-1] + ']+bestaudio[ext=m4a]/bestaudio'
            outtmpl = '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s'
            postprocessors = [
                {
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': preferred
                },
                {
                    'key': 'FFmpegEmbedSubtitle',
                }
            ]
        else:
            format = 'bestaudio[ext=' + preferred + ']/bestaudio'
            outtmpl = '%(playlist)s/%(title)s.%(ext)s'
            postprocessors = [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': preferred
                }
            ]
        
        options.update(
            format = format,
            outtmpl = path + outtmpl,
            writethumbnail = True,
            writesubtitles = video,
            subtitlesformat = 'srt',
            allsubtitles = video,
            postprocessors = postprocessors + [
                {
                    'key': 'EmbedThumbnail',
                }
            ],
            overwrites = replace,
        )

    try:
        with YoutubeDL(options) as ydl:
            if download:
                ydl.download(url)
                queue.put('Download complete')
            else:
                entries = {}
                info = ydl.extract_info(url, download)

                if 'entries' in info:
                    path += validate(info['entries'][0]['playlist_title']) or 'Untitled playlist'

                    if not replace:
                        try: 
                            with open(path, encoding='utf-8') as file: entries = load(file)
                        except: entries = {}

                    for entry in info['entries']:
                        if entry:
                            uploader = entry.get('channel') or entry.get('uploader') or '<Unknown>'
                            title = entry.get('title') or '<Untitled>'
                            if uploader in entries:
                                if title not in entries[uploader]:
                                    changes += 1
                                    entries[uploader] += [title]
                            else:
                                changes += 1
                                entries[uploader] = [title]

                    queue.put('Successfully cataloged 1 entry.' if changes == 1 else f'Successfully cataloged {changes} entries.')
                else:
                    uploader = info['channel'] or info['uploader'] or 'Unknown'
                    title = info['title'] or 'Untitled'
                    path += validate(uploader + ' - ' + title)
                    entries = info
                    queue.put(f'Successfully cataloged video.')
                
                with open(path + '.json', mode='w', encoding='utf-8') as file: dump(entries, file, ensure_ascii=False, indent=4)
    
    except TypeError:
        queue.put('Error: Invalid URL')
    except Exception as e:
        queue.put(f'{type(e).__name__}: {e}')

    queue.put('done')

def validate(name: str) -> str:
    if name.isalnum():
        reserved = ['CON', 'PRN', 'AUX', 'NUL'] + [f'COM{n}' for n in range(10)] + [f'LPT{n}' for n in range(10)]
        if name in reserved:
            return name + '_'
    else:
        return sub('[<>:"/\\|?*\x00-\x1F]', '_', name)
