text = "X-DSPAM-Confidence:    0.8475";
length = len(text)
startofnum = text.find(':')+1
print text[0:startofnum]
thenumis = float(text[startofnum:length])
print thenumis
