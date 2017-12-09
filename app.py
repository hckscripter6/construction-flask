from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms import SubmitField, FileField, StringField, PasswordField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug import secure_filename
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123qweasdzxc!@#@localhost/briney'
app.config['SECRET_KEY'] = 'jfeiios;alsei*#@@!fdkj;sa'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(30), unique=True)
	email = db.Column(db.String(50))
	password = db.Column(db.String(80))
	
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/images/uploads'
configure_uploads(app, photos)

class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=25)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	remember = BooleanField('remember me')
	submit = SubmitField()
	
class RegisterForm(FlaskForm):
	email = StringField('email', validators=[InputRequired(), Length(min=4, max=50)])
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=25)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	submit = SubmitField()

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
	filename = db.Column(db.String(300))
	project = db.Column(db.String(300))
	tag = db.Column(db.String(25))
	
	def __init__(self, filename, project, tag):
		self.filename = filename
		self.project = project  
		self.tag = tag

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
	concrete = Projects.query.filter_by(tag="concrete").order_by(Projects.id.desc()).all()
	decks = Projects.query.filter_by(tag="decks").order_by(Projects.id.desc()).all()
	garages = Projects.query.filter_by(tag="garages").order_by(Projects.id.desc()).all()
	basement = Projects.query.filter_by(tag="basement").order_by(Projects.id.desc()).all()
	bathroom = Projects.query.filter_by(tag="bathroom").order_by(Projects.id.desc()).all()
	tile = Projects.query.filter_by(tag="tile").order_by(Projects.id.desc()).all()
	walls = Projects.query.filter_by(tag="walls").order_by(Projects.id.desc()).all()
	office = Projects.query.filter_by(tag="office").order_by(Projects.id.desc()).all()
	fencing = Projects.query.filter_by(tag="fencing").order_by(Projects.id.desc()).all()
	handicap = Projects.query.filter_by(tag="handicap").order_by(Projects.id.desc()).all()
	siding = Projects.query.filter_by(tag="siding").order_by(Projects.id.desc()).all()
	island = Projects.query.filter_by(tag="island").order_by(Projects.id.desc()).all()
	flooring = Projects.query.filter_by(tag="flooring").order_by(Projects.id.desc()).all()
	stairs = Projects.query.filter_by(tag="stairs").order_by(Projects.id.desc()).all()
	railing = Projects.query.filter_by(tag="railing").order_by(Projects.id.desc()).all()
	vanity = Projects.query.filter_by(tag="vanity").order_by(Projects.id.desc()).all()
	fireplace = Projects.query.filter_by(tag="fireplace").order_by(Projects.id.desc()).all()
	playhouse = Projects.query.filter_by(tag="playhouse").order_by(Projects.id.desc()).all()
	bunkbeds = Projects.query.filter_by(tag="bunkbeds").order_by(Projects.id.desc()).all()
	pantry = Projects.query.filter_by(tag="pantry").order_by(Projects.id.desc()).all()
	stair = Projects.query.filter_by(tag="stair").order_by(Projects.id.desc()).all()
	egress = Projects.query.filter_by(tag="egress").order_by(Projects.id.desc()).all()
	kitchen = Projects.query.filter_by(tag="kitchen").order_by(Projects.id.desc()).all()
	window = Projects.query.filter_by(tag="window").order_by(Projects.id.desc()).all()
	roof = Projects.query.filter_by(tag="roof").order_by(Projects.id.desc()).all()
	return render_template('projects.html', concrete=concrete, decks=decks, garages=garages, basement=basement, bathroom=bathroom, tile=tile, office=office, fencing=fencing, handicap=handicap, siding=siding, island=island, flooring=flooring, stairs=stairs, railing=railing, vanity=vanity, fireplace=fireplace, playhouse= playhouse, bunkbeds=bunkbeds, pantry=pantry, stair=stair, egress=egress, kitchen=kitchen, window=window, roof=roof)
	
@app.route('/contact')
def contact():
	return render_template('contact.html')
	
@app.route('/signup', methods=["GET", "POST"])
def signup():
	register = RegisterForm()
	
	if register.validate_on_submit():
		hashed_password = generate_password_hash(register.password.data, method='sha256')
		new_user = User(username=register.username.data, email=register.email.data, password=hashed_password)
		db.session.add(new_user)
		db.session.commit()
		return 'New user added'
	return render_template('admin/signup.html',register=register)
	
