import sys, subprocess, time, os, shutil

# FFMPEG_PATH = "./ffmpeg/ffmpeg"

class cmdUtils:
    Purple = '\033[95m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    Green = '\033[92m'
    Tan = '\033[93m'
    Red = '\033[91m'
    Grey = '\033[0m' # Default
    White = '\033[1m'
    Sound = '\007'

# console clearer
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def cover_video(droppedFile, outputPath, cover, container):

    ffmpeg_cmd = FFMPEG_PATH
    ffmpeg_cmd += ' -y'
    ffmpeg_cmd += f' -i "{droppedFile}"'

    if container == "mp4":
        ffmpeg_cmd += f' -i "{cover}"'

        ffmpeg_cmd += ' -map 0 -map 1'
        ffmpeg_cmd += ' -c copy'
        ffmpeg_cmd += ' -c:v:1 mjpeg'
        ffmpeg_cmd += ' -disposition:v:1 attached_pic'

    if container == "mkv":
        ffmpeg_cmd += f' -attach "{cover}"'
        ffmpeg_cmd += ' -metadata:s:t mimetype=image/jpeg'
        ffmpeg_cmd += ' -c copy'
        ffmpeg_cmd += ' -map 0'

    ffmpeg_cmd += f' "{outputPath}"'

    print(ffmpeg_cmd)
    subprocess.call(ffmpeg_cmd)

if __name__ == "__main__":

    ### Checking FFmpeg installation

    FFMPEG_PATH = shutil.which('ffmpegu') or './ffmpeg/ffmpeg'
    try:
        subprocess.run([FFMPEG_PATH, '-version'], check=True)  # ensure ffmpeg is available
    except:
        print(f'{cmdUtils.Red}Error: Couldn\'t find FFMPEG.{cmdUtils.Grey}')
        input()
        sys.exit(1)

    ### Get dragndroped file and add file output suffix
    droppedFile = sys.argv[1]
    print(f'{cmdUtils.Green}Detected input file : {droppedFile}{cmdUtils.Grey}')

    # droppedFile = "./testSubjects/sequence/throwhands%04d.jpg"
    outputPath = f'{droppedFile.rsplit(".",1)[0]}__{time.strftime("%Y-%m-%d_%H-%M-%S")}.{droppedFile.rsplit(".",1)[1]}'
    print(f'{cmdUtils.Green}Output file will be: {outputPath}{cmdUtils.Grey}')

    ### CONTAINER CHECK ###

    def get_container(file):
        _container = droppedFile.rsplit(".",1)[1]
        if _container.lower() == "mp4":
            return "mp4"
        if _container.lower() == "mkv":
            return "mkv"

        else:
            print(f'{cmdUtils.Red}Error: Only MP4 and MKV files are supported for now.{cmdUtils.Grey}')
            sys.exit(1)

    ### COVER SETUP ###
    def get_cover(file):
        _cover = os.path.dirname(file) + "/cover.jpg"
        print(f'{cmdUtils.Tan}Checking if {_cover} exists...{cmdUtils.Grey}')
        if os.path.exists(_cover) == True:
            return _cover
        else:
            print(f'{cmdUtils.Red}Error: Couldn\'t find "cover.jpg" alongside input video file.{cmdUtils.Grey}')
            sys.exit(1)

    cover = get_cover(droppedFile)
    print(f'{cmdUtils.Green}Found cover file: {cover}{cmdUtils.Grey}')
    container = get_container(droppedFile)
    print(f'{cmdUtils.Green}Detected container: {container}{cmdUtils.Grey}')

    ### Run main fun
    cover_video(droppedFile, outputPath, cover, container)

    print(cmdUtils.Sound)
    print(f'{cmdUtils.Green}Successfully created {outputPath}\nThis window will close after 10 seconds.{cmdUtils.Grey}')
    subprocess.call('timeout /t 10')