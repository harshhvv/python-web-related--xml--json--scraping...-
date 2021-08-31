import ssl
import urllib.request, urllib.error, urllib.parse
import json

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"
while True:
    address = input("enter: ")
    if len(address)<1:
        break
    url = serviceurl+ urllib.parse.urlencode({'address':address})
    print('retrieveing', url)
    x = urllib.request.urlopen(url)
    data = x.read().decode()
    print(data)