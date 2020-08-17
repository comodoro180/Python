import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
print('Retrieving', address)

uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
results = tree.findall('.//count')
total_comments = 0
count = 0
for item in results:
    # print('Item:', item.text)
    total_comments = total_comments + int(item.text)
    count = count + 1

print('Count:', count)
print('Sum:', total_comments)
