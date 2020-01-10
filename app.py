from flask import Flask, request, Response, render_template
import pymysql.cursors

connection = pymysql.connect(host="CREDS.TXT", user="CREDENTIALS.TXT", password="READ IN FROM CREDENTIALS.TXT", db="codebreakers")

app = Flask(__name__)

@app.route("/")
def splash():
	"""main page. Loads up splash screen."""
	return render_template("splash.html")

@app.route("/signup")
def signupPage():
	return render_template("signup.html")

@app.route("/signupAction", methods=["POST"])
def signupAction():
	
	fields = [i.split("=")[1] for i in str(request.get_data())[2:-1].split("&")]
	#trust me, it works.

	username = fields[0]
	password = fields[1]
	confirm  = fields[2]
	
	print(username)
	print(password)
	print(confirm)

	with connection.cursor as cursor:
		query = "GET x rows where username =", username
		cursor.execute(query, (values, separated, by, commas))
		connection.commit()

		# if that works...
		query = "INSERT row where username =", username
		cursor.execute(query, (values, separated, by, commas))
		connection.commit()

		return redirect("/signupsuccess")

@app.route("/login")
def loginPage():
	return render_template("login.html")

@app.route("/loginAction", methods=["POST"])
def loginAction():
	print(request.get_data())

# @app.route("/gamepage")
# def gamepage():
# 	"""The webpage for being in a game. Loads up game HTML elements.
# 	Should be unable to reach here manually."""
# 	return render_template("gamepage.html")

# @app.route("/piledrop", methods=["POST"])
# def piledrop():
# 	"""handler for placing a card on a pile.
# 	called with AJAX from game page. cannot manually get here."""
# 	color = request.get_data().decode("utf-8")

# 	resp = Response("Hello from localhost 5k! You dragged a card to the " + color + " pile!");

# 	resp.headers['Access-Control-Allow-Origin'] = '*'
	
# 	return resp

app.run()