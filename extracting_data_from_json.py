#Michelle Habib Oct 11-2022
import json
import ssl
import urllib.request, urllib.parse, urllib.error

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total = 0
url = input("Enter location:")

uhand = urllib.request.urlopen(url, context=ctx)
data = uhand.read()
info = json.loads(data)

for item in info['comments']:
    total += int(item['count'])

print(total)
