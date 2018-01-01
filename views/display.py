from flask import Flask, render_template, request, redirect, url_for
from models.projects import Project, Image, db
from forms.contact import Contact
from config import app
from views.projects import s3projects
from flask_mail import Mail, Message
import os

index = False

mail = Mail(app)	


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
	projects = Project.query.join(Image).order_by(Project.name).all()
	return render_template('projects.html', projects=projects, s3projects=s3projects)
	
@app.route('/contact', methods=["POST", "GET"])
def contact():
	return render_template('contact.html', form=form)