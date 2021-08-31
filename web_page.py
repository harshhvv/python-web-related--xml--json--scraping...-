#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 17:08:05 2021

@author: harsh
"""

import urllib.error
import urllib.request
import urllib.parse
fhand = urllib.request.urlopen(
    'file://Users/harsh/Desktop/driver_signup/index.html')
for line in fhand:
    print(line.decode().strip())
