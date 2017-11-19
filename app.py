from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms import SubmitField, FileField, StringField, PasswordField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug import secure_filename
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123qweasdzxc!@#@localhost/briney'
app.config['SECRET_KEY'] = 'jfeiios;alsei*#@@!fdkj;sa'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(30), unique=True)
	
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/images/uploads'
configure_uploads(app, photos)

class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	remember = BooleanField('remember me')

class ConcreteForm(FlaskForm):
	concrete = FileField('concrete')
	submit = SubmitField()
	
class DeckForm(FlaskForm):
	decks = FileField('decks')
	submit = SubmitField()
	
class GarageForm(FlaskForm):
	garages = FileField('garages')
	submit = SubmitField()	
	
class BasementForm(FlaskForm):
	basement = FileField('basement')
	submit = SubmitField()	
	
class BathroomForm(FlaskForm):
	bathroom = FileField('bathroom')
	submit = SubmitField()	
	
class TileForm(FlaskForm):
	tile = FileField('tile')
	submit = SubmitField()
	
class WallForm(FlaskForm):
	walls = FileField('walls')
	submit = SubmitField()
	
class OfficeForm(FlaskForm):
	office = FileField('office')
	submit = SubmitField()
	
class FencingForm(FlaskForm):
	fencing = FileField('fencing')
	submit = SubmitField()

class HandicapForm(FlaskForm):
	handicap = FileField('handicap')
	submit = SubmitField()
	
class SidingForm(FlaskForm):
	siding = FileField('siding')
	submit = SubmitField()
	
class IslandForm(FlaskForm):
	island = FileField('island')
	submit = SubmitField()
	
class FlooringForm(FlaskForm):
	flooring = FileField('flooring')
	submit = SubmitField()
	
class StairsForm(FlaskForm):
	stairs = FileField('stairs')
	submit = SubmitField()

class RailingForm(FlaskForm):
	railing = FileField('railing')
	submit = SubmitField()
	
class VanityForm(FlaskForm):
	vanity = FileField('vanity')
	submit = SubmitField()

class FireplaceForm(FlaskForm):
	fireplace = FileField('fireplace')
	submit = SubmitField()
	
class PlayhouseForm(FlaskForm):
	playhouse = FileField('playhouse')
	submit = SubmitField()
	
class BunkbedForm(FlaskForm):
	bunkbeds = FileField('bunkbeds')
	submit = SubmitField()
	
class PantryForm(FlaskForm):
	pantry = FileField('pantry')
	submit = SubmitField()

class StairForm(FlaskForm):
	stair = FileField('stair')
	submit = SubmitField()
	
class EgressForm(FlaskForm):
	egress = FileField('egress')
	submit = SubmitField()
	
class KitchenForm(FlaskForm):
	kitchen = FileField('kitchen')
	submit = SubmitField()
	
class WindowForm(FlaskForm):
	window = FileField('window')
	submit = SubmitField()
	
class RoofForm(FlaskForm):
	roof = FileField('roof')
	submit = SubmitField()
	
class Projects(db.Model):
	id =  db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(300))
	project_id = db.Column(db.Integer())
	
	def __init__(self, name, project_id):
		self.name = name
		self.project_id = project_id

index = False

@app.route('/')
def index():
	return render_template('index.html', index=True)
	
@app.route('/resume')
def resume():
	return render_template('resume.html')
	
@app.route('/testimonials')
def testimonials():
	return render_template('testimonials.html')

@app.route('/projects', methods=["GET", "POST"])
def projects():
	concrete = Projects.query.filter_by(project_id=1)
	decks = Projects.query.filter_by(project_id=2)
	garages = Projects.query.filter_by(project_id=3)
	basement = Projects.query.filter_by(project_id=4)
	bathroom = Projects.query.filter_by(project_id=5)
	tile = Projects.query.filter_by(project_id=6)
	walls = Projects.query.filter_by(project_id=7)
	office = Projects.query.filter_by(project_id=8)
	fencing = Projects.query.filter_by(project_id=9)
	handicap = Projects.query.filter_by(project_id=10)
	siding = Projects.query.filter_by(project_id=11)
	island = Projects.query.filter_by(project_id=12)
	flooring = Projects.query.filter_by(project_id=13)
	stairs = Projects.query.filter_by(project_id=14)
	railing = Projects.query.filter_by(project_id=15)
	vanity = Projects.query.filter_by(project_id=16)
	fireplace = Projects.query.filter_by(project_id=17)
	playhouse = Projects.query.filter_by(project_id=18)
	bunkbeds = Projects.query.filter_by(project_id=19)
	pantry = Projects.query.filter_by(project_id=20)
	stair = Projects.query.filter_by(project_id=21)
	egress = Projects.query.filter_by(project_id=22)
	kitchen = Projects.query.filter_by(project_id=23)
	window = Projects.query.filter_by(project_id=24)
	roof = Projects.query.filter_by(project_id=25)
	return render_template('projects.html', concrete=concrete, decks=decks, garages=garages, basement=basement, bathroom=bathroom, tile=tile, walls=walls, office=office, fencing=fencing, handicap=handicap, siding=siding, island=island, flooring=flooring, stairs=stairs, railing=railing, vanity=vanity, fireplace=fireplace, playhouse= playhouse, bunkbeds=bunkbeds, pantry=pantry, stair=stair, egress=egress, kitchen=kitchen, window=window, roof=roof)
	
