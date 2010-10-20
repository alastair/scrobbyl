Scrobbyl
==========================

Don't you wish you could **scrobb**le your vin**yl**?  Well, now you can.

What it does
------------

 1. Listens to line-in for 20 seconds
 2. Uses the echonest fingerprinter to work out what the song is
 3. If this segment is different to the previous 20 seconds, scrobble it
 4. rinse and repeat

To run
----------
 
 * make sure ffmpeg is in your path
 * run 'python lastfm.py auth' to link scrobbyl to your account
 * plug in your turntable through your line in
 * run

To do
----------
Stay tuned for fingerprinting with a microphone instead of line-in
