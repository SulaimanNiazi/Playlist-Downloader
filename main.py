from tkinter import Tk, Label, Entry, Button, StringVar, BooleanVar, Checkbutton
from tkinter.ttk import Combobox
from tkinter.filedialog import askdirectory
from multiprocessing import Process
from threading import Thread

def download(url: str, format: str, quality: str, path="."):
    for x in range(100000): print(x)
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
        self.button = Button(root, text="Download", command=self.main_button_pressed)
        self.button.grid(column=3, row=0, padx=10, sticky="we")

        Label(root, text="Location:").grid(column=0, row=1, padx=10, sticky="we")
        self.path = Entry(root)
        self.path.grid(column=1, columnspan=2, row=1, padx=10, sticky="we")
        Button(root, text="Browse", command=lambda: self.path.insert(0, askdirectory(initialdir="."))).grid(column=3, row=1, padx=10, sticky="we")

        self.formats = ["No Downloads", "m4a", "mkv", "mp3", "mp4"]
        qualities = ["8K UHD 4320p", "4K UHD 2160p", "QHD 1440p", "FHD 1080p", "HD 720p", "SD 480p", "SD 360p", "LD 240p", "LD 144p"]
        
        Label(root, text="Options:").grid(column=0, row=2, padx=10, sticky="we")
        self.format = StringVar(value=self.formats[0])
        format_combo = Combobox(root, state="readonly", textvariable=self.format, values=self.formats)
        format_combo.grid(column=1, row=2, padx=10, sticky="we")
        self.quality = StringVar()
        quality_combo = Combobox(root, state="readonly", textvariable=self.quality)
        quality_combo.grid(column=2, row=2, padx=10, sticky="we")
        self.catalog = BooleanVar()
        Checkbutton(root, text="Catalog", variable=self.catalog).grid(column=3, row=2, padx=10, sticky="we")
        def set_qualities(_):
            if self.format.get() in ("mkv", "mp4"):
                self.quality.set(qualities[3])
                quality_combo.config(values=qualities)
            else:
                self.quality.set("")
                quality_combo.config(values=[])
        format_combo.bind("<<ComboboxSelected>>", set_qualities)

        self.process = Process()

    def main_button_pressed(self):
        if self.process.is_alive():
            self.process.terminate()
        else:
            url = self.url_bar.get()
            format = self.format.get()
            if url and (self.catalog.get() or format != self.formats[0]):
                self.button.config(text="Cancel")
                Thread(target=lambda: self.download_handler(url, format, self.quality.get(), self.path.get()), daemon=True).start()
    
    def download_handler(self, url: str, format: str, quality: str, path="."):
        self.process = Process(target=download, args=(url, format, quality, path))
        self.process.start()
        self.process.join()
        self.button.config(text="Download")

if __name__ == "__main__":
    root = Tk()
    app = gui(root)
    root.mainloop()
