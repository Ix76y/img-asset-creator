#!/usr/bin/python

import sys


#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

MSG_HELP_SHORT = """
Usage: python imgasset.py [options]... img|imgFolder

Try --help for more help.
"""

MSG_HELP = """imgasset - Image Asset Creator for Android and iOS\n
Usage: python imgasset.py [options]... img|imgFolder

- [ Options ] -

Options Short / Long           | Type | Description                                          | Example
================================+======+======================================================+============================
-h, --help                     |      | Print help                                           |
-iOS                           |      | Using iOS naming convetions                          | Out: <img>@3x.jpg, <img>@2x..
-android                       |      | Using Android naming convetions                      | Out: <img_name>.jpg
-o                             | STR  | Output Folder                                        | -o ~/Desktop
-w                             | NUM  | Define Width in px for highest quality               | -w 300
-y                             | NUM  | Define Height in px for highest quality              | -y 300
-q                             | NUM  | Setting the quality of the image in percent          | -q 85

Example Usage: python imgasset.py -iOS myImage.jpg
"""

MSG_RUNNING = 'Running Asset Creation...'

MSG_NOT_INSTALLED = "The following package(s) are currently not installed: "
MSG_INSTALL = "Do you want to install them with pip? [y/n]"
MSG_CREATE_DIR_FAILED = "Creation of the directory failed: "
MSG_CREATE_ANDROID_DIR_FAILED = "Creation of android directories failed."
MSG_BAD_ARG_WH = "Bad Arguments passed for width and or height..."
MSG_BAR_ARG_Q = "Invalid Parameter: Quality value should be between [0,100] but is "
MSG_INVALID_FILE = 'Invalid input file or directory '
MSG_FINISHED = 'Finished creating assets!'
