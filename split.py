#/usr/bin/python

import parsemp3
import sys
import os
import math
import tempfile
import subprocess

def main():
	file = os.path.abspath(sys.argv[1])
	data = parsemp3.parsemp3(sys.argv[1])
	print data["duration"]/1000

	tracklen = data["duration"]/1000
	splits = math.ceil(tracklen/20)

	for i in range(splits):
		start = i * 20
		end = start + 20
		print "start",start,"end",end
		(fd,outfile)=tempfile.mkstemp(suffix=".wav")
		os.close(fd)
		args = ["ffmpeg", "-y", "-i", file, "-ac", "1", "-ar", "22050", "-f", "wav", "-t", "20", "-ss", "%d" %start, outfile]
		subprocess.call(args, stderr=open("/dev/null", "w"))
		os.rename(outfile, "data/%d.wav" %start)


if __name__=="__main__":
	main()
