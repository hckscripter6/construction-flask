from config import db

class Projects(db.Model):
	id =  db.Column(db.Integer, primary_key=True)
	filename = db.Column(db.String(300))
	project = db.Column(db.String(300))
	tag = db.Column(db.String(25))
	
	def __init__(self, filename, project, tag):
		self.filename = filename
		self.project = project  
		self.tag = tag