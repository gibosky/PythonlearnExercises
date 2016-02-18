#10.2 Write a program to read through the mbox-short.txt and figure out the distribution 
#by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and 
#then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, 
#print out the counts, sorted by hour as shown below.

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
dictWeek = dict()
dictHours = dict()

for line in fh:
    if not line.startswith("From ") : 
        continue
    else :
        words = line.split()
        time = words[5].split(':')
        hour = time[0]
        dictHours[hour] = dictHours.get(hour,0) + 1

t = sorted(dictHours.items()) 
print t

for k, v in t: 
    print k,v

#for k, v in sorted(d.items()): 
#    print k, v 
#lst = list()
#for key, val in  dictHours.items(): 
#    lst.append( (key, val) ) 
#lst.sort 

#for key, val in lst:
#    print key, val 

        