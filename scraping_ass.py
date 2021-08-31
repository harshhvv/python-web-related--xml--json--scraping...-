import urllib.error
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl

url = "http://py4e-data.dr-chuck.net/comments_986835.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
nums = []
for tag in tags:
    #print(tag) #prints the entire tag i.e. from <span>........</span>
    #print(tag.get('class', None)) #prints the value of class attribute present
    #print(tag.contents) #prints the value b/w span and /span
    nums.append(int(tag.contents[0]))
    #print(tag.attrs) #prints all attributes of tag along with its value as key-value pair
print(sum(nums))
