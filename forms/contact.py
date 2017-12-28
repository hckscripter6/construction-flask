from wtforms import SubmitField, TextAreaField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length

class Contact(FlaskForm):
	name = StringField('Name', validators=[InputRequired()])
	email = StringField('Email', validators=[InputRequired(), Email('Email is required')])
	subject = StringField('Subject', validators=[InputRequired()])
	message = TextAreaField('Message', validators=[InputRequired()])
	submit = SubmitField('Send')