import urllib.error
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ok

url = 'http://py4e-data.dr-chuck.net/comments_986837.xml'
output = urllib.request.urlopen(url).read()
tree = ok.fromstring(output)


l=[]
for comments in tree.findall('comments'):
    #print(comments)
    for comment in comments.findall('comment'):
        #print(comment)
        l.append(int(comment.find('count').text))

print(sum(l))
