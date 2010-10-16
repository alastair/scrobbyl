#!/usr/bin/python

import os
import sys
import urllib2
import urlparse
import urllib
import echonestconf
import json

def _do_en_query(method, postdata=None, **kwargs):
        args = {}
        for k,v in kwargs.items():
                args[k] = v.encode("utf8")
	args["api_key"] = echonestconf.echonest_key
	args["format"]="json"

        url=urlparse.urlunparse(('http',
                'developer.echonest.com',
                '/api/v4/%s' % method,
                '',
                urllib.urlencode(args),
                ''))
	print >> sys.stderr, "opening url",url
        f = urllib2.Request(url)
        try:
                f = urllib2.urlopen(f)
        except Exception, e:
                print >> sys.stderr, e.msg
                print >> sys.stderr, e.fp.read()
                raise
	return json.loads(f.read())

def artist_profile(artistid):
	return _do_en_query("artist/profile", bucket="id:musicbrainz", id=artistid)

def fp_lookup(code):
	return _do_en_query("song/identify", code=code)

def track_profile(id):
	return _do_en_query("track/profile", id=id)

def pp(data):
	print json.dumps(data, indent=4)

def main():
	pp(artist_profile("ARH6W4X1187B99274F"))

if __name__ =="__main__":
	if len(sys.argv) < 2:
		print "usage: %s [mbid|] <args>" % sys.argv[0]
		sys.exit()
	else:
		main()
