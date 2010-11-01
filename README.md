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

FAQ
----------
**Wait, I can't work out how to run it**

  Scrobbyl is only in proof of concept stage now.  We'll have an OS X and Linux frontend available soon.

**How can I scrobble from a cafe/stereo/concert/store?**

  Sorry, you can only scrobble from a direct line-in at the moment.

