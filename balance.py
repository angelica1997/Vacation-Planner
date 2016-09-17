from googleplaces import GooglePlaces, types, lang
import json
import clustering
import urllib
import pprint

def process(clust):
	for c in clust:
		while(len(c) < 4):
			YOUR_API_KEY = 'AIzaSyDcivoD8aUEhmSk-yb5GLd1FovUrt8xgpc'
			google_places = GooglePlaces(YOUR_API_KEY)
			response = google_places.nearby_search(
	        		   location='New+York, America',keyword='attraction')