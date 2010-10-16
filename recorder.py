#!/usr/bin/python 

import pyaudio
import sys
import wave

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5 

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS, 
                rate = RATE, 
                input = True,
                output = True,
                frames_per_buffer = chunk)

print "* recording"
all = []
for i in range(0, 44100 / chunk * RECORD_SECONDS):
    data = stream.read(chunk)
    all.append(data)
    # check for silence here by comparing the level with 0 (or some threshold) for 
    # the contents of data.
    # then write data or not to a file

print "* done"

stream.stop_stream()
stream.close()
p.terminate()

data = ''.join(all)
wf = wave.open("recorded.wav", 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(data)
wf.close()
