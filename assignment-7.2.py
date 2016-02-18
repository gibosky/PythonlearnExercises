# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try:
	fh = open(fname)
except IOError, e:
	print 'File cannot be opened:', fname 
	exit() 
count = 0
sum = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
    	continue
    else :
		line = line.strip()
		pos = line.find(':') + 1
		value = float(line[pos:])
		count = count + 1
		sum = sum + value
print sum/count
