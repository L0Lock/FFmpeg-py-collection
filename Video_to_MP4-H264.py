import sys, subprocess, time, os, shutil

# FFMPEG_PATH = "./ffmpeg/ffmpeg"

# text formatting
class colors:
    Purple = '\033[95m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    Green = '\033[92m'
    Tan = '\033[93m'
    Red = '\033[91m'
    Grey = '\033[0m' # Default
    White = '\033[1m'

# console clearer
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def encode_video(droppedFilePath, outputPath, framerate, crf=21, preset="ultrafast"):

	ffmpeg_cmd = FFMPEG_PATH
	ffmpeg_cmd += ' -y'
	ffmpeg_cmd += ' -i "{0}"'.format(droppedFilePath)
	ffmpeg_cmd += ' -r {0}'.format(framerate)

	ffmpeg_cmd += ' -c:v libx264 -crf {0} -preset {1}'.format(crf, preset)
	ffmpeg_cmd += ' -c:a aac'

	ffmpeg_cmd += ' "{0}"'.format(outputPath)

	print(ffmpeg_cmd)
	subprocess.call(ffmpeg_cmd)

if __name__ == "__main__":

	### Checking FFmpeg installation

	FFMPEG_PATH = shutil.which('ffmpeg') or './ffmpeg/ffmpeg'
	try:
	    subprocess.run([FFMPEG_PATH, '-version'], check=True)  # ensure ffmpeg is available
	except:
	    print(f"{colors.Red}FFmpeg not found!{colors.Grey}")
	    input()
	    sys.exit(1)

	### Get dragndroped file and add file output suffix
	droppedFilePath = sys.argv[1]
	# droppedFilePath = "./testSubjects/testVid.mp4"
	outputPath = droppedFilePath.rsplit(".",1)[0]+"__"+time.strftime("%Y-%m-%d_%H-%M-%S")+'.mp4'
	
	### FRAMERATE SETUP ###
	cls()
	framerate = input("Type the desired Framerate:")
	if framerate == "": framerate = 24
	# framerate = 24

	### Run main fun
	encode_video(droppedFilePath, outputPath, framerate)

	print(f"{colors.Green}Encoding succesful. This window will close after 10 seconds.{colors.Grey}")
	subprocess.call('timeout /t 10')