from googleplaces import GooglePlaces, types, lang
import json
import clustering
import urllib
import pprint

def process(clust):
	j = 0
	while (j < len(clust)):
		if (len(clust[j]) < 4):
			YOUR_API_KEY = 'AIzaSyDcivoD8aUEhmSk-yb5GLd1FovUrt8xgpc'
			center = min(clust[j], key=lambda t:t[2])
			lat = str(center[0])
			lng = str(center[1])
			google_places = GooglePlaces(YOUR_API_KEY)
			geo = google_places.nearby_search(
	        		   location=lat+','+lng,radius = 1000, keyword='attraction')

			for c in geo.places:
				if(len(clust[j]) > 3):
					break
				place1={}
				c.get_details()
				lat = c.geo_location['lat']
				lng = c.geo_location['lng']
				place_id = c.place_id
				rank = len(clust[j])
				if(notcontain(clust,place_id)):
					clust[j].append((lat,lng,rank, place_id))

		j += 1

	return clust

def notcontain(l, x):
	for each in l:
		for y in each:
			if (y[3]==x):
				return False
	return True