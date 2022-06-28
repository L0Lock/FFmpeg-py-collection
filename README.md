# FFmpeg-py-collection

[![GitHub license](https://img.shields.io/github/license/L0Lock/ffmpeg-py-collection)](https://github.com/L0Lock/FFmpeg-py-collection/blob/master/LICENSE)  [![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/H2H818FHX)

A collection of python files for some usefull ffmpeg conversions.


## Installation

- Download the [latest release](https://github.com/L0Lock/FFmpeg-py-collection/releases/latest) and unpack it wherever you want.
- If you don't have FFmpeg already, download the [lastest "static" ffmpeg pack](https://ffmpeg.zeranoe.com/builds/). You can either put the ffmpeg executables in the repository's `ffmpeg` folder, or register ffmpeg to your operating system.

<details>
  <summary>Click to expand: How to register ffmpeg in Windows</summary>

 - Browse in the archive up to the `bin` subfolder containing ffmpeg, ffprobe and ffplay executables. Uncompress the `bin` folder (in this example we'll use `C:\ffmpeg\bin`

- Register ffmpeg, ffprobe & ffplay to environment variables

<details>
<summary><b>Through command lines:</b></summary>
  
  - Hit the windows key, write down `cmd` and press <kbd>&#9166; Enter</kbd>
  
  - Enter the following command, line after line:
    
    ```
    set ffmpeg=C:\ffmpeg\bin
    set ffprobe=C:\ffmpeg\bin
    set ffplay=C:\ffmpeg\bin
    ```
</details>

<details>
<summary><b>Through user interface:</b></summary>

Do the following:

  ```
  My Computer
  Environment variables
  Add
  Name: ffmpeg
  Value: C:\ffmpeg\bin
  Add
  Name: ffprobe
  Value: C:\ffmpeg\bin
  Add
  Name: ffplay
  Value: C:\ffmpeg\bin
  Ok
  Ok
  ```
</details>
</details>

## How to use

### General usage

Drag and drop your media file onto the .py file with the desired effect. Type in the desired framerate when asked, and press <kbd>&#9166; Enter</kbd>. Pressing <kbd>&#9166; Enter</kbd> without typing a framerate will result in the default 24 fps.