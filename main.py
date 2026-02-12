from tkinter import Tk

class gui:
    def __init__(self, root: Tk):
        root.title("Media Downloader")

if __name__ == "__main__":
    root = Tk()
    app = gui(root)
    root.mainloop()