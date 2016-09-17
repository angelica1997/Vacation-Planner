from googleplaces import GooglePlaces, tyoes, lang
import json

def search():
	days = 5
	with open('Test.json') as data:
		places = json.load(data)

	location = []
	for place in places :
		place1={}
    	place1['place_id'] = place['place_id']
    	geo = GeoDataApi.getPlaceById(place["place_id"])
    	place1['loc'] = (geo['lat'], geo['lng'])
    	location.append(place1['loc'])


	API_KEY = 'AIzaSyBV_VtVaZJfy54pQiviMq2ZFllqQokZE3I'

	google_places = GooglePlaces(API_KEY)
	
	MyUrl = ('https://maps.googleapis.com/maps/api/distancematrix/'
			 'json?origins=place_id:'+placeid1+
			 '&kdestinations=place_id:'+placeid2)