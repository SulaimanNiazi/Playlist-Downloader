from tkinter import Tk, Label, Entry, Button, StringVar, BooleanVar, Checkbutton
from tkinter.ttk import Combobox

class gui:
    def __init__(self, root: Tk):
        root.title("Media Downloader")
        root.minsize(700, 300)
        root.maxsize(root.winfo_screenwidth(), root.winfo_screenheight())

        for i in range(4):
            root.columnconfigure(i, weight=10)
            root.rowconfigure(i, weight=10)
        root.columnconfigure(0, weight=1)

        Label(root, text="URL:").grid(column=0, row=0, padx=10, sticky="we")
        self.url_bar = Entry(root)
        self.url_bar.grid(column=1, columnspan=2, row=0, padx=10, sticky="we")
        Button(root, text="Download", command=self.download).grid(column=3, row=0, padx=10, sticky="we")

        Label(root, text="Options:").grid(column=0, row=2, padx=10, sticky="we")
        video_formats = ["No Video Downloads", "8K UHD 4320p", "4K UHD 2160p", "QHD 1440p", "FHD 1080p", "HD 720p", "SD 480p", "SD 360p", "LD 240p", "LD 144p"]
        self.video_option = StringVar(value=video_formats[0])
        Combobox(root, state="readonly", textvariable=self.video_option, values=video_formats).grid(column=1, row=2, padx=10, sticky="we")
        audio_formats = ["No Audio Downloads", "M4A"]
        self.audio_option = StringVar(value=audio_formats[0])
        Combobox(root, state="readonly", textvariable=self.audio_option, values=audio_formats).grid(column=2, row=2, padx=10, sticky="we")
        self.catalog_option = BooleanVar()
        Checkbutton(root, text="Catalog", variable=self.catalog_option).grid(column=3, row=2, padx=10, sticky="we")
    
    def download(self):
        pass

if __name__ == "__main__":
    root = Tk()
    app = gui(root)
    root.mainloop()