@app.route('/login', methods=["POST", "GET"])
def login():
	login = LoginForm()
	if login.validate_on_submit():
		user = User.query.filter_by(username=login.username.data).first()
		if user:
			if check_password_hash(user.password, login.password.data):
				login_user(user, remember=login.remember.data)
				return redirect(url_for('admin_projects'))
	return render_template('admin/login.html', login=login)
	
@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))
	

'''@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
	return render_template('admin/dashboard.html')'''
	
@app.route('/dashboard/projects/<tag>', methods=['GET', 'POST'])
@login_required
def project_edit(tag):
	project_title = Projects.query.filter_by(tag=tag).first()
	project = Projects.query.filter_by(tag=tag).order_by(Projects.id.desc()).all()
	return render_template('admin/single_project.html', project=project, project_title=project_title)
	
@app.route('/dashboard/projects/<tag>/<filename>', methods=['GET', 'POST'])
@login_required
def picture_edit(tag, filename):
	image = Projects.query.filter_by(filename=filename).order_by(Projects.id.desc()).first()

	return render_template('admin/single_image.html', image=image)
	
@app.route('/dashboard/projects/<tag>/<filename>/delete', methods=['GET', 'POST'])
@login_required
def delete(tag, filename):
	image = Projects.query.filter_by(filename=filename).first()
	os.remove('static/images/uploads/'+ image.filename)
	db.session.delete(image)
	db.session.commit()
	return 'The image has been successfuly deleted'
	
@app.route('/dashboard/projects', methods=['GET', 'POST'])
@login_required
def admin_projects():  #Each comment refers to the line of code below it
#Concrete flatwork
	#access form data 
	concrete = ConcreteForm()
	#if the form is submited......
	if concrete.validate_on_submit() and 'concrete' in request.files:
		#Assign file request data to variable
		file = request.files['concrete']
		#Assign function (that checks if file already exists in folder) to a variable
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		#if file already exists in folder prior to submission then display page that gives error message
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		#else if file does not exist in folder prior to submission.....
		else:
			#upload file to folder
			filename = photos.save(request.files['concrete'])
			#upload file info to database
			newFile = Projects(filename=file.filename, project="Concrete", tag="concrete")
			db.session.add(newFile)
			db.session.commit()
		#if file has successfully been submitted to folder and file info is successfully entered to database then redirect to admin page that displays photos to current project
		return redirect('/dashboard/projects/concrete')

