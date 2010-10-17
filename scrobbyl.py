#!/usr/bin/env python

import sys
import os
import subprocess
import json
import echonest
import time

def fingerprint(file):
	platform = os.uname()[0]
	if platform == "Darwin":
		codegen = "./codegen.Darwin"
	elif platform == "Linux":
		codegen = "./codegen.Linux-i686"
	proclist = [codegen, os.path.abspath(file), "0", "20"]
	p = subprocess.Popen(proclist, stdout=subprocess.PIPE)
	code = p.communicate()[0]
	return json.loads(code)

def main(file):
	statusfile = os.path.expanduser("~/.scrobbyl")
	lines = []
	if os.path.exists(statusfile):
		fp = open(statusfile, "r")
		lines = fp.readlines()
		fp.close()
	lasttime = 0
	lastartist = ""
	lasttrack = ""
	if len(lines) == 3:
		lasttime = int(lines[0])
		lastartist = lines[1]
		lasttrack = lines[2]
	
	f = fingerprint(file)

	code = f[0]["code"]
	song = echonest.fp_lookup(code)
	echonest.pp(song)

	if "response" in song and "status" in song["response"] \
			and song["response"]["status"]["message"] == "Success":
		track = song["response"]["songs"][0]["title"]
		artist = song["response"]["songs"][0]["artist_name"]
		now = time.time()

		print (now-lasttime)
		if now - lasttime < 100:
			# Only scrobble if we've just been playing
			if lasttrack != "" and lasttrack != track:
				print "Last track was",lasttrack,"now",track,", scrobbling"
			else:
				print "same song"
		else:
			print "too long since we last did it,", now-lasttime
		fp = open(statusfile, "w")
		fp.write("%d\n%s\n%s" % (now, artist, track))
		fp.close()

if __name__=="__main__":
	if len(sys.argv) < 2:
		print >>sys.stderr, "usage: %s <file>" % sys.argv[0]
		sys.exit(0)
	main(sys.argv[1])
