import urllib
import json
from bs4 import BeautifulSoup


url = raw_input('Enter URL: ')




html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
print 'Retrieving:', url
# Retrieve all of the anchor tags
tagDict = dict()
tags = soup.find_all(True)
for tag in tags:
    try:
        tagDict[tag.name] = tagDict.get(tag.name,0)+1
    except:
        print 'bad tag'
print json.dumps(tagDict, sort_keys=True, indent=4)
print 'Number of distinct tags:', len(tagDict)
