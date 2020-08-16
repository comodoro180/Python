# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import ssl
import urllib.error
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup


def deep_link(link, position, count, count_out=0):
    print('Retrieving:', link, count_out)
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    iteration = 1
    for tag in tags:
        if iteration == position and count > count_out:
            deep_link(tag.get('href', None), position, count, count_out+1)
        iteration = iteration + 1


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
count = input('count:')
position = input('position:')

count = int(count)
position = int(position)

deep_link(url, position, count)
