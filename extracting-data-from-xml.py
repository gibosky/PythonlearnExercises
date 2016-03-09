import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_241374.xml'
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
#print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
print 'Results:', len(results)
count = 0
sumValue = 0
for item in results :
    #print item.find('count').text
    count = count + 1
    sumValue = sumValue + int(item.find('count').text)
print "Count", count
print "Sum", sumValue