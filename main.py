from playlist_downloader import freeze_support, gui

if __name__ == '__main__':
    freeze_support()
    app = gui()
    app.run()