@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
	return render_template('admin/dashboard.html')
	
@app.route('/dashboard/projects', methods=['GET', 'POST'])
def admin_projects():
	concrete = ConcreteForm()
	if concrete.validate_on_submit() and 'concrete' in request.files:
	#upload to folder
		filename = photos.save(request.files['concrete'])
	#upload to database
		file = request.files['concrete']
		newFile = Projects(name=file.filename, project_id=1)
		db.session.add(newFile)
		db.session.commit()
		
	decks = DeckForm()
	if decks.validate_on_submit() and 'decks' in request.files:
	#upload to folder
		filename = photos.save(request.files['decks'])
	#upload to database
		file = request.files['decks']
		newFile = Projects(name=file.filename, project_id=2)
		db.session.add(newFile)
		db.session.commit()	
		
	garages = GarageForm()
	if garages.validate_on_submit() and 'garages' in request.files:
	#upload to folder
		filename = photos.save(request.files['garages'])
	#upload to database
		file = request.files['garages']
		newFile = Projects(name=file.filename, project_id=3)
		db.session.add(newFile)
		db.session.commit()	
		
	basement = BasementForm()
	if basement.validate_on_submit() and 'basement' in request.files:
	#upload to folder
		filename = photos.save(request.files['basement'])
	#upload to database
		file = request.files['basement']
		newFile = Projects(name=file.filename, project_id=4)
		db.session.add(newFile)
		db.session.commit()	
		
	bathroom = BathroomForm()
	if bathroom.validate_on_submit() and 'bathroom' in request.files:
	#upload to folder
		filename = photos.save(request.files['bathroom'])
	#upload to database
		file = request.files['bathroom']
		newFile = Projects(name=file.filename, project_id=5)
		db.session.add(newFile)
		db.session.commit()
		
	tile = TileForm()
	if tile.validate_on_submit() and 'tile' in request.files:
	#upload to folder
		filename = photos.save(request.files['tile'])
	#upload to database
		file = request.files['tile']
		newFile = Projects(name=file.filename, project_id=6)
		db.session.add(newFile)
		db.session.commit()
		
	walls = WallForm()
	if walls.validate_on_submit() and 'walls' in request.files:
	#upload to folder
		filename = photos.save(request.files['walls'])
	#upload to database
		file = request.files['walls']
		newFile = Projects(name=file.filename, project_id=7)
		db.session.add(newFile)
		db.session.commit()
		
	office = OfficeForm()
	if office.validate_on_submit() and 'office' in request.files:
	#upload to folder
		filename = photos.save(request.files['office'])
	#upload to database
		file = request.files['office']
		newFile = Projects(name=file.filename, project_id=8)
		db.session.add(newFile)
		db.session.commit()
		
	fencing = FencingForm()
	if fencing.validate_on_submit() and 'fencing' in request.files:
	#upload to folder
		filename = photos.save(request.files['fencing'])
	#upload to database
		file = request.files['fencing']
		newFile = Projects(name=file.filename, project_id=9)
		db.session.add(newFile)
		db.session.commit()
		
	handicap = HandicapForm()
	if handicap.validate_on_submit() and 'handicap' in request.files:
	#upload to folder
		filename = photos.save(request.files['handicap'])
	#upload to database
		file = request.files['handicap']
		newFile = Projects(name=file.filename, project_id=10)
		db.session.add(newFile)
		db.session.commit()
		
	siding = SidingForm()
	if siding.validate_on_submit() and 'siding' in request.files:
	#upload to folder
		filename = photos.save(request.files['siding'])
	#upload to database
		file = request.files['siding']
		newFile = Projects(name=file.filename, project_id=11)
		db.session.add(newFile)
		db.session.commit()
		
	island = IslandForm()
	if island.validate_on_submit() and 'island' in request.files:
	#upload to folder
		filename = photos.save(request.files['island'])
	#upload to database
		file = request.files['island']
		newFile = Projects(name=file.filename, project_id=12)
		db.session.add(newFile)
		db.session.commit()
		
	flooring = FlooringForm()
	if flooring.validate_on_submit() and 'flooring' in request.files:
	#upload to folder
		filename = photos.save(request.files['flooring'])
	#upload to database
		file = request.files['flooring']
		newFile = Projects(name=file.filename, project_id=13)
		db.session.add(newFile)
		db.session.commit()
		
	stairs = StairsForm()
	if stairs.validate_on_submit() and 'stairs' in request.files:
	#upload to folder
		filename = photos.save(request.files['stairs'])
	#upload to database
		file = request.files['stairs']
		newFile = Projects(name=file.filename, project_id=14)
		db.session.add(newFile)
		db.session.commit()
		
	railing = RailingForm()
	if railing.validate_on_submit() and 'railing' in request.files:
	#upload to folder
		filename = photos.save(request.files['railing'])
	#upload to database
		file = request.files['railing']
		newFile = Projects(name=file.filename, project_id=15)
		db.session.add(newFile)
		db.session.commit()
		
	vanity = VanityForm()
	if vanity.validate_on_submit() and 'vanity' in request.files:
	#upload to folder
		filename = photos.save(request.files['vanity'])
	#upload to database
		file = request.files['vanity']
		newFile = Projects(name=file.filename, project_id=16)
		db.session.add(newFile)
		db.session.commit()
		
	fireplace = FireplaceForm()
	if fireplace.validate_on_submit() and 'fireplace' in request.files:
	#upload to folder
		filename = photos.save(request.files['fireplace'])
	#upload to database
		file = request.files['fireplace']
		newFile = Projects(name=file.filename, project_id=17)
		db.session.add(newFile)
		db.session.commit()
		
	playhouse = PlayhouseForm()
	if fireplace.validate_on_submit() and 'playhouse' in request.files:
	#upload to folder
		filename = photos.save(request.files['playhouse'])
	#upload to database
		file = request.files['playhouse']
		newFile = Projects(name=file.filename, project_id=18)
		db.session.add(newFile)
		db.session.commit()
		
	bunkbeds = BunkbedForm()
	if bunkbeds.validate_on_submit() and 'bunkbeds' in request.files:
	#upload to folder
		filename = photos.save(request.files['bunkbeds'])
	#upload to database
		file = request.files['bunkbeds']
		newFile = Projects(name=file.filename, project_id=19)
		db.session.add(newFile)
		db.session.commit()
		
	pantry = PantryForm()
	if pantry.validate_on_submit() and 'pantry' in request.files:
	#upload to folder
		filename = photos.save(request.files['pantry'])
	#upload to database
		file = request.files['pantry']
		newFile = Projects(name=file.filename, project_id=20)
		db.session.add(newFile)
		db.session.commit()
		
	stair = StairForm()
	if stair.validate_on_submit() and 'stair' in request.files:
	#upload to folder
		filename = photos.save(request.files['stair'])
	#upload to database
		file = request.files['stair']
		newFile = Projects(name=file.filename, project_id=21)
		db.session.add(newFile)
		db.session.commit()
		
	egress = EgressForm()
	if egress.validate_on_submit() and 'egress' in request.files:
	#upload to folder
		filename = photos.save(request.files['egress'])
	#upload to database
		file = request.files['egress']
		newFile = Projects(name=file.filename, project_id=22)
		db.session.add(newFile)
		db.session.commit()
		
	kitchen = KitchenForm()
	if kitchen.validate_on_submit() and 'kitchen' in request.files:
	#upload to folder
		filename = photos.save(request.files['kitchen'])
	#upload to database
		file = request.files['kitchen']
		newFile = Projects(name=file.filename, project_id=23)
		db.session.add(newFile)
		db.session.commit()
		
	window = WindowForm()
	if window.validate_on_submit() and 'window' in request.files:
	#upload to folder
		filename = photos.save(request.files['window'])
	#upload to database
		file = request.files['window']
		newFile = Projects(name=file.filename, project_id=24)
		db.session.add(newFile)
		db.session.commit()
		
	roof = RoofForm()
	if roof.validate_on_submit() and 'roof' in request.files:
	#upload to folder
		filename = photos.save(request.files['roof'])
	#upload to database
		file = request.files['roof']
		newFile = Projects(name=file.filename, project_id=25)
		db.session.add(newFile)
		db.session.commit()
	return render_template('admin/projects.html', garages=garages, concrete=concrete, decks=decks, basement=basement, bathroom=bathroom, tile=tile, walls=walls, office=office, fencing=fencing, handicap=handicap, siding=siding, island=island, flooring=flooring, stairs=stairs, railing=railing, vanity=vanity, fireplace=fireplace, playhouse=playhouse, bunkbeds=bunkbeds, pantry=pantry, stair=stair, egress=egress, kitchen=kitchen, window=window, roof=roof)

if __name__ == '__main__':
	app.jinja_env.auto_reload = True
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.config['DEBUG'] = True
	app.run()