#!/usr/bin/python 
import StringIO

versiontbl = [ 2.5, 0, 2, 1 ]
layertbl = [ 0, 3, 2, 1 ]

bitratetbl = [
 [ ],
 [ [], # Version 1
  [ 0, 32, 64, 96, 128, 160, 192, 224, 256, 288, 320, 352, 384, 416, 448 ], #l1
  [ 0, 32, 48, 56,  64,  80,  96, 112, 128, 160, 192, 224, 256, 320, 384 ], #l2
  [ 0, 32, 40, 48,  56,  64,  80,  96, 112, 128, 160, 192, 224, 256, 320 ], #l3
 ],
 [ [], # Version 2
  [ 0, 32, 48, 56,  64,  80,  96, 112, 128, 144, 160, 176, 192, 224, 256 ], #l1
  [ 0,  8, 16, 24,  32,  40,  48,  56,  64,  80,  96, 112, 128, 144, 160 ], #l2
  [ 0,  8, 16, 24,  32,  40,  48,  56,  64,  80,  96, 112, 128, 144, 160 ], #l3
 ],
]

sampleratetbl = [
	[ ],
	[ 44100, 48000, 32000 ],
	[ 22050, 24000, 16000 ],
	]

v2_2_0_to_v2_4_0 = {
	"BUF":"RBUF",  	# Recommended Buffer Size
	"CNT":"PCNT",	# Play Count
	"COM":"COMM",	# Comments
	"CRA":"AENC",	# Audio Encryption
#	"CRM":,		# Encrypted Meta Frame
#	"ETC":,		# Equalisation timing codes
	"EQU":"EQUA",	# Equalisation
	"GEO":"GEOB",	# General Encapsulation Object
	"IPL":"IPLS",	# Involved People List
	"LNK":"LINK",	# Linked Information
	"MCI":"MCDI",	# Music CD Identifier
	"MUL":"MLLT",	# MPEG Location Lookup Table
	"PIC":"APIC",	# Attached Picture
	"POP":"POPM",	# Popularimeter
	"REV":"RVRB",	# Reverb
	"RVA":"RVAD",	# Relative Volume Adjustment
	"SLT":"SYLT",	# Syncronised Text/Lyrics
	"STC":"SYTC",	# Synconrised Tempo Codes
	"TAL":"TALB",	# Album/Movie/Show Title
	"TBP":"TBPM",	# BPM
	"TCM":"TCOM",	# Composer
	"TCO":"TCON",	# Content Type
	"TCP":"TCP",	# Compilation. DEPRECATED IN 2.4
	"TCR":"TCOP",	# Copyright Message
#	"TDA":,		# Textual Data
	"TDA":"TDAT",	# Date
	"TPL":"TDLY",	# Playlist Delay
	"TEN":"TENC",	# Encoded by
	"TFT":"TFLT",	# File type
	"TIM":"TIME",	# Time
	"TKE":"TKEY",	# Initial key
	"TLA":"TLAN",	# Language(s)
	"TLE":"TLEN",	# Length
	"TMT":"TMED",	# Media type
	"TOA":"TOPE",	# Original artist(s)/performer(s)
	"TOF":"TOFN",	# Original filename
	"TOL":"TOLY",	# Original Lyricist(s)/text writer(s)
	"TOR":"TORY",	# Original release year
	"TOT":"TOAL",	# Original album/Movie/Show title
 	"TP1":"TPE1",	# Lead artist(s)/Lead performer(s)/Soloist(s)/Performing group
	"TP2":"TPE2",	# Band/Orchestra/Accompaniment
	"TP3":"TPE3",	# Conductor/Performer refinement
	"TP4":"TPE4",	# Interpreted, remixed, or otherwise modified by
	"TPA":"TPOS",	# Part of a set
	"TPB":"TPUB",	# Publisher
	"TRC":"TSRC",	# ISRC (International Standard Recording Code)
	"TRD":"TRDA",	# Recording dates
	"TRK":"TRCK",	# Track number/Position in set
	"TSI":"TSIZ",	# Size
	"TSS":"TSSE",	# Software/hardware and settings used for encoding
	"TT1":"TIT1",	# Content group description
 	"TT2":"TIT2",	# Title/Songname/Content description
	"TT3":"TIT3",	# Subtitle/Description refinement
	"TXT":"TEXT",	# Lyricist/text writer
	"TXX":"TXXX",	# User defined text information frame
	"TYE":"TYER",	# Year
	"UFI":"UFID",	# Unique file identifier
	"ULT":"USLT",	# Unsychronized lyric/text transcription
	"WAF":"WOAF",	# Official audio file webpage
	"WAR":"WOAR",	# Official artist/performer webpage
	"WAS":"WOAS",	# Official audio source webpage
	"WCM":"WCOM",	# Commercial information
	"WCP":"WCOP",	# Copyright/Legal information
	"WPB":"WPUB",	# Publishers official webpage
	"WXX":"WXXX",	# User defined URL link frame
	"CM1":"CM1",	# Apple proprietary rating/popularity
}

