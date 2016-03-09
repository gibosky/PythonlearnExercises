import re

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox2.txt'
fh = open(fname)
count = 0
for line in fh:
    if not re.search('From:', line) : continue
    pieces = line.split()
    org =  re.findall('@([^ ]*)',pieces[1])
    org = "'" + org[0] +"'"
    print org
    count = count +1
print "count", count



#org =  re.findall('@([^ ]*)',pieces[1])
#    org = "'" + org[0] +"'"
