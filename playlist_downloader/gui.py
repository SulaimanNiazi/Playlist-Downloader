from tkinter import Tk, Label, Entry, Button, StringVar, BooleanVar, Checkbutton, messagebox
from tkinter.ttk import Combobox
from tkinter.filedialog import askdirectory
from multiprocessing import Process, Queue
from threading import Thread
from .downloader import download

class gui:
    def __init__(self):
        root = Tk()
        root.title('Media Downloader')
        root.minsize(700, 300)
        root.maxsize(root.winfo_screenwidth(), root.winfo_screenheight())
        root.protocol('WM_DELETE_WINDOW', self.close)

        for i in range(4):
            root.columnconfigure(i, weight=10)
            root.rowconfigure(i, weight=10)
        root.columnconfigure(0, weight=1)
        root.columnconfigure(3, weight=1)

        Label(root, text='URL:').grid(column=0, row=0, padx=10, sticky='we')
        self.url_bar = Entry(root)
        self.url_bar.grid(column=1, columnspan=2, row=0, padx=10, sticky='we')
        self.button = Button(root, text='Download', command=self.main_button_pressed)
        self.button.grid(column=3, row=0, padx=10, sticky='we')

        Label(root, text='Location:').grid(column=0, row=1, padx=10, sticky='we')
        self.path = Entry(root)
        self.path.grid(column=1, columnspan=2, row=1, padx=10, sticky='we')
        Button(root, text='Browse', command=lambda: self.path.insert(0, askdirectory(initialdir='.'))).grid(column=3, row=1, padx=10, sticky='we')

        self.formats = ['No Downloads', 'm4a', 'mkv', 'mp3', 'mp4']
        qualities = ['8K UHD 4320p', '4K UHD 2160p', 'QHD 1440p', 'FHD 1080p', 'HD 720p', 'SD 480p', 'SD 360p', 'LD 240p', 'LD 144p']
        
        Label(root, text='Options:').grid(column=0, row=2, padx=10, sticky='we')
        self.format = StringVar(value=self.formats[0])
        format_combo = Combobox(root, state='readonly', textvariable=self.format, values=self.formats)
        format_combo.grid(column=1, row=2, padx=10, sticky='we')
        self.quality = StringVar(value='Catalog')
        quality_combo = Combobox(root, state='readonly', textvariable=self.quality, values=['Catalog'])
        quality_combo.grid(column=2, row=2, padx=10, sticky='we')
        self.replace = BooleanVar()
        Checkbutton(root, text='Replace', variable=self.replace).grid(column=3, row=2, padx=10, sticky='we')

        def set_qualities(_):
            format = self.format.get()
            if format in ('mkv', 'mp4'):
                self.quality.set(qualities[3])
                quality_combo.config(values=qualities)
            elif format in ('m4a', 'mp3'):
                self.quality.set('Best')
                quality_combo.config(values=['Best'])
            else:
                self.quality.set('Catalog')
                quality_combo.config(values=['Catalog'])
        format_combo.bind('<<ComboboxSelected>>', set_qualities)

        Label(root, text='Browser:').grid(column=0, row=3, padx=10, sticky='we')
        browsers = ['Chrome', 'Firefox', 'Vivaldi']
        self.browser = StringVar(value=browsers[1])
        Combobox(root, state='readonly', textvariable=self.browser, values=browsers).grid(column=1, row=3, padx=10, sticky='we')

        self.process = Process()
        self.root = root
        self.queue = Queue(maxsize=2)

    def main_button_pressed(self):
        def handler():
            message = 'Download failed prematurely.'
            
            while True:
                try:
                    value = self.queue.get()
                    if value == 'done':
                        break
                    else:
                        message = value
                except: break
            
            self.button.config(text='Download', padx=2)
            lower = message.lower()
            if lower.__contains__('fail') or lower.__contains__('error'):
                messagebox.showerror('Download Failed', message)
            else:
                messagebox.showinfo('Download Complete', message)

        if self.process.is_alive():
            if messagebox.askyesno('Cancelling Download', 'Are you sure you want to cancel the download?', default='no'): self.process.terminate()
        else:
            url = self.url_bar.get()
            if url:
                self.button.config(text='Cancel', padx=10)
                self.process = Process(
                    target=download,
                    args=(
                        url,
                        self.format.get(),
                        self.quality.get(),
                        (self.path.get() or '.') + '/',
                        self.replace.get(),
                        self.browser.get().lower(),
                        self.queue
                    )
                )
                self.process.start()
                Thread(target=handler, daemon=True).start()
    
    def run(self):
        self.root.mainloop()
    
    def close(self):
        if self.process.is_alive():
            answer = messagebox.askyesnocancel('A download is still running', 'Do you want to cancel the download (yes) or let it run in the background to completion (No)?')
            if answer is None: return
            elif answer: self.process.terminate()
        self.root.destroy()