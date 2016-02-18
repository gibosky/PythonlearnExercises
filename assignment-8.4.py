def openFile (fname) : 
	try :
		fh = open(fname)
	except IOError, e:
		print 'File cannot be opened:', fname 
		exit() 
	return fh

fname = raw_input("Enter file name: ")
fh = openFile(fname)

lstAll = list()
lstLine = list()

for line in fh :
	lstLine = line.split()
	for word in lstLine :
		if word not in lstAll :
			lstAll.append(word)
lstAll.sort()
print lstAll
#print line.rstrip()
