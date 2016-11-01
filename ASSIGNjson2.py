import urllib
import json

service = 'http://python-data.dr-chuck.net/geojson?'
#address = 'South Federal University'
address = raw_input('Enter location: ')
url = service + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url
data = urllib.urlopen(url).read()
print 'Retrieved', len(data), 'characters'
dataParse = json.loads(data)
#print json.dumps(dataParse, indent=4)
print 'Place id', dataParse['results'][0]['place_id']
