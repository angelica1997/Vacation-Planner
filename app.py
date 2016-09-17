from flask import Flask

from flask import render_template

app = Flask(__name__)
 
@app.route("/")
def hello():
    return render_template("pics_test.html")


 
@app.route('/signUp')
def signUp():
    return render_template('main.html')

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username'];
    password = request.form['password'];
    return json.dumps({'status':'OK','user':user,'pass':password});
 
if __name__ == "__main__":
    app.run()
