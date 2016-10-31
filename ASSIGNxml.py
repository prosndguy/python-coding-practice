import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
print 'Retrieving', url
data = urllib.urlopen(url).read()
print 'Retrieved', len(data), 'characters'
dataParse = ET.fromstring(data)
counts = dataParse.findall('.//count')
print 'Count:', len(counts)
total = 0
for item in counts:
    total = total + int(item.text)
print 'Sum:',total
