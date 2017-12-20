from flask import Flask, render_template, request, redirect, url_for
from models.projects import Project
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
	projects = Project.query.order_by(Project.id.desc()).all()
	return render_template('projects.html', projects=projects, s3projects=s3projects)
	
@app.route('/contact')
def contact():
	return render_template('contact.html')