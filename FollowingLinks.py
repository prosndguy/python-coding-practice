import urllib
from BeautifulSoup import *


url = raw_input('Enter URL: ')
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))


for i in range(count + 1):

    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    print 'Retrieving:', url
    # Retrieve all of the anchor tags
    tags = soup('a')
    name = tags[position - 1].get('href',None)
    url = name
