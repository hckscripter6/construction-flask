from flask import Flask, render_template, request, redirect, url_for
from config import app
from werkzeug import secure_filename
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.authentication import User, db
from forms.authentication import LoginForm, RegisterForm

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

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