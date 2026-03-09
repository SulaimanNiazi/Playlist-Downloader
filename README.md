# Playlist Downloader

**Playlist Downloader** is a utility built on top of **yt-dlp** that allows you to download YouTube videos or extract structured metadata from videos and playlists.

The tool can either:

* **Download videos**
* **Download audio-only files**
* **Catalogue videos or entire playlists** by exporting their metadata to a **JSON file**

This makes it useful for archiving playlists, analyzing channels, or keeping structured records of video collections.

---

## Download

Pre-built Windows executables are available on the Releases page.

⬇ **[Download the latest version](https://github.com/SulaimanNiazi/Playlist-Downloader/releases/latest/download/Playlist.Downloader.exe)**

---

## Features

* Download individual YouTube videos
* Download audio-only versions of videos
* Choose video resolutions from **144p up to 8K**
* Save videos as **MP4 or MKV**
* Save audio as **M4A or MP3**
* Extract metadata from individual videos
* Catalogue entire playlists
* Export collected data to **JSON**
* Identify which video belongs to which **uploader/channel**
* Uses your existing **browser login session** for accessing restricted videos

---

## Requirements

* Python 3.9+
* `yt-dlp`
* A browser logged into YouTube

Supported browsers for authentication:

* Chrome
* Firefox
* Vivaldi

---

## Installation (Manual / Python)

Clone the repository and install the required dependency:

```bash id="rj3e4d"
pip install yt-dlp
```

Then run the application:

```bash id="r7id0o"
python main.py
```

---

## Executable Version

Pre-built **Windows executable files** are available in the **Releases** section of this repository.

Download the latest `.exe` file and run it directly — no Python installation required.

---

## Authentication Requirement

The program requires you to be **logged into YouTube in your browser**.
The tool reads your browser session to allow access to videos that require login.

Make sure you are logged in to YouTube in one of the following browsers before running the program:

* Chrome
* Firefox
* Vivaldi

---

## Usage

### Download a Video

1. Copy a YouTube video URL
2. Paste it into the application
3. Select the desired **resolution (144p – 8K)**
4. Choose the format (**MP4 or MKV**)
5. Start the download

The video will be downloaded using **yt-dlp**.

---

### Download Audio Only

You can extract only the audio track from a video.

Available audio formats:

* **M4A**
* **MP3**

This is useful for downloading music, podcasts, or spoken content.

---

### Catalogue a Video

Instead of downloading the video, you can extract metadata such as:

* Title
* Channel / uploader
* Upload date
* Duration
* Description
* Video ID

The information is exported as a **JSON file**.

---

### Catalogue a Playlist

When a playlist URL is provided, the application will:

* Process every video in the playlist
* Extract metadata for each video
* Record which **uploader/channel** published each video
* Export the full dataset to a **JSON catalogue**

This is useful for:

* Archiving playlists
* Analyzing creator contributions
* Creating searchable video indexes

---

## Output Format

Metadata is exported in **JSON** format for easy processing.

Example structure:

```json id="h3ewv7"
{
  "playlist_title": "Example Playlist",
  "videos": [
    {
      "title": "Example Video",
      "uploader": "Example Channel",
      "video_id": "abc123",
      "url": "https://youtube.com/watch?v=abc123"
    }
  ]
}
```

---

## Disclaimer

This project relies on **yt-dlp** for media extraction.
Please ensure that you comply with **YouTube's Terms of Service** and applicable copyright laws when downloading or archiving content.

---

## Credits

* Powered by **yt-dlp**
* Built as a lightweight tool for downloading and cataloguing YouTube content
