#!/usr/bin/python
# Copyright 2013-2015 Pervasive Displays, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied.  See the License for the specific language
# governing permissions and limitations under the License.


import sys
import os
import time
from PIL import Image
from PIL import ImageOps
from EPD import EPD
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import subprocess
import shlex




def main(argv):
    """main program - display list of images"""
    subprocess.call(shlex.split('/home/pi/speedtest-cron/speedtest2.sh'))
    x = 0
    with open('graph.txt') as f:
        lines = f.readlines()
        y = [line.split()[0] for line in lines]

    with open('graph2.txt') as f2:
        lines = f2.readlines()
        y2 = [line.split()[0] for line in lines]
        #x = [x++1 for line in lines]

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title("Speed Test")
    ax1.plot(y, c='r', label='Down')
    ax1.plot(y2, c='b', label='Up')
    leg = ax1.legend()
    fig.set_size_inches(3.8, 2.5)
    fig.savefig('temp.png', dpi=75)


    epd = EPD()

    epd.clear()

    #print('panel = {p:s} {w:d} x {h:d}  version={v:s} COG={g:d} FILM={f:d}'.format(p=epd.panel, w=epd.width, h=epd.height, v=epd.version, g=epd.cog, f=epd.film))

    for file_name in argv:
        if not os.path.exists(file_name):
            sys.exit('error: image file{f:s} does not exist'.format(f=file_name))
        #print('display: {f:s}'.format(f=file_name))
        display_file(epd, file_name)


def display_file(epd, file_name):
    """display centre of image then resized image"""

    image = Image.open(file_name)
    image = ImageOps.grayscale(image)

    # crop to the middle
    w,h = image.size
    x = w / 2 - epd.width / 2
    y = h / 2 - epd.height / 2

    cropped = image.crop((x, y, x + epd.width, y + epd.height))
    bw = cropped.convert("1", dither=Image.FLOYDSTEINBERG)

    epd.display(bw)
    epd.update()


    #time.sleep(3) # delay in seconds

    #rs = image.resize((epd.width, epd.height))
    #bw = rs.convert("1", dither=Image.FLOYDSTEINBERG)

    #epd.display(bw)
    #epd.update()

    #time.sleep(3) # delay in seconds

# main
if "__main__" == __name__:
    if len(sys.argv) < 2:
        sys.exit('usage: {p:s} image-file'.format(p=sys.argv[0]))
    main(sys.argv[1:])
