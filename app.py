from flask import Flask

from flask import render_template, request, jsonify

app = Flask(__name__)

@app.route('/_send_location')
def send_location():
    loc = request.args.get('loc', 0, type=str)
    return jsonify(result=loc)
 
@app.route("/")
def index():
    return render_template("index.html")
 
if __name__ == "__main__":
    app.run(debug=True)
