import re

fhand = open('ACTUALregex.txt')
numlist = list()
numtextlist = re.findall('[0-9]+', fhand.read())
for num in numtextlist:
	numint = int(num)
	numlist.append(numint)
print sum(numlist), numtextlist
