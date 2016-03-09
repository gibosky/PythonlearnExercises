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

def findFriend(url, count, position, result) :
    html = accessURL(url)
    soup = BeautifulSoup(html)
    tags = soup('a')
    i = 2 
    for tag in tags:
        if position < i :
            break
        i = i + 1
    URL = tag.get('href', None)
    print "URL :", URL
    result = result + tag.contents[0] + " "
    print "result :", result
    count = count - 1
    print "count :", count

    if count < 1: 
        return result
    else :
        return findFriend(URL, count, position, result)

print findFriend("http://python-data.dr-chuck.net/known_by_Karsyn.html ", 7, 18, "Karsyn ")