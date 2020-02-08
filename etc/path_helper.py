#!/usr/bin/env python3

import os

def get_file_name(orgPath):
    return os.path.splitext(os.path.split(orgPath)[1])

def using_android_naming(str):
    return str.lower().replace(" ", "_")
