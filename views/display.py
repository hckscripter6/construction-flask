from flask import Flask, render_template, request, redirect, url_for
from models.projects import Projects
from config import app
from views.projects import s3projects

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
	return render_template('projects.html', concrete=concrete, decks=decks, garages=garages, basement=basement, bathroom=bathroom, tile=tile, office=office, fencing=fencing, handicap=handicap, siding=siding, island=island, flooring=flooring, stairs=stairs, railing=railing, vanity=vanity, fireplace=fireplace, playhouse= playhouse, bunkbeds=bunkbeds, pantry=pantry, stair=stair, egress=egress, kitchen=kitchen, window=window, roof=roof, s3projects=s3projects)
	
@app.route('/contact')
def contact():
	return render_template('contact.html')