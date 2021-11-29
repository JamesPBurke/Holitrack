#!/usr/bin/env python3

import tweepy
import twauth
import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

class IDPrinter(tweepy.Stream):

    def on_status(self, status):
        status_text = "Yes, I can hear you @" + status.user.screen_name
        print(status.user.screen_name)
        print(status.text)
        screen_name = status.user.screen_name
        statid = status.id
        self.api.update_status(status_text, in_reply_to_status_id = statid)
        xpos = 0
        done = False
        while done == False:
            xpos += 1
            if (xpos > self.matrix.width):
                done = True
            self.matrix.SetImage(animage, -xpos)
            self.matrix.SetImage(animage, -xpos + self.matrix.width)
            time.sleep(0.03)

auth = tweepy.OAuthHandler(twauth.API_KEY, twauth.API_SECRET)
auth.set_access_token(twauth.ACCESS_TOKEN, twauth.ACCESS_SECRET)

printer = IDPrinter(
    twauth.API_KEY, twauth.API_SECRET,
    twauth.ACCESS_TOKEN, twauth.ACCESS_SECRET
)

IDPrinter.api = tweepy.API(auth)

image = Image.open("cat.png")

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'

IDPrinter.matrix = RGBMatrix(options=options)

# Create a thumbnail that first our screen
image.thumbnail((IDPrinter.matrix.width, IDPrinter.matrix.height), Image.ANTIALIAS)

animage = image.convert('RGB')

printer.filter(track=["#elfgoat"])

