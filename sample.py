from googleplaces import GooglePlaces, types, lang
import json
import urllib

location = 'London'
YOUR_API_KEY = 'AIzaSyBV_VtVaZJfy54pQiviMq2ZFllqQokZE3I'

google_places = GooglePlaces('AIzaSyBV_VtVaZJfy54pQiviMq2ZFllqQokZE3I')
MyUrl = ('https://maps.googleapis.com/maps/api/place/textsearch/'
		 'json?query=tourist+attraction+'+location+
		 '&key=AIzaSyBV_VtVaZJfy54pQiviMq2ZFllqQokZE3I')  #grabbing the JSON result
response = urllib.urlopen(MyUrl)
jsonRaw = response.read()
jsonData = json.loads(jsonRaw)
print(type(jsonData))

j = json.dumps(jsonData,sort_keys=True, indent=4)

with open('Tests.json','w') as outf:
	outf.write(j)
