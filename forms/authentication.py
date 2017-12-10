from wtforms import SubmitField, FileField, StringField, PasswordField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length

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