genres = [ 
	u"Blues",u"Classic Rock",u"Country",u"Dance",u"Disco",u"Funk", 
	u"Grunge",u"Hip-Hop",u"Jazz",u"Metal",u"New Age",u"Oldies",u"Other", 
	u"Pop",u"R&B",u"Rap",u"Reggae",u"Rock",u"Techno",u"Industrial", 
	u"Alternative",u"Ska",u"Death Metal",u"Pranks",u"Soundtrack", 
	u"Euro-Techno",u"Ambient",u"Trip-Hop",u"Vocal",u"Jazz+Funk",u"Fusion", 
	u"Trance",u"Classical",u"Instrumental",u"Acid",u"House",u"Game", 
	u"Sound Clip",u"Gospel",u"Noise",u"Alt. Rock",u"Bass",u"Soul", 
	u"Punk",u"Space",u"Meditative",u"Instrum. Pop",u"Instrum. Rock", 
	u"Ethnic",u"Gothic",u"Darkwave",u"Techno-Industu",u"Electronic", 
	u"Pop-Folk",u"Eurodance",u"Dream",u"Southern Rock",u"Comedy", 
	u"Cult",u"Gangsta",u"Top 4u",u"Christian Rap",u"Pop/Funk",u"Jungle", 
	u"Native American",u"Cabaret",u"New Wave",u"Psychadelic",u"Rave", 
	u"Showtunes",u"Trailer",u"Lo-Fi",u"Tribal",u"Acid Punk",u"Acid Jazz", 
	u"Polka",u"Retro",u"Musical",u"Rock & Roll",u"Hard Rock",u"Folk", 
	u"Folk/Rock",u"National Folk",u"Swing",u"Fusion",u"Bebob",u"Latin", 
	u"Revival",u"Celtic",u"Bluegrass",u"Avantgarde",u"Gothic Rock", 
	u"Progress. Rock",u"Psychadel. Rock",u"Symphonic Rock",u"Slow Rock", 
	u"Big Band",u"Chorus",u"Easy Listening",u"Acoustic",u"Humour", 
	u"Speech",u"Chanson",u"Opera",u"Chamber Music",u"Sonata",u"Symphony", 
	u"Booty Bass",u"Primus",u"Porn Groove",u"Satire",u"Slow Jam", 
	u"Club",u"Tango",u"Samba",u"Folklore",u"Ballad",u"Power Ballad", 
	u"Rhythmic Soul",u"Freestyle",u"Duet",u"Punk Rock",u"Drum Solo", 
	u"A Capella",u"Euro-House",u"Dance Hall",u"Goa",u"Drum & Bass", 
	u"Club-House",u"Hardcore",u"Terror",u"Indie",u"BritPop",u"Negerpunk", 
	u"Polsk Punk",u"Beat",u"Christian Gangsta Rap",u"Heavy Metal", 
	u"Black Metal",u"Crossover",u"Contemporary Christian",u"Christian Rock",
	u"Merengue",u"Salsa",u"Thrash Metal",u"Anime",u"Jpop",u"Synthpop" 
	]

