#__author = vkremez
# This programming challenge was written for University of Michigan's programming challenge using Google geocode API.
# The purpose of this program is to retrieve specific latitude and longitude information about any geographical location.

import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print('Retrieved',len(data),'characters')

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print json.dumps(js, indent=4)

    placeid = js["results"][0]["place_id"]

    print("Place id: ", placeid)
