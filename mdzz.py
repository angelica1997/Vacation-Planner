from googleplaces import GooglePlaces, types, lang
import json
import clustering
import urllib
import pprint
import balance

def search():
	days = 5
	with open('Tests.json') as data:
		places = json.load(data)

	#print places

		#print(each)

	#print(location)
	clus = clustering.kmeans(places,days,[])

	processed = balance.process(clus)

	j = json.dumps(processed,sort_keys=True, indent=4)

	with open('Results.json','w') as outf:
		outf.write(j)

	#google_places = GooglePlaces(API_KEY)
	
	#MyUrl = ('https://maps.googleapis.com/maps/api/distancematrix/'
	#		 'json?origins=place_id:'+placeid1+
	#		 '&kdestinations=place_id:'+placeid2)

search()