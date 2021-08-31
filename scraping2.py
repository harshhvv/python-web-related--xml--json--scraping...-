#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 23:48:10 2021

@author: harsh
"""

import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
url = "http://www.dr-chuck.com/page2.htm)"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
#get all anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))