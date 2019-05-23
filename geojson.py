import urllib
import json
import sys

#serviceurl = 'http://python-data.dr-chuck.net/geojson?'
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

address = raw_input('Enter location: ')
if len(address) < 1 : sys.exit("Wrong location")

url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
print data

try: js = json.loads(str(data))
except: js = None
if 'status' not in js or js['status'] != 'OK':
    sys.exit("Failure To Retrieve")
#place_id = js["results"][0]["place_id"]
#print 'Place id',place_id
    
    #TODO
    #Return lat,lng,adress
lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]
print 'lat',lat,'lng',lng
location = js['results'][0]['formatted_address']
print location
