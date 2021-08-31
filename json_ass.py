import urllib.request, urllib.error, urllib.parse
import json
#import ssl
#url = http://py4e-data.dr-chuck.net/comments_986838.json
l = []
url = input('enter url:')
x = urllib.request.urlopen(url)
data = x.read().decode()
info = json.loads(data)
for comment in info['comments']:
    l.append(comment['count'])
print(sum(l))