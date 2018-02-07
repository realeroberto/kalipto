import random
import string
import socket
import threading
import time
import runpy
import wget

from twitter import *
from stegano import lsb


#-----------------------------------------------------------------------
# load API credentials 
#-----------------------------------------------------------------------
config = runpy.run_path("config.py")

#-----------------------------------------------------------------------
# create twitter API objects
#-----------------------------------------------------------------------
twitter = Twitter(
	auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]),
	retry = True)
twitter_upload = Twitter(domain='upload.twitter.com',
	auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]),
	retry = True)

#-----------------------------------------------------------------------
# post a new status
#-----------------------------------------------------------------------
def send():
    while True:
        msg = input('\nLOCAL > ')
        if msg and len(msg) > 0:
            secret = lsb.hide("example.png", msg)
            secret.save("example-steg.png")
            with open("example-steg.png", "rb") as imagefile:
                imagedata = imagefile.read()
            id_img = twitter_upload.media.upload(media = imagedata, media_category = "tweet_image")["media_id_string"]
            results = twitter.statuses.update(media_ids = id_img)

#-----------------------------------------------------------------------
# read new statuses
#-----------------------------------------------------------------------
def receive():
    since_id = None
    while True:
        if not since_id:
            statuses = twitter.statuses.home_timeline(count = 10)
        else:
            statuses = twitter.statuses.home_timeline(since_id = since_id)

        media_files = set()
        for status in statuses:
            media = status['entities'].get('media', [])
            if(len(media) > 0):
                media_files.add(media[0]['media_url'])
            #text = status["text"]
            #since_id = status["id"]

        for media_file in media_files:
            filename = wget.download(media_file, bar=None)
            text = lsb.reveal(filename)
            print('\nREMOTE > ' + text)

        time.sleep(60)

#-----------------------------------------------------------------------
# main loop
#-----------------------------------------------------------------------
def main():
    thread_send = threading.Thread(target = send)
    thread_receive = threading.Thread(target = receive)
    thread_send.start()
    thread_receive.start()
