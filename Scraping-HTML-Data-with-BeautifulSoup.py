# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

def accessURL (url) : 
    try :
        html = urllib.urlopen(url).read()
    except IOError, e:
        print 'Site cannot be access:', url
        exit() 
    return html

url = raw_input('Enter - ')
if len(url) < 1 : url = "http://python-data.dr-chuck.net/comments_241377.html"
print len(url)
html = accessURL(url)

soup = BeautifulSoup(html)

count = 0
sumSpans = 0

# Retrieve all of the anchor spans
spans = soup('span')
for span in spans:
    # Look at the parts of a span
    #print 'SPAN:',span
    #print span.get('class', None), '\n'
    #print 'Contents:',span.contents[0]
    #print 'Attrs:',span.attrs
    count = count + 1
    sumSpans = sumSpans + int(span.contents[0]) 
print "Count ", count
print "Sum ", sumSpans