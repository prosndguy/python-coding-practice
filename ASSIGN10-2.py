#Write a program to read through the mbox-short.txt and figure out who
#has the sent the greatest number of mail messages. The program looks for
#'From ' lines and takes the second word of those lines as the person who
#sent the mail. The program creates a Python dictionary that maps the
#sender's mail address to a count of the number of times they appear in
#the file. After the dictionary is produced, the program reads through
#the dictionary using a maximum loop to find the most prolific committer.


name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
#name = "mbox-short.txt"
handle = open(name)
email_time = dict()
for line in handle:
	if 'From ' not in line: continue
	words = line.split()
	times = words[5].split(':')
	email_time[times[0]] = email_time.get(times[0],0)+1
for hour, num in sorted(email_time.items()):
	print hour, num