tagconvertfrom={
	"v1" : {
		"TIT2" : "TIT2",
		"TYER" : "TYER",
		"TRCK" : "TRCK",
		"TPE1" : "TPE1",
		"TALB" : "TALB",
		"COMM" : "",	# Doesn't match exactly with ID3v2
		"TCON" : "TCON",
	},
	"v2" : {
		"TYER" : "TYER",
		"TIT2" : "TIT2",
		"TRCK" : "TRCK",
		"TPE1" : "TPE1",
		"TALB" : "TALB",
		"COMM" : "COMM",
		"TCON" : "TCON",
	},
	"ape" : {
		"title" : "TIT2",
		"Track" : "TIT2",
		"Album" : "TALB",
		"album" : "TALB",
		"artist": "TPE1",
		"Year"  : "TYER",
		"genre" : "TCON",
	},
	"lyrics" : {
		"IND" : "",	# Indication, specific to lyrics v2
		"EAL" : "TALB",
		"ETT" : "TIT2",
		"EAR" : "TPE1",
		"INF" : "",	# Doesn't match exactly with COMM
		"CRC" : "",	# The CRC is pretty annoying.
	},
}

tagconvertto={}

for tagtype in tagconvertfrom:
	tagconvertto[tagtype]={}
	for tagname in tagconvertfrom[tagtype]:
		tagconvertto[tagtype][tagconvertfrom[tagtype][tagname]]=tagname

def strip_padding(x):
	while x.endswith("\x00"):
		x=x[:-1]
	return x

def parse_unicode(x):
	if x.startswith("\xff\xfe"):
		st= x.decode("utf-16-le")
	else:
		st= x.decode("utf-16-be")
	# Strip leading whitespace
	while st.startswith(u"\ufeff"):
		st=st[1:]
	return st

# How many bloody versions of id3 do we REALLY need?!

def v1(tag):
	assert len(tag)==128-3
	try:
		data={
			"TIT2" : strip_padding(tag[:30]).decode("ISO-8859-1"),
			"TPE1" : strip_padding(tag[30:60]).decode("ISO-8859-1"),
			"TALB" : strip_padding(tag[60:90]).decode("ISO-8859-1"),
			"TYER" : strip_padding(tag[90:94]).decode("ISO-8859-1"),
			"COMM" : (u"From ID3v1",strip_padding(tag[94:122]).decode("ISO-8859-1")),
			"TRCK" : unicode(ord(tag[123])),
		}
		if ord(tag[124])!=0xff:
			genreid=ord(tag[124])
			if genreid in genres:
				genrename=genres[genreid]
			else:
				genrename=u"unknowngenre#%d" % genreid
			data["TCON"]=u"("+unicode(ord(tag[124]))+u")"+genrename
		return data
	except:
		print "genres:",`tag[124]`
		raise


def v2_2_0(tag):
	data={}
	while tag!="":
		if tag[0]=="\x00":
			while tag.startswith("\x00"):
				tag=tag[1:]
			if tag!="":
				raise "Err, padding had data in it?"
			break
			
		tagid=tag[:3]
		tag=tag[3:]
		taglen=ord(tag[0])*128*128+ord(tag[1])*128+ord(tag[2])
		tag=tag[3:]
		tagdata=tag[:taglen]
		tag=tag[taglen:]
		if tagid.startswith("T"):
			if tagdata[0]=="\x00": # latin-1
				tagdata=tagdata[1:]
				if "\x00" in tagdata:
					tagdata=tagdata[:tagdata.index("\x00")]
				tagdata=tagdata.decode("ISO-8859-1")
			elif tagdata[0]=="\x01": # utf16
				if "\x00" in tagdata:
					# This is meant to remove extra null's at the end of
					# the string, but it eats into the string.
					# tagdata=tagdata[:tagdata.index("\x00")]
					pass
				tagdata=parse_unicode(tagdata[1:])
			else:
				raise "Unknown Encoding"
		elif tagid=="COM":
			encoding=tagdata[0]
			commenttype,commentdata=tagdata[1:].split("\x00",1)
			if encoding=="\x00":
				commenttype=commenttype.decode("ISO-8859-1")
				commentdata=commentdata.decode("ISO-8859-1")
			elif encoding=="\x01":
				commenttype=parse_unicode(commenttype)
				commentdata=parse_unicode(commentdata)
			else:
				raise "Unknown encoding"
			tagdata=(commenttype,commentdata)
		#print "tag:",`tagid`,"(",v2_2_0_to_v2_4_0[tagid],")"
		#print "taglen:",taglen
		#print "data:",`tagdata`
		if tagid not in v2_2_0_to_v2_4_0:
			print "Unknown ID3v2.2.0 tag:",`tagid`
		else:
			data[v2_2_0_to_v2_4_0[tagid]]=tagdata
	return data

