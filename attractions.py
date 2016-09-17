
from googleplaces import GooglePlaces, types, lang
import json
import urllib


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	YOUR_API_KEY = 'AIzaSyBV_VtVaZJfy54pQiviMq2ZFllqQokZE3I'

	google_places = GooglePlaces(YOUR_API_KEY)

	query_result = google_places.nearby_search(
	        location='New+York, America',keyword='attraction')

	res = query_result.raw_response

	dic = []
	i = 0
	for place in query_result.places:
	    # Returned places from a query are place summaries.
	    place1={}
	    place.get_details()
	    place1['name'] = place.name
	    place1['website'] = place.website
	    place1['place_id'] = place.place_id
	    place1['rank'] = i
	    #loc = place.geo_location
	    #lat = loc['lat']
	    #lng = loc['lng']
	    #print lat
	    dic.append(place1)
	    i+=1

	j = json.dumps(dic,sort_keys=True, indent=4)

	with open('Tests.json','w') as outf:
		outf.write(j)
		
	return j

if __name__ == "__main__":
    app.run()
