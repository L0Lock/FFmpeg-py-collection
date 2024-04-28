# FFmpeg-py-collection

[![GitHub license](https://img.shields.io/github/license/L0Lock/ffmpeg-py-collection?style=for-the-badge)](https://github.com/L0Lock/FFmpeg-py-collection/blob/master/LICENSE)  [![ko-fi](https://github.com/L0Lock/convertRotationMode/raw/main/Prez/SupportOnKofi.jpg)](https://ko-fi.com/H2H818FHX)

A collection of python files for some usefull ffmpeg conversions.


## Installation

- Download the [latest release](https://github.com/L0Lock/FFmpeg-py-collection/releases/latest) and unpack it wherever you want.
- If you don't have FFmpeg already, download the [lastest "static" ffmpeg pack](https://ffmpeg.zeranoe.com/builds/). You can either put the ffmpeg executables in the repository's `ffmpeg` folder, or register ffmpeg's path to your operating system (**recommended!**).

<details>
  <summary>Click to expand: <b>How to register ffmpeg in Windows</b></summary>

 - Browse in the archive up to the `bin` subfolder containing ffmpeg, ffprobe and ffplay executables. Uncompress the `bin` folder where you want. This guide will use: `C:\ffmpeg\bin`

- Register ffmpeg, ffprobe & ffplay to environment variables

  **Through command line (fastest):**
  
  - Open the terminal (press <kbd>![Windows key](http://i.imgur.com/AAjIi.png)</kbd><kbd>X</kbd> and click `Terminal`)
  - enter the following command:
    ```bash
    setx PATH "%PATH%;C:\ffmpeg\bin"
    ```
  
  **Through user interface:**

  - Startmenu Search: "Edit Environment Variables for your account"
  - <kbd>Environment variables</kbd>
  - Under "User variables for \<username\>", find and double-click "Path" 
  - <kbd>New</kbd>
  - Type in `C:\ffmpeg\bin` and <kbd>&#9166; Enter</kbd>
  - <kbd>Ok</kbd>
  - <kbd>Ok</kbd>
  - <kbd>Ok</kbd>

</details>

## How to use

### General usage

Drag and drop your media file onto the .py file with the desired effect. Type in the desired framerate when asked, and press <kbd>&#9166; Enter</kbd>. Pressing <kbd>&#9166; Enter</kbd> without typing a framerate will result in the default 24 fps.

### Adding Cover

Same general usage, but:
- your picture file must be named `cover.jpg` and in the same folder as the source video.

![demo covers](https://github.com/L0Lock/FFmpeg-py-collection/blob/main/assets/img/covers_demo.jpg)

Do check those links first:

 - [Enabling cover thumbnails on your system](https://codecalamity.com/guides/video-thumbnails/)
 - [Cover variants](https://www.matroska.org/technical/attachments.html):

FileName | Image Orientation | Pixel Length of Smallest Side
-- | -- | --
cover.jpg | Portrait or square | 600
small_cover.png | Portrait or square | 120
cover_land.png | Landscape | 600
small_cover_land.jpg | Landscape | 120
