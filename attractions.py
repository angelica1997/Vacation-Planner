
from googleplaces import GooglePlaces, types, lang
import json
import urllib

def attraction_list():

	YOUR_API_KEY = 'AIzaSyBwNcWLEs2CtcXgjur6nbR8JwGsiK-0HGw'

	google_places = GooglePlaces(YOUR_API_KEY)

	LOCATION = app.send_location()
	QUERY = 'attraction'
	MyUrl = ('https://maps.googleapis.com/maps/api/place/textsearch/json'
		'?query=tourist+attraction+%s'
		'&key=%s') % (LOCATION, YOUR_API_KEY)
           #grabbing the JSON result
	response = urllib.urlopen(MyUrl)

	jsonRaw = response.read()
	jsonData = json.loads(jsonRaw)

	print jsonData

	results = jsonData['results']

	dic = []

	i = 0
	for each in results:
		name = each['name']
		place_id = each['place_id']
		icon = each['icon']
		geo = each['geometry']
		lat = geo['location']['lat']
		lng = geo['location']['lng']
		rank = i
		dic.append((lat,lng,rank,place_id,icon,name))
		i += 1

	print dic

	j = json.dumps(dic,sort_keys=True, indent=4)

	with open('Tests.json','w') as outf:
		outf.write(j)

	return j

#hello()
