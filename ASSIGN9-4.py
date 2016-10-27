#Write a program to read through the mbox-short.txt and figure out who
#has the sent the greatest number of mail messages. The program looks for
#'From ' lines and takes the second word of those lines as the person who
#sent the mail. The program creates a Python dictionary that maps the
#sender's mail address to a count of the number of times they appear in
#the file. After the dictionary is produced, the program reads through
#the dictionary using a maximum loop to find the most prolific committer.


name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emailers = dict()
for line in handle:
	if 'From ' not in line: continue
	words = line.split()
	emailers[words[1]] = emailers.get(words[1],0)+1
most_emails = None
big_sender = None
if emailers != {}:
	for address, count in emailers.items():
		if most_emails is None or most_emails < count:
			most_emails = count
			big_sender = address
print big_sender, most_emails
		