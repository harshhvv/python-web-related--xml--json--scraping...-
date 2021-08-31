import urllib.error
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl

# ignore ssl certification errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("enter- ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

'''tags = soup("span")
l = []
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    l.append((tag.contents[0]))
    print('Attrs:', tag.attrs)
print((l))
'''