from flask import Flask, render_template, request, redirect, url_for
from config import app
import os, json, boto3
from flask_login import login_required
from models.projects import Project, Image, db
from forms.projects import FileForm, AddProject

s3 = boto3.resource('s3')
client = boto3.client('s3')
s3projects = "https://brineyconstruction-app.s3.amazonaws.com/projects"

def tag_generator(val):
	a = val.split()
	b = "-".join(a)
	c = b.lower()
	d = c.strip()
	e = d.replace(",", "")
	f = e.replace(".", "")
	return f

@app.route('/dashboard/projects/<tag>', methods=['GET', 'POST'])
@login_required
def project_edit(tag):
	project_title = Project.query.filter_by(tag=tag).first()
	#project = Project.query.filter_by(tag=tag).order_by(Project.id.desc()).all()
	return render_template('admin/single_project.html', s3projects=s3projects, project_title=project_title)
	
@app.route('/dashboard/projects/<tag>/<name>', methods=['GET', 'POST'])
@login_required
def picture_edit(tag, name):
	image = Project.query.filter_by(name=name).order_by(Projects.id.desc()).first()
	return render_template('admin/single_image.html', image=image, s3projects=s3projects)
	
@app.route('/dashboard/projects/<tag>/<image_name>/delete', methods=['GET', 'POST'])
@login_required
def delete(tag, image_name):
	project = Project.query.filter_by(tag=tag).first()
	filename = project.image.name=image_name
	delete_data = Image.query.filter_by(name=image_name).first()
	s3.Object('brineyconstruction-app', s3projects+"/"+ project.name +"/"+ filename).delete()
	db.session.delete(delete_data)
	db.session.commit()
	return 'The image has been successfuly deleted'


@app.route('/dashboard/projects', methods=['GET', 'POST'])
@login_required
def admin_projects():	
	upload = FileForm()
	project_loop = Project.query.all()
	if upload.validate_on_submit():
		for loop in project_loop:
			if request.form["project"] == loop.tag:
				file = request.files['file']
				s3.Bucket('brineyconstruction-app').put_object(Key='projects/'+ loop.name + '/'+ file.filename, Body=file)
				newFile = Image(name=file.filename, project=loop)
				db.session.add(newFile)
				db.session.commit()	
				return redirect('/dashboard/projects/'+loop.tag)
	
	option_loop = Project.query.all()
	
	add_project = AddProject()		
	if add_project.validate_on_submit():
		render_tag = tag_generator(request.form["project"])
		p = Project(name=request.form["project"], tag=render_tag)
		db.session.add(p)
		db.session.commit()
		return 'You have added the project'
	return render_template('admin/projects.html', option_loop=option_loop, s3projects=s3projects, upload=upload, add_project=add_project)
	
