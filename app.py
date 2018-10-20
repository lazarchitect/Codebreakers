from flask import Flask, request, Response


app = Flask(__name__)

@app.route("/colorprinter", methods=["POST"])
def colorprinter():

	color = request.get_data().decode("utf-8")
	
	print(color)

	resp = Response("Hello from localhost 5k! You dragged a card to the " + color + " pile!");

	resp.headers['Access-Control-Allow-Origin'] = '*'
	
	return resp