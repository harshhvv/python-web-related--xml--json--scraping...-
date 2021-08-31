import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    parms = dict()
    parms['key'] = api_key
    parms['address'] = address
    url = serviceurl + urllib.parse.urlencode(parms) #constructing the url with proper query and ecoding it 
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    js = json.loads(data) 
    #print(json.dumps(js, indent=4)) #prints the json prettily with indentation of 4 
    placeid = js['results'][0]['place_id']
    print(placeid)