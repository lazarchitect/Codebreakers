from flask import Flask, request, Response, render_template


app = Flask(__name__)

@app.route("/")
def splash():
	return render_template("splash.html")

@app.route("/gamepage")
def gamepage():
	return render_template("gamepage.html")

@app.route("/piledrop", methods=["POST"])
def piledrop():

	color = request.get_data().decode("utf-8")

	resp = Response("Hello from localhost 5k! You dragged a card to the " + color + " pile!");

	resp.headers['Access-Control-Allow-Origin'] = '*'
	
	return resp