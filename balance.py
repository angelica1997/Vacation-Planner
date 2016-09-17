from googleplaces import GooglePlaces, types, lang
import json
import clustering
import urllib
import pprint

def process(clust):
	j = 0
	while (j < len(clust)):
		if (len(clust[j]) < 4):
			YOUR_API_KEY = 'AIzaSyBdND_8stEjVtLh_jZVxODQSwQpzNnFdMU'
			center = min(clust[j], key=lambda t:t[2])
			lat = str(center[0])
			lng = str(center[1])
			google_places = GooglePlaces(YOUR_API_KEY)
			LOCATION = lat+','+lng
			QUERY = 'attraction'
			MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
					 '?location=%s'
					 '&radius=1000'
					 '&key=%s') % (LOCATION, YOUR_API_KEY)

			response = urllib.urlopen(MyUrl)
			jsonRaw = response.read()
			jsonData = json.loads(jsonRaw)
			results = jsonData['results']

			for each in results:
				if(len(clust[j]) > 3):
					break
				place1={}
				geo = each['geometry']['location']
				lat = geo['lat']
				lng = geo['lng']
				place_id = each['place_id']
				icon = each['icon']
				rank = len(clust[j])
				name = each['name']
				if(notcontain(clust,place_id)):
					clust[j].append((lat,lng,rank,place_id,icon,name))

		j += 1
	return clust

def notcontain(l, x):
	for each in l:
		for y in each:
			if (y[3]==x):
				return False
	return True