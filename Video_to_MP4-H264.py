import sys, subprocess, time, os

FFMPEG_PATH = "./ffmpeg/ffmpeg"

def encode_video(droppedFilePath, outputPath, framerate, crf=21, preset="ultrafast"):

	ffmpeg_cmd = FFMPEG_PATH
	ffmpeg_cmd += ' -y'
	ffmpeg_cmd += ' -i {0}'.format(droppedFilePath)
	ffmpeg_cmd += ' -r {0}'.format(framerate)

	ffmpeg_cmd += ' -c:v libx264 -crf {0} -preset {1}'.format(crf, preset)
	ffmpeg_cmd += ' -c:a aac -filter_complex "[1:0] apad" -shortest'

	ffmpeg_cmd += ' {0}'.format(outputPath)

	print(ffmpeg_cmd)
	subprocess.call(ffmpeg_cmd)

if __name__ == "__main__":

	droppedFilePath = sys.argv[1]
	outputPath = droppedFilePath.rsplit(".",1)[0]+"__"+time.strftime("%Y-%m-%d_%H-%M-%S")+'.mp4'
	
	framerate = input("Type the desired Framerate:")
	if framerate == "": framerate = 24

	encode_video(droppedFilePath, outputPath, framerate)