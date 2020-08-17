import json
import ssl
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
print('Retrieving', address)

uh = urllib.request.urlopen(address, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)
# print(json.dumps(js, indent=4))
comments = js['comments']
print('Count:', len(comments))

total_comments = 0
for comment in comments:
    total_comments = total_comments + comment['count']

print('Sum:', total_comments)
