
import xml.etree.ElementTree as ok
data= '''
<person> 
<name>hi</name>
<phone type = "intl"> +1 74756373 </phone>
<email hide "yes"></email> 
</person>'''
tree = ok.fromstring(data)
print("Name: ", tree.find('name').text)
print("Attr: ", tree.find('email').get('hide'))