def v2_3_0(tag, version):
	data={}
	while tag:
		if tag[0]=="\x00":
			while tag.startswith("\x00"):
				tag=tag[1:]
			if tag!="":
				# mp3ext puts data in here.  Ignore it.
				#raise "Err, padding had data in it?",`tag`
				pass
			break
		tagid=tag[:4]
		if version == 3:
			taglen=ord(tag[4])*256*256*256+ord(tag[5])*256*256+ord(tag[6])*256+ord(tag[7])
		elif version == 4:
			taglen=ord(tag[4])*128*128*128+ord(tag[5])*128*128+ord(tag[6])*128+ord(tag[7])
		tagflag=ord(tag[8])*256+ord(tag[9])
		tagdata=tag[10:10+taglen]
		#print "got tagid %s, taglen is %d (version %s)" % (tagid, taglen, version)
		tag=tag[10+taglen:]
		if tagid.startswith("T"):
			if tagdata[0]=="\x00": # latin-1
				#if "\x00" in tagdata:
				#	tagdata=tagdata[:tagdata.index("\x00")]
				tagdata=tagdata[1:].decode("ISO-8859-1")
			elif tagdata[0]=="\x01": # utf16
				#if "\x00\x00" in tagdata:
				#	tagdata=tagdata[:tagdata.index("\x00\x00")]
				tagdata=parse_unicode(tagdata[1:])
			elif tagdata[0]=="\x03": # utf8
				#if "\x00" in tagdata:
				#	tagdata=tagdata[:tagdata.index("\x00")]
				tagdata=tagdata[1:].decode("utf8")
			else:
				raise "Unknown Encoding",`tagdata[0]`
		if tagid in data and type(data[tagid]) == type([]):
			data[tagid].append(tagdata)
		elif tagid in data and data[tagid] != tagdata:
			data[tagid] = [data[tagid], tagdata]
		else:
			data[tagid]=tagdata
	return data

def lyricsv2(data):
	assert data.startswith("LYRICSBEGIN"),`data`
	data=data[11:]
	retdata={}
	while data:
		tagid=data[:3]
		tagsize=int(data[3:8])
		tagdata=data[8:8+tagsize]
		data=data[8+tagsize:]
		retdata[tagid]=tagdata
	return retdata

def apev2(ape):
	data={}
	assert ape[-32:].startswith("APETAGEX"),`ape`
	ape=ape[32:]
	while ape!="":
		apelen=ord(ape[3])*256*256*256+ord(ape[2])*256*256+ord(ape[ 1])*256+ord(ape[ 0])
		apeflg=ord(ape[7])*256*256*256+ord(ape[6])*256*256+ord(ape[ 5])*256+ord(ape[ 4])
		apekey,ape=ape[8:].split("\x00",1)
		apedata=ape[:apelen]
		ape=ape[apelen:]
		data[apekey]=apedata
	return data

# Just read id3 tags, skipping the bitstream and any other tag types
def readid3(fname):
	f=open(fname,"rb")

	f.seek(-128,2)
	id3v1=f.read(128)
	flength=f.tell()
	if id3v1.startswith("TAG"):
		v1data=v1(id3v1[3:])
		flength-=128
	else:
		v1data={}

	f.seek(0)

	# Find a ID3v2 tag
	if f.read(3)=="ID3":
		id3version = ord(f.read(1))+ord(f.read(1))/256.0
		id3flags = ord(f.read(1))
		id3len = ord(f.read(1))*128*128*128+ord(f.read(1))*128*128+ord(f.read(1))*128+ord(f.read(1))
		#print "ID3 v 2",id3version,"found"
		#print "flags:",id3flags
		#print "len:",id3len
		tag=f.read(id3len)
		if int(id3version)==2:
			v2data=v2_2_0(tag)
		elif int(id3version) in [3,4]:
			v2data=v2_3_0(tag, id3version)
		else:
			print "Unknown tag version ID3v2.",int(id3version)
			v2data={}
		v2data["version"]=u"ID3v2.%s" % unicode(id3version)
	else:
		f.seek(0)
		v2data={}

	return {
		"v2" : v2data,
		"v1" : v1data
		}

