from tkinter import Tk, Label, Entry, Button

class gui:
    def __init__(self, root: Tk):
        root.title("Media Downloader")
        root.minsize(700, 400)
        root.maxsize(root.winfo_screenwidth(), root.winfo_screenheight())

        for i in range(3):
            root.columnconfigure(i, weight=1)
            root.rowconfigure(i, weight=1)
        root.columnconfigure(1, weight=10)

        Label(root, text="Enter URL: ").grid(column=0, row=0, padx=10, sticky="we")
        self.url_bar = Entry(root)
        self.url_bar.grid(column=1, row=0, padx=10, sticky="we")
        Button(root, text="Start", command=self.start).grid(column=2, row=0, padx=10, sticky="we")
    
    def start(self):
        print(self.url_bar.get())

if __name__ == "__main__":
    root = Tk()
    app = gui(root)
    root.mainloop()