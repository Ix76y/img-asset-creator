#!/usr/bin/env python3

import sys
import os
import glob
import subprocess
import pkg_resources
import imgasset_helper as h
import path_helper as ph

required = {'pillow'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    print(h.MSG_NOT_INSTALLED, "".join(missing))
    print(h.MSG_INSTALL)
    i = input()
    if i.lower() == "y":
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing]) #stdout=subprocess.DEVNULL
    else:
        sys.exit()

from PIL import Image

ANDROID_FOLDERS = ["ldpi", "mdpi", "hdpi", "xhdpi", "xxhdpi", "xxxhdpi"]
ANDROID_SCALE = [0.75, 1, 1.5, 2, 3, 4]

def resize_img(imgPath, outputPath, width, height, quality = 100):
    img = Image.open(imgPath)
    ratio = float(img.size[0]) / float(img.size[1])
    wsize = width
    hsize = height
    if width <= 0 and height <= 0:
        print(h.MSG_BAD_ARG_WH)
    if width == 0:
        wsize = int(float(height)*ratio)
    elif height == 0:
        hsize = int(float(width)/ratio)

    img = img.resize((wsize,hsize), Image.ANTIALIAS)
    img.save(outputPath, optimize=True,quality=quality)

def create_ios_img(imgPath, outputFolder, width, height, quality):
    path = ph.get_file_name(imgPath)
    for count in range(1,4):
        out = outputFolder + path[0] + "@" + str(count) + "x" + path[1]
        resize_img(imgPath, out, int(float(width) / 3.0 * count) , int(float(height) / 3.0 * count), quality)

def create_android_img(imgPath, outputFolder, width, height, quality):
    path = ph.get_file_name(imgPath)
    for idx,folder in enumerate(ANDROID_FOLDERS):
        out = outputFolder + folder + "/" + ph.using_android_naming(path[0]) + path[1]
        resize_img(imgPath, out, int(float(width) / 4.0 * ANDROID_SCALE[idx]), int(float(height) / 4.0 * ANDROID_SCALE[idx]), quality)


def run_asset_creation(argv):
    print(h.MSG_RUNNING)
    isFile = isDir = ios = android = False
    img = outputFolder = ""
    size = width = height = 0
    quality = 100
    images = []

    for idx,v in enumerate(argv):
        if v == "-w":
            width = int(argv[idx+1])
        elif v == "-h":
            height = int(argv[idx+1])
        elif v == "-q":
            quality = int(argv[idx+1])
            if quality > 100 or quality < 0:
                print(h.MSG_BAD_ARG_Q, quality)
                return
        elif v == "-o":
            outputFolder = argv[idx+1]
            if not outputFolder.endswith(os.path.sep) and not outputFolder.endswith('.'):
                outputFolder += os.path.sep
            try:
                if not os.path.exists(outputFolder):
                    os.mkdir(outputFolder)
            except OSError:
                print (h.MSG_CREATE_DIR_FAILED, outputFolder)
                return
        elif v.lower() == "-ios":
            ios = True
        elif v.lower() == "-android":
            android = True
        elif idx == len(argv) - 1:
            isFile = os.path.isfile(v)
            isDir = os.path.isdir(v)
            if not isDir and not isFile:
                print(h.MSG_INVALID_FILE+v)
                return
            elif isFile:
                images += v
            elif isDir:
                images += glob.glob(str(v)+"/*.png")
                images += glob.glob(str(v)+"/*.jpg")
                images += glob.glob(str(v)+"/*.jpeg")
                images += glob.glob(str(v)+"/*.JPG")
                images += glob.glob(str(v)+"/*.JPEG")
                images += glob.glob(str(v)+"/*.PNG")
    print("Images: ", " ".join(images))
    print("Output: ", outputFolder)
    if android:
        try:
            for folder in ANDROID_FOLDERS:
                if not os.path.exists(outputFolder + folder):
                    os.mkdir(outputFolder + folder)
        except OSError:
            print (h.MSG_CREATE_ANDROID_DIR_FAILED)
            return
    for img in images:
        if ios:
            create_ios_img(img, outputFolder, width, height, quality)
        if android:
            create_android_img(img, outputFolder, width, height, quality)
    print(h.MSG_FINISHED)


if len(sys.argv) < 2:
    print(h.MSG_HELP_SHORT)
elif sys.argv[1] == "-h" or sys.argv[1] == "--help" :
    print(h.MSG_HELP)
else:
    run_asset_creation(sys.argv[1:])