def parsemp3(fname):
	fin=open(fname,"rb")
	contents = fin.read()
	fin.close()
	f = StringIO.StringIO(contents)

	# Decode the ID3v1
	f.seek(-128,2)
	id3v1=f.read(128)
	flength=f.tell()
	if id3v1.startswith("TAG"):
		v1data=v1(id3v1[3:])
		flength-=128
	else:
		v1data={}

	# Decode as many of the tags at the end that we can
	lyricsdata={}
	apedata={}
	while 1:
		# Decode a lyrics v2.0 tag 
		f.seek(flength-9)
		lyrics=f.read(9)
		if lyrics=="LYRICS200":
			f.seek(flength-9-6)
			read=int(f.read(6))
			f.seek(flength-(9+read+6))
			data=f.read(read)
			flength-=(9+6+read)
			lyricsdata=lyricsv2(data)
			continue

		# Decode a APEv2 tag at the end
		f.seek(flength-32)
		ape=f.read(32)
		if ape.startswith("APETAGEX"):
			apever=ord(ape[11])*256*256*256+ord(ape[10])*256*256+ord(ape[ 9])*256+ord(ape[ 8])
			apelen=ord(ape[15])*256*256*256+ord(ape[14])*256*256+ord(ape[13])*256+ord(ape[12])
			apecnt=ord(ape[19])*256*256*256+ord(ape[18])*256*256+ord(ape[17])*256+ord(ape[16])
			apeflg=ord(ape[23])*256*256*256+ord(ape[22])*256*256+ord(ape[21])*256+ord(ape[20])
			flength-=32
			flength-=apelen

			#print "apever:",hex(apever)
			#print "apelen:",apelen
			#print "apecnt:",apecnt
			#print "apeflg:",hex(apeflg)
			f.seek(flength)
			apedata=f.read(apelen+32)

			apedata=apev2(apedata)

			continue

		break

	# Goto the start of the file
	f.seek(0)

	# Find a ID3v2 tag
	if f.read(3)=="ID3":
		id3version = ord(f.read(1))+ord(f.read(1))/256.0
		id3flags = ord(f.read(1))
		id3len = ord(f.read(1))*128*128*128+ord(f.read(1))*128*128+ord(f.read(1))*128+ord(f.read(1))
		#print "ID3 v 2",id3version,"found"
		#print "flags:",id3flags
		#print "len:",id3len
		tag=f.read(id3len)
		if int(id3version)==2:
			v2data=v2_2_0(tag)
		elif int(id3version) in [3,4]:
			v2data=v2_3_0(tag, id3version)
		else:
			print "Unknown tag version ID3v2.",int(id3version)
			v2data={}
		v2data["version"]=u"ID3v2.%s" % unicode(id3version)
	else:
		f.seek(0)
		v2data={}

	# Start decoding the mp3 stream
	bitstream=""
	frames=0
	duration=0
	bitrates={}
	layers={}
	unknowns=[]
	unknown=""
	errors=[]
	offset=f.tell()
	while 1:
		# skip until we find an mpeg frame header
		if f.tell()>=flength:
			break
		b=f.read(1)
		if b=="":
			print "Expected",flength-f.tell(),"more bytes!"
			break
		bitstream+=b
		b=ord(b)
		if b!=255:
			#print "not a header 1",`chr(b)`
			unknown+=chr(b)
			continue
		b=f.read(1)
		if b=="":
			bitstream=bitstream[:-1] # strip off the incomplete header
			print "Truncated header"
			break
		bitstream+=b
		b=ord(b)
		if b&0xe0 != 0xe0:
			unknown+=chr(255)+chr(b)
			continue
		if unknown!="":
			unknowns.append((offset,unknown))
			unknown=""
			offset=f.tell()
		# Now we've found mpeg header
		version=versiontbl[(b>>3)&0x03]
		layer=layertbl[(b>>1)&0x03]
		crcprotection=(b&0x01)

		#print "version:",version,"layer:",layer

		b=f.read(1)
		bitstream+=b
		b=ord(b)
		try:
			bitrate=bitratetbl[version][layer][(b>>4)&0x0F]*1000
		except:
			errors.append(("error","Unknown bitrate, V%d/%d enc: %d" %
				(version,layer,(b>>4)&0x0f)))
			continue
		try:
			samplerate=sampleratetbl[version][(b>>2)&0x03]
		except:
			errors.append(("error","Unknown samplerate, v%d enc: %d" % 
				(version,(b>>2)&0x03)))
			continue

		padding=(b>>1)&0x01
		private=(b&0x01)

		b=f.read(1)
		bitstream+=b
		b=ord(b)
		stereomode=(b>>6)&0x03
		modeextension = (b>>4)&0x03
		copyright = (b>>3)&0x01
		original = (b>>2)&0x01
		emphasis = b&0x03

		if bitrate in bitrates:
			bitrates[bitrate]+=1
		else:
			bitrates[bitrate]=1

		# Record the layers used
		if version not in layers: layers[version]={}
		if layer not in layers[version]: layers[version][layer]=0
		layers[version][layer]+=1

		#print "bitrate:",bitrate
		#print "samplerate:",samplerate
		#print "padding:",padding
		#print "private:",private
		#print "stereomode:",stereomode
		#print "mode extension:",modeextension
		#print "copyright:",copyright
		#print "original:",original
		#print "emphasis:",emphasis

		if layer==1:
			framelengthinbytes = (12 * bitrate / samplerate + padding) * 4
		else:
			framelengthinbytes = 144 * bitrate / samplerate + padding

		# Durations are in milliseconds
		if framelengthinbytes == 0 or bitrate == 0:
			frameduration = 0
			frames+=1
		else:
			frameduration=framelengthinbytes*8.0*1000/bitrate
			duration+=frameduration
			frames+=1

		#print "duration:",frameduration
		#print "skipping",framelengthinbytes
		skip=f.read(min(framelengthinbytes-4,flength-f.tell()))
		bitstream+=skip
		if len(skip) != framelengthinbytes-4:
			#errors.append("Truncated frame, missing %d bytes" % (
			#		(framelengthinbytes-4)-len(skip)))
			break
	if unknown!="":
		unknowns.append((frames,unknown))
		unknown=""

	return { 
		"filename" : fname,
		"duration" : duration,
		"frames": frames,
		"bitrates":bitrates,
		"v1" : v1data,
		"v2" : v2data,
		"lyrics" : lyricsdata,
		"unknown" : unknowns,
		"ape" : apedata,
		"errors" : errors,
		"layers" : layers,
		"bitstream" : bitstream,
		}

