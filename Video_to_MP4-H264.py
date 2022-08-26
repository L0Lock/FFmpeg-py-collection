import sys, subprocess, time, os, shutil

# FFMPEG_PATH = "./ffmpeg/ffmpeg"

# text formatting
class cmdUtils:
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

def encode_video(droppedFile, outputPath, framerate, crf=21, preset="ultrafast"):

	ffmpeg_cmd = FFMPEG_PATH
	ffmpeg_cmd += ' -y'
	ffmpeg_cmd += f' -i "{droppedFile}"'
	ffmpeg_cmd += f' -r {framerate}'

	ffmpeg_cmd += f' -c:v libx264 -crf {crf} -preset {preset}'
	ffmpeg_cmd += ' -c:a aac'

	ffmpeg_cmd += f' "{outputPath}"'

	print(ffmpeg_cmd)
	subprocess.call(ffmpeg_cmd)

if __name__ == "__main__":

	### Checking FFmpeg installation

	FFMPEG_PATH = shutil.which('ffmpeg') or './ffmpeg/ffmpeg'
	try:
	    subprocess.run([FFMPEG_PATH, '-version'], check=True)  # ensure ffmpeg is available
	except:
	    print(f'{cmdUtils.Red}Error: Couldn\'t find FFMPEG.{cmdUtils.Grey}')
	    input()
	    sys.exit(1)

	### FRAMERATE SETUP ###
	cls()
	framerate = input("Type the desired Framerate:")
	if framerate == "": framerate = 24
	# framerate = 24

	### Get dragndroped file and add file output suffix
	droppedFile = sys.argv[1]
	print(f'{cmdUtils.Green}Detected input file : {droppedFile}{cmdUtils.Grey}')

	outputPath = f'{droppedFile.rsplit(".",1)[0]}__{time.strftime("%Y-%m-%d_%H-%M-%S")}.mp4'
	print(f'{cmdUtils.Green}Output file will be: {outputPath}{cmdUtils.Grey}')

	### Run main fun
	encode_video(droppedFile, outputPath, framerate)

	print(cmdUtils.Sound)
	print(f"{cmdUtils.Green}Encoding succesful. This window will close after 10 seconds.{cmdUtils.Grey}")
	subprocess.call('timeout /t 10')