from __future__ import unicode_literals

import sys
import os
import subprocess
import argparse
import glob
import math
import random
from subprocess import PIPE, Popen

import json
from collections import OrderedDict
import io

if sys.platform == "win32":
    CONVERT_BIN = "convert.exe"
    MOVE = "move "
    MKDIR = "md "
elif sys.platform == 'linux' or sys.platform == 'linux2':
    CONVERT_BIN = "convert"
    MOVE = "mv "
    MKDIR = "mkdir "
elif sys.platform == 'darwin':
    CONVERT_BIN = "convert"
    MOVE = "mv "
    MKDIR = "mkdir "

def getRandomInt(min, max):
    return int(math.floor(random.random() * (max - min)) + min);

def magick(videoFile):
    # home = os.path.dirname(os.path.realpath(__file__))

    # replace with random seed function
    randomRotate = [313, 17, 102, 29, 39, 256, 60, 247, 153, 333, 104, 254, 70, 123, 74, 312, 149, 152, 83, 36, 126, 308, 117, 252, 202, 277, 116, 175, 51, 325, 16, 96, 251, 216, 245, 224, 100, 262, 325, 59, 94, 4, 256, 298, 18, 213, 312, 283, 138, 162, 99, 118, 63, 260, 201]

    home = os.path.expanduser("~")
    inputFolder = home + "/_create/cf_photoshop/flags/embossed-fixedsize"
    outputFolder = home + "/_create/cf_photoshop/flags/testout/"

    # WEIRD ERRORS

    # convert: unable to open image '/Users/samenglander/_create/cf_photoshop/flags/imagerotation/Flag_of_Turkey.svg.png_NEWSIZE.png': No such file or directory @ error/blob.c/OpenBlob/3143.
    # convert: WriteBlob Failed `/Users/samenglander/_create/cf_photoshop/flags/imagerotation/Flag_of_Turkey.svg.png_NEWSIZE.png' @ error/png.c/MagickPNGErrorHandler/1711.

    # https://stackoverflow.com/questions/12298893/error-writeblob-failed-using-imagemagick-6-7-9

    i = 0
    for file in os.listdir(inputFolder):
        if file.endswith(".png"):
            newInputPath = os.path.join(inputFolder, file)
            newOutputPath = os.path.join(outputFolder, file)
            # randomInt = str(getRandomInt(1, 360))
            randomInt = str(randomRotate[i])
            i = i + 1
            # cmd = ['convert', newInputPath, newOutputPath]
            # print(randomInt)

            # try sizes:
            # 500x333
            # 250x167
            # 125x83
            cmd = ['convert', newInputPath, '-resize', '500x333', '-background', 'skyblue', '-virtual-pixel', 'transparent', '+distort', 'SRT', randomInt, '+repage', newOutputPath+'_ROTATED.png']
            output = subprocess.call(cmd)

def check_arg(args=None):

# Command line options
# Currently, only the url option is used

    parser = argparse.ArgumentParser(description='download video')
    parser.add_argument('-i', '--input',
                        help='input folder',
                        required='True')

    results = parser.parse_args(args)
    return (results.input)


# Usage sample:
#    syntax: python iframe_extract.py -u url
#    (ex) python iframe_extract.py -u https://www.youtube.com/watch?v=dP15zlyra3c

if __name__ == '__main__':
    i = check_arg(sys.argv[1:])
    magick(i)
