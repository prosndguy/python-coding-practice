# Use the file name mbox-short.txt as the file name
while True:
    try:
		fname = raw_input("Enter file name: ")
		fh = open(fname)
		count = 0
		total = 0
		avg = 0
		for line in fh:
			if not line.startswith("X-DSPAM-Confidence:"):
				continue
			count = count + 1
			length = len(line)
			startofnum = line.find(':')+1
			total = total + float(line[startofnum:length])
		avg = total/count
		print "Average spam confidence:",avg
    except:
	    print "Invalid file, please try again..."
	    continue