def validate(song):
	errors=[]
	for i in ["v1","v2","ape","lyrics"]:
		for j in song[i]:
			if type(song[i][j])==type(u"") and song[i][j].strip()!=song[i][j]:
				errors.append(("warning","%s %s tag has bad whitespace (%s)" % (i,j,`song[i][j]`)))
		for j in ["v1","v2","ape","lyrics"]:
			# No point in comparing stuff against itself
			if i>=j:
				continue
			for itagname in song[i]:
				try:
					v2tagname=tagconvertfrom[i][itagname]
				except:
					print "Unknown tag %s: %s (%s)" % (`i`,`itagname`,song[i][itagname])
					continue
				# No tag that means this?
				if v2tagname=="":
					continue
				try:
					jtagname=tagconvertto[j][v2tagname]
				except:
					print "Unknown tag %s: %s" % (`j`,`v2tagname`)

				if jtagname not in song[j]:
					continue

				itagvalue=song[i][itagname]
				jtagvalue=song[j][jtagname]
				# v1 is truncated, so ignore the rest of the tag
				if i=="v1" and v2tagname in ["TIT2","IDE1","TALB"]:
					jtagvalue=jtagvalue[:30]
				if j=="v1" and v2tagname in ["TIT2","IDE1","TALB"]:
					itagvalue=itagvalue[:30]

				# Track numbers should be treated as numbers
				itagvala = 0
				itagvalb = 0
				jtagvala = 0
				jtagvalb = 0
				if jtagvalue=="":
					jtagvalue="0"
				if v2tagname=="TRCK":
					# TODO: Deal with x/y
					if type(itagvalue) == type(u"") and itagvalue.find("/") != -1:
						[itagvala, itagvalb] = itagvalue.split("/")
					else:
						itagvala = itagvalb = int(itagvalue)
					if type(jtagvalue) == type(u"") and jtagvalue.find("/") != -1:
						[jtagvala, jtagvalb] = jtagvalue.split("/")
					else:
						jtagvala = jtagvalb = int(jtagvalue)

				# Do comparisons
				if itagvala == jtagvala and itagvalb == jtagvalb:
					continue
				# Is one tag truncated?
				if len(itagvalue)<len(jtagvalue):
					if type(jtagvalue)==type(u"") and jtagvalue.startswith(itagvalue):
						errors.append(("warning","%s %s tag truncated: (%s: %s vs %s: %s)" % (i,itagname,i,`itagvalue`,j,`jtagvalue`)))
						continue
				elif len(jtagvalue)<len(itagvalue):
					if type(itagvalue)==type(u"") and itagvalue.startswith(jtagvalue):
						errors.append(("warning","%s %s tag truncated: (%s: %s vs %s: %s)" % (j,jtagname,j,`jtagvalue`,i,`itagvalue`)))
						continue
				# Is there case differences?
				if type(itagvalue)==type(u"") and itagvalue.lower()==jtagvalue.lower():
					errors.append(("warning","%s %s tag and %s %s tag differ in case (%s: %s vs %s: %s)" % (i,itagname,j,jtagname,i,`itagvalue`,j,`jtagvalue`)))
					continue

				errors.append(("warning","%s %s tag and %s %s tag don't match (%s: %s vs %s: %s)" % (i,itagname,j,jtagname,i,`itagvalue`,j,`jtagvalue`)))
					
	return errors


