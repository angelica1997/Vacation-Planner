from googleplaces import GooglePlaces, types, lang
import json
import clustering
import urllib
import pprint

def search():
	days = 5
	with open('Tests.json') as data:
		places = json.load(data)

	#print places
	YOUR_API_KEY = 'AIzaSyDcivoD8aUEhmSk-yb5GLd1FovUrt8xgpc'

	google_places = GooglePlaces(YOUR_API_KEY)

	location = []
	
	for each in places :
		response = urllib.urlopen('https://maps.googleapis.com/maps/api/place/details/json?'
		'placeid='+each['place_id']+'&key='+YOUR_API_KEY)
		raw = response.read()
		geo = json.loads(raw)
		lat = geo['result']['geometry']['location']['lat']
		lng = geo['result']['geometry']['location']['lng'] 
		location.append((lat,lng,each['rank'],each['place_id']))
		#print(each)

	API_KEY = 'AIzaSyBV_VtVaZJfy54pQiviMq2ZFllqQokZE3I'
	#print(location)
	clus = clustering.kmeans(location,days,[])
	print(clus)

	#google_places = GooglePlaces(API_KEY)
	
	#MyUrl = ('https://maps.googleapis.com/maps/api/distancematrix/'
	#		 'json?origins=place_id:'+placeid1+
	#		 '&kdestinations=place_id:'+placeid2)

search()