class Session:
	"""representing the attributes of a logged in user. 
	THERE CAN ONLY BE ONE.
	If there is multiple sessions, we have a problem.
	If there is zero sessions, then no one should be logged in. """

	def __init__(self, username, email):
		self.username = username
		self.email = email