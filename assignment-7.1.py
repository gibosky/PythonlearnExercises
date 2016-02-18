# Use words.txt as the file name
fname = raw_input("Enter file name: ")
try:
	fh = open(fname)
except IOError, e:
	print 'File cannot be opened:', fname 
	exit() 

for line in fh :
	line = line.rstrip().upper()
	print line