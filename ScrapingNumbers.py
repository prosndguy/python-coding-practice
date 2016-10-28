import urllib
from BeautifulSoup import *


url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
numlist = list()
for tag in tags:
    # Look at the parts of a tag
    numlist.append(int(tag.contents[0]))
print "Count", str(len(numlist))+"\n"+"Sum", str(sum(numlist))+"..."
