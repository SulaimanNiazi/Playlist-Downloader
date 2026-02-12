from tkinter import Tk

class gui:
    def __init__(self, root: Tk):
        root.title("Media Downloader")
        root.minsize(700, 400)
        root.maxsize(root.winfo_screenwidth(), root.winfo_screenheight())

if __name__ == "__main__":
    root = Tk()
    app = gui(root)
    root.mainloop()