from flask import Flask, request, Response, render_template
import pymysql.cursors
from hashlib import sha256

with open("credentials.txt", "r") as f:
	contents = f.read()
	contentList = contents.split("\n")
	creds = {}
	for credential in contentList:
		key, value = credential.split("=")
		creds[key] = value

connection = pymysql.connect(host=creds["DB_HOST"], user=creds["DB_USERNAME"], password=creds["DB_PASSWORD"], db=creds["DB_NAME"])

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
	email    = fields[3]
	
	#check if their confirm was correct (can handle this with JSON on the page itself)
	if(password != confirm):
		print("DEBUG: password and confirm did not match")
		return render_template("/signupfail.html", reason="password and confirmation did not match.")

	#hash the password
	h = sha256()
	h.update(password.encode('utf-8'))
	password = h.hexdigest()[:20] # the hash is too long!

	with connection.cursor() as cursor:
		query = "SELECT userid FROM codebreakers.users WHERE username=%s"
		cursor.execute(query, (username))
		connection.commit()
		if(cursor.fetchone() == None):
			# if that works...
			query = "INSERT INTO codebreakers.users (username, password, email) VALUES (%s, %s, %s)"
			cursor.execute(query, (username, password, email))
			connection.commit()

			return render_template("/signupsuccess.html", username=username)

		else: #username is taken
			return render_template("/signupfail.html", reason="username already in use.")

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



@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500

app.run()