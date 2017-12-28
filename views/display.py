from flask import Flask, render_template, request, redirect, url_for
from models.projects import Project, Image, db
from forms.contact import Contact
from config import app
from views.projects import s3projects
import smtplib

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
	projects = Project.query.filter_by().order_by(Project.name).all()
	return render_template('projects.html', projects=projects, s3projects=s3projects)
	
@app.route('/contact', methods=["POST", "GET"])
def contact():
	form = Contact()
	if form.validate_on_submit():
		sender = request.form["email"]
		receiver = 'hunterk31@hotmail.com'
		message = request.form["message"]

		smtpObj = smtplib.SMTP('localhost')
		smtpObj.sendmail(sender, receiver, message)
		return "Successfully sent email"
		
	return render_template('contact.html', form=form)