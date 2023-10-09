import urllib.request, urllib.parse, urllib.error
import json

api_key = ''

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter a location: ')
    if len(address) < 1: break

    params = {
        'address' : address,
        'key' : api_key 
    }

# Gives a dictionary of addresses. String for the end of the url. 
    url = serviceurl + urllib.parse.urlencode(params)

# Goes to the url nad retrieves the info from it
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failure to Retrieve ===')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

