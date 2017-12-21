from config import db

class Project(db.Model):
	id =  db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	tag = db.Column(db.String(100))
	images = db.relationship('Image', backref="project", passive_deletes=True, lazy='dynamic')
	
class Image(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='CASCADE'))
	
