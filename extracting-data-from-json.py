import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/comments_241378.json'


url = serviceurl
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data

info = json.loads(data)

count = 0
sumValue = 0

for item in info["comments"]:
    count = count + 1
    sumValue = sumValue + int(item['count'])

print "Count", count
print "Sum", sumValue
  
