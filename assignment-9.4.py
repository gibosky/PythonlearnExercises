# 9.4 Write a program to read through the mbox-short.txt and 
# figure out who has the sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as 
# the person who sent the mail. 
# The program creates a Python dictionary that maps 
# the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using 
# a maximum loop to find the most prolific committer.

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

dictGreatestNumberSentEmail = dict()
valueCountGreatest = None

for line in fh:
    if not line.startswith("From ") : 
    	continue
    else :
    	words = line.split()
    	email = words[1]
    	dictGreatestNumberSentEmail[email] = dictGreatestNumberSentEmail.get(email,0) + 1
    	if valueCountGreatest < dictGreatestNumberSentEmail[email] :
    		valueCountGreatest = dictGreatestNumberSentEmail[email]
    		emailCountGreatest = email
print emailCountGreatest, valueCountGreatest




