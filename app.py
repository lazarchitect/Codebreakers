from flask import Flask, request, Response, render_template, session, redirect
import pymysql.cursors
from hashlib import sha256
import os




def get_fields(request):
	return [i.split("=")[1] for i in str(request.get_data())[2:-1].split("&")]

def sha_hash(password):
	"""for use with hashing passwords."""
	h = sha256()
	h.update(password.encode('utf-8'))
	password = h.hexdigest()[:20] # the hash is too long for the varchar(45)
	return password

#this block reads in all data from credentials.txt so the whole server has access to it. Stores the data in 'creds'
with open("credentials.txt", "r") as f:
	contents = f.read()
	contentList = contents.split("\n")
	creds = {}
	for credential in contentList:
		key, value = credential.split("=")
		creds[key] = value

connection = pymysql.connect(host=creds["DB_HOST"], user=creds["DB_USERNAME"], password=creds["DB_PASSWORD"], db=creds["DB_NAME"])

app = Flask(__name__)

#for use with session
app.secret_key = os.urandom(16)

waitingRoom = ""

@app.route("/")
def splash():
	"""main page. Loads up splash screen."""
	print("Session:", session)
	return render_template("splash.html")

@app.route("/signup")
def signupPage():
	return render_template("signup.html")

@app.route("/signupAction", methods=["POST"])
def signupAction():
	
	fields = get_fields(request)

	username = fields[0]
	password = fields[1]
	confirm  = fields[2]
	email    = fields[3]
	
	#check if their confirm was correct (can handle this with JSON on the page itself)
	if(password != confirm):
		print("DEBUG: password and confirm did not match")
		return render_template("/signupfail.html", reason="password and confirmation did not match.")

	#hash the password
	password = sha_hash(password)

	with connection.cursor() as cursor:
		query = "SELECT userid FROM codebreakers.users WHERE username=%s OR email=%s"
		cursor.execute(query, (username, email))
		connection.commit()
		if(cursor.fetchone() == None):
			# if that works...
			query = "INSERT INTO codebreakers.users (username, password, email) VALUES (%s, %s, %s)"
			cursor.execute(query, (username, password, email))
			connection.commit()

			return render_template("/signupsuccess.html", username=username)

		else: #username is taken
			return render_template("/signupfail.html", reason="username or email already in use.")

@app.route("/login")
def loginPage():
	return render_template("login.html")

@app.route("/loginAction", methods=["POST"])
def loginAction():

	if 'username' in session:
		print("user already logged in")
		return redirect("/")

	fields = get_fields(request)
	username = fields[0]
	password = fields[1]

	#hash the password
	print(fields)
	print(password)
	password = sha_hash(password)
	print("hashed:", password)


	with connection.cursor() as cursor:
		print(cursor)
		query = "SELECT email FROM codebreakers.users WHERE username=%s AND password=%s"
		print(query, username, password)
		cursor.execute(query, (username, password))
		# connection.commit()

		result = cursor.fetchone()
		print("login query result:", result)
		
		if(result != None): # note the NOT None
			email = result[0]
			session['username'] = username
			print("Session created upon successful login")
			print("Session:", session)
			return redirect	("/")

		else: # user not found
			return render_template("/loginfail.html", reason="That combination of username and password was not found in our systems.")

@app.route("/logout")
def logout():
	session.pop('username', None)
	return redirect("/")


@app.route("/getWaitingRoom", methods=["POST"])
def getWaitingRoom():
	return waitingRoom

@app.route("/addToWaitingRoom", methods=["POST"])
def addToWaitingRoom():
	global waitingRoom
	waitingRoom += " " + session['username']
	return waitingRoom

@app.route("/gamepage")
def gamepage():
	return render_template("gamepage.html")

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