import json
import urllib

serviceurl = raw_input('Enter location: ')
if not serviceurl: serviceurl = 'http://python-data.dr-chuck.net/comments_283750.json'

print 'Retrieving', serviceurl
uh = urllib.urlopen(serviceurl)
data = uh.read()

#TODO
#Find sum of comments
'''
js = json.loads(str(data))
comments = js['comments']
summary = 0
for info in comments:
    summary += int(info.get('count'))
    print summary
'''
print sum((info.get('count')) for info in json.loads(str(data))['comments'])
