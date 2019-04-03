from flask import Flask, request, Response, render_template

app = Flask(__name__)

@app.route("/")
def splash():
	"""main page. Loads up splash screen."""
	return render_template("splash.html")

@app.route("/gamepage")
def gamepage():
	"""The webpage for being in a game. Loads up game HTML elements.
	Should be unable to reach here manually."""
	return render_template("gamepage.html")

@app.route("/piledrop", methods=["POST"])
def piledrop():
	"""handler for placing a card on a pile.
	called with AJAX from game page. cannot manually get here."""
	color = request.get_data().decode("utf-8")

	resp = Response("Hello from localhost 5k! You dragged a card to the " + color + " pile!");

	resp.headers['Access-Control-Allow-Origin'] = '*'
	
	return resp

app.run()	