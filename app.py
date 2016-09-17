from flask import Flask
from flask import render_template, request, jsonify

from googleplaces import GooglePlaces, types, lang
import json
import urllib

app = Flask(__name__)

@app.route('/_get_location')
def get_location():
    loc = request.args.get('loc', 0, type=str)
    return loc

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/_send_location")
def send_location():

	YOUR_API_KEY = 'AIzaSyBdND_8stEjVtLh_jZVxODQSwQpzNnFdMU'

	google_places = GooglePlaces(YOUR_API_KEY)

	LOCATION = get_location()
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
	j = json.dumps(dic,sort_keys=True, indent=4)
	#with open('Tests.json','w') as outf:
	#	outf.write(j)
    print j
	return j




if __name__ == "__main__":
    app.run(debug=True)