#repeat these steps with remaining projects! :)		
	decks = DeckForm()
	if decks.validate_on_submit() and 'decks' in request.files:
		file = request.files['decks']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['decks'])
			newFile = Projects(filename=file.filename, project="Decks", tag="decks")
			db.session.add(newFile)
			db.session.commit()	
		return redirect('/dashboard/projects/decks')
		
	garages = GarageForm()
	if garages.validate_on_submit() and 'garages' in request.files:
		file = request.files['garages']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['garages'])
			newFile = Projects(filename=file.filename, project="Garages, polebarns and sheds", tag="garages")
			db.session.add(newFile)
			db.session.commit()	
		return redirect('/dashboard/projects/garages')
		
	basement = BasementForm()
	if basement.validate_on_submit() and 'basement' in request.files:
		file = request.files['basement']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['basement'])
			newFile = Projects(filename=file.filename, project="Finished basement including greatroom, bedroom, and bathroom", tag="basement")
			db.session.add(newFile)
			db.session.commit()	
		return redirect('/dashboard/projects/basements')
		
	bathroom = BathroomForm()
	if bathroom.validate_on_submit() and 'bathroom' in request.files:
		file = request.files['bathroom']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['bathroom'])
			newFile = Projects(filename=file.filename, project="Bathroom remodels", tag="bathroom")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/bathroom')
		
		
	tile = TileForm()
	if tile.validate_on_submit() and 'tile' in request.files:
		file = request.files['tile']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['tile'])
			newFile = Projects(filename=file.filename, project="Tile work", tag="tile")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/tile')
		
	office = OfficeForm()
	if office.validate_on_submit() and 'office' in request.files:
		file = request.files['office']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['office'])
			newFile = Projects(filename=file.filename, project="Converted half of a garage into a very nice office", tag="office")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/office')
		
	fencing = FencingForm()
	if fencing.validate_on_submit() and 'fencing' in request.files:
		file = request.files['fencing']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['fencing'])
			newFile = Projects(filename=file.filename, project="Fencing", tag="fencing")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/fencing')
		
	handicap = HandicapForm()
	if handicap.validate_on_submit() and 'handicap' in request.files:
		file = request.files['handicap']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['handicap'])
			newFile = Projects(filename=file.filename, project="Handicap shower", tag="handicap")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/handicap')
		
	siding = SidingForm()
	if siding.validate_on_submit() and 'siding' in request.files:
		file = request.files['siding']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['siding'])
			newFile = Projects(filename=file.filename, project="Siding", tag="siding")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/siding')
		
	island = IslandForm()
	if island.validate_on_submit() and 'island' in request.files:
		file = request.files['island']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['island'])
			newFile = Projects(filename=file.filename, project="Custom island", tag="island")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/island')
		
	flooring = FlooringForm()
	if flooring.validate_on_submit() and 'flooring' in request.files:
		file = request.files['flooring']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['flooring'])
			newFile = Projects(filename=file.filename, project="Flooring", tag="flooring")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/flooring')
		
	stairs = StairsForm()
	if stairs.validate_on_submit() and 'stairs' in request.files:
		file = request.files['stairs']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['stairs'])
			newFile = Projects(filename=file.filename, project="Wood stairs", tag="stairs")
			db.session.add(newFile)
			db.session.commit()	
		return redirect('dashboard/projects/stairs')
		
	railing = RailingForm()
	if railing.validate_on_submit() and 'railing' in request.files:
		file = request.files['railing']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['railing'])
			newFile = Projects(filename=file.filename, project="Railing", tag="railing")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/railing')
		
	vanity = VanityForm()
	if vanity.validate_on_submit() and 'vanity' in request.files:
		file = request.files['vanity']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['vanity'])
			newFile = Projects(filename=file.filename, project="Custom vanity", tag="vanity")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/vanity')
		
	fireplace = FireplaceForm()
	if fireplace.validate_on_submit() and 'fireplace' in request.files:
		file = request.files['fireplace']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['fireplace'])
			newFile = Projects(filename=file.filename, project="Custom fireplace", tag="fireplace")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/fireplace')
		
	playhouse = PlayhouseForm()
	if fireplace.validate_on_submit() and 'playhouse' in request.files:
		file = request.files['playhouse']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['playhouse'])
			newFile = Projects(filename=file.filename, project="Kids playhouse", tag="playhouse")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/playhouse')
		
	bunkbeds = BunkbedForm()
	if bunkbeds.validate_on_submit() and 'bunkbeds' in request.files:
		file = request.files['bunkbeds']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['bunkbeds'])
			newFile = Projects(filename=file.filename, project="Kids bunkbeds", tag="bunkbeds")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/bunkbeds')
		
	pantry = PantryForm()
	if pantry.validate_on_submit() and 'pantry' in request.files:
		file = request.files['pantry']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['pantry'])
			newFile = Projects(filename=file.filename, project="Custom kitchen pantry", tag="pantry")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/pantry')
		
	stair = StairForm()
	if stair.validate_on_submit() and 'stair' in request.files:
		file = request.files['stair']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['stair'])
			newFile = Projects(filename=file.filename, project="Stair railing", tag="stair")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/stair')
		
	egress = EgressForm()
	if egress.validate_on_submit() and 'egress' in request.files:
		file = request.files['egress']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['egress'])
			newFile = Projects(filename=file.filename, project="Egress window well", tag="egress")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/egress')
		
	kitchen = KitchenForm()
	if kitchen.validate_on_submit() and 'kitchen' in request.files:
		file = request.files['kitchen']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['kitchen'])
			newFile = Projects(filename=file.filename, project="Custom kitchen", tag="kitchen")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/kitchen')
		
	window = WindowForm()
	if window.validate_on_submit() and 'window' in request.files:
		file = request.files['window']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['window'])
			newFile = Projects(filename=file.filename, project="Window", tag="window")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/window')		
		
	roof = RoofForm()
	if roof.validate_on_submit() and 'roof' in request.files:
		file = request.files['roof']
		FileAlreadyUploaded = os.path.exists("static/images/uploads/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['roof'])
			newFile = Projects(filename=file.filename, project="New siding and re-roof", tag="roof")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/roof')
		
	return render_template('admin/projects.html', garages=garages, concrete=concrete, decks=decks, basement=basement, bathroom=bathroom, tile=tile, office=office, fencing=fencing, handicap=handicap, siding=siding, island=island, flooring=flooring, stairs=stairs, railing=railing, vanity=vanity, fireplace=fireplace, playhouse=playhouse, bunkbeds=bunkbeds, pantry=pantry, stair=stair, egress=egress, kitchen=kitchen, window=window, roof=roof)

if __name__ == '__main__':
	app.jinja_env.auto_reload = True
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.config['DEBUG'] = True
	app.run()