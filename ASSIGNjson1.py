import urllib
import json

url = raw_input('Enter location: ')
print 'Retrieving', url
data = urllib.urlopen(url).read()
print 'Retrieved', len(data), 'characters'
dataParse = json.loads(data)
counts = dataParse['comments']
print 'Count:', len(counts)
total = 0
for item in counts:
    total = total + item['count']
print 'Sum:',total
