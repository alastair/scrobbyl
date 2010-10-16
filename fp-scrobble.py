#!/usr/bin/python

import sys
import os
import fp
import echonest

supported_types = [".wav", ".mp3", ".ogg", ".flac"]

def main(dir):
	matches = {}
	artists = {}
	count = 0
	for f in os.listdir(dir):
		print "file",f
		if os.path.splitext(f)[1] not in supported_types:
			print "skipping",f
			continue
		code = fp.fingerprint(os.path.join(dir, f))
		match = echonest.fp_lookup(code)
		echonest.pp(match)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print >>sys.stderr, "usage: %s <dir>" % sys.argv[0]
		sys.exit(1)
	else:
		main(sys.argv[1])