def encode_keyvalue(k,v):
	n=u"\t%s: %s" % (k.decode("ascii","replace"),v.decode("ascii","replace"))
	return n.encode("ascii","replace")

if __name__=="__main__":
	import sys
	try:
		for filename in sys.argv[1:]:
			data=parsemp3(filename)
			print "Filename:",filename
			print "Duration:","%.02fs (%d:%02d:%05.02f)" % (data["duration"]/1000.0,int(data["duration"]/3600000),int(data["duration"]/60000)%60,(data["duration"]/1000.0)%60)
			print "Frames:",data["frames"]
			print "Bitrates:"
			rates=data["bitrates"].keys()
			rates.sort()
			total=0
			for i in rates:
				print "\t%8d: %8d (%3d%%)" % (i,data["bitrates"][i],data["bitrates"][i]*100.0/data["frames"])
				total+=i*data["bitrates"][i]
			print "\t Average: %11.02f" % (total*1.0/data["frames"])
			print "Encodings:"
			for i in data["layers"]:
				for j in data["layers"][i]:
					print "\tVersion %d, Layer %d: %8d (%3d%%)" % (i,j,data["layers"][i][j],data["layers"][i][j]*100/data["frames"])
			if data["v1"]!={}:
				print "TAG: ID3v1:"
				for i in data["v1"]:
					print (u"\t%s: %s" % (i,data["v1"][i])).encode("ascii","replace")
			if data["v2"]!={}:
				print "TAG: ID3v2:"
				for i in data["v2"]:
					if i == "APIC":
						print "\t%s: Picture attached (%d bytes)" % (i,len(data["v2"][i]))
					elif i == "TXXX" or i == "UFID" or i == "TMCL" or i == "TIPL":
						print "\t%s:" % i
						infos = data["v2"][i]
						if type(infos) != type(list()):
							infos = [infos]
						for info in infos:
							if len(info.split("\0")) != 2:
								print "\t\tBad data:",`info`
							else:
								print "\t\t%s: %s" % tuple(info.split("\0"))
					elif type(data["v2"][i])==type(u""):
						print (u"\t%s: %s" % (i,data["v2"][i])).encode("ascii","replace")
					else:
						print ("\t%s: %s" % (repr(i),repr(data["v2"][i])))
			if data["lyrics"]!={}:
				print "TAG: Lyrics v2:"
				for i in data["lyrics"]:
					print (u"\t%s: %s" % (i,data["lyrics"][i])).encode("ascii","replace")
			if data["ape"]!={}:
				print "TAG: APEv2:"
				for i in data["ape"]:
					print encode_keyvalue(i,data["ape"][i])
			if data["unknown"]!=[]:
				print "Unknown data:"
				for (offset,raw) in data["unknown"]:
					print (u"\t%d: %s" % (offset,`raw`)).encode("ascii","replace")
			errors=data["errors"]

			errors+=validate(data)
			if errors!=[]:
				print "Errors:"
				for i in data["errors"]:
					print "\t%s" % `i`
			print

	except:
		print
		print "filename:",filename
		raise
