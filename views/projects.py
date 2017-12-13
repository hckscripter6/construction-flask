from flask import Flask, render_template, request, redirect, url_for
from config import app
import os, json, boto3
from flask_login import login_required
from models.projects import Projects, db
from forms.projects import ConcreteForm, DeckForm, BasementForm, GarageForm, BathroomForm, BunkbedForm, EgressForm, FencingForm, FireplaceForm, FlooringForm, HandicapForm, IslandForm, KitchenForm, OfficeForm, PantryForm, PlayhouseForm, RailingForm, RoofForm, SidingForm, StairForm, StairsForm, TileForm, VanityForm, WindowForm

s3 = boto3.resource('s3')
s3projects = "https://brineyconstruction-app.s3.amazonaws.com/projects"

@app.route('/dashboard/projects/<tag>', methods=['GET', 'POST'])
@login_required
def project_edit(tag):
	project_title = Projects.query.filter_by(tag=tag).first()
	project = Projects.query.filter_by(tag=tag).order_by(Projects.id.desc()).all()
	return render_template('admin/single_project.html', s3projects=s3projects, project=project, project_title=project_title)
	
@app.route('/dashboard/projects/<tag>/<filename>', methods=['GET', 'POST'])
@login_required
def picture_edit(tag, filename):
	image = Projects.query.filter_by(filename=filename).order_by(Projects.id.desc()).first()
	return render_template('admin/single_image.html', image=image)
	
@app.route('/dashboard/projects/<tag>/<filename>/delete', methods=['GET', 'POST'])
@login_required
def delete(tag, filename):
	image = Projects.query.filter_by(filename=filename).first()
	os.remove('static/images/projects/'+ image.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['decks'])
			newFile = Projects(filename=file.filename, project="Decks", tag="decks")
			db.session.add(newFile)
			db.session.commit()	
		return redirect('/dashboard/projects/decks')
		
	garages = GarageForm()
	if garages.validate_on_submit():
		file = request.files['garages']
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			s3.Bucket('brineyconstruction-app').put_object(Key='projects/garages/'+str(file.filename), Body=file)
			newFile = Projects(filename=file.filename, project="Garages, polebarns and sheds", tag="garages")
			db.session.add(newFile)
			db.session.commit()	
		return redirect('/dashboard/projects/garages')
		
	basement = BasementForm()
	if basement.validate_on_submit() and 'basement' in request.files:
		file = request.files['basement']
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['basement'])
			newFile = Projects(filename=file.filename, project="Finished basement including greatroom, bedroom, and bathroom", tag="basement")
			db.session.add(newFile)
			db.session.commit()	
		return redirect('/dashboard/projects/basement')
		
	bathroom = BathroomForm()
	if bathroom.validate_on_submit() and 'bathroom' in request.files:
		file = request.files['bathroom']
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
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
		FileAlreadyUploaded = os.path.exists("static/images/projects/"+file.filename)
		if FileAlreadyUploaded:
			return render_template('admin/file_duplicate_message.html')
		else:
			filename = photos.save(request.files['roof'])
			newFile = Projects(filename=file.filename, project="New siding and re-roof", tag="roof")
			db.session.add(newFile)
			db.session.commit()
		return redirect('dashboard/projects/roof')
		
	return render_template('admin/projects.html', garages=garages, concrete=concrete, decks=decks, basement=basement, bathroom=bathroom, tile=tile, office=office, fencing=fencing, handicap=handicap, siding=siding, island=island, flooring=flooring, stairs=stairs, railing=railing, vanity=vanity, fireplace=fireplace, playhouse=playhouse, bunkbeds=bunkbeds, pantry=pantry, stair=stair, egress=egress, kitchen=kitchen, window=window, roof=roof, s3projects=s3projects)
	
