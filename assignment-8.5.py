def openFile (fname) : 
	try :
		fh = open(fname)
	except IOError, e:
		print 'File cannot be opened:', fname 
		exit() 
	return fh

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = openFile(fname)
count = 0

for line in fh:
    if not line.startswith("From ") : 
    	continue
    else :
    	words = line.split()
    	email = words[1]
    	print email
    	count = count + 1
print "There were", count, "lines in the file with From as the first word"
