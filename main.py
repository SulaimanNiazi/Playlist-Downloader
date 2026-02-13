from tkinter import Tk, Label, Entry, Button, StringVar, BooleanVar, Checkbutton
from tkinter.ttk import Combobox
from tkinter.filedialog import askdirectory

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
        button = Button(root, text="Download", command=self.button_pressed)
        button.grid(column=3, row=0, padx=10, sticky="we")

        Label(root, text="Location:").grid(column=0, row=1, padx=10, sticky="we")
        self.path = Entry(root)
        self.path.grid(column=1, columnspan=2, row=1, padx=10, sticky="we")
        Button(root, text="Browse", command=lambda: self.path.insert(0, askdirectory(initialdir="."))).grid(column=3, row=1, padx=10, sticky="we")

        formats = ["No Downloads", "m4a", "mkv", "mp3", "mp4"]
        qualities = ["8K UHD 4320p", "4K UHD 2160p", "QHD 1440p", "FHD 1080p", "HD 720p", "SD 480p", "SD 360p", "LD 240p", "LD 144p"]
        
        Label(root, text="Options:").grid(column=0, row=2, padx=10, sticky="we")
        self.format = StringVar(value=formats[0])
        format_combo = Combobox(root, state="readonly", textvariable=self.format, values=formats)
        format_combo.grid(column=1, row=2, padx=10, sticky="we")
        self.quality = StringVar()
        quality_combo = Combobox(root, state="readonly", textvariable=self.quality)
        quality_combo.grid(column=2, row=2, padx=10, sticky="we")
        self.catalog_option = BooleanVar()
        Checkbutton(root, text="Catalog", variable=self.catalog_option).grid(column=3, row=2, padx=10, sticky="we")
        def set_qualities(event):
            if self.format.get() in ("mkv", "mp4"):
                self.quality.set(qualities[3])
                quality_combo.config(values=qualities)
            else:
                self.quality.set("")
                quality_combo.config(values=[])
        format_combo.bind("<<ComboboxSelected>>", set_qualities)

    def button_pressed(self):
        pass

if __name__ == "__main__":
    root = Tk()
    app = gui(root)
    root.mainloop()