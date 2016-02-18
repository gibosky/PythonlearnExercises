import re

def openFile (fname) : 
    try :
        fh = open(fname)
    except IOError, e:
        print 'File cannot be opened:', fname 
        exit() 
    return fh

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum_241372.txt"

fh = openFile(fname)
sumTotal = 0

for line in fh:
	listStrNumbers = re.findall('[0-9]+',line)
	if len(listStrNumbers) > 0 : 
		listNumbers = map(int, listStrNumbers)
		sumTotal = sumTotal + sum(listNumbers)
print sumTotal