#Michelle Habib Oct-11-2022
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total = 0
url = input("Enter location: ")

uhand = urllib.request.urlopen(url, context=ctx)
data = uhand.read()
tree = ET.fromstring(data)

for comments in tree.findall('comments/comment'):
     total += int((comments.find('count').text))

print(total)
