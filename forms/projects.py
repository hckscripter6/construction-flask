from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField, SelectField, StringField
from wtforms.validators import InputRequired


class FileForm(FlaskForm):
	file = FileField('file', validators=[InputRequired()])
	submit = SubmitField()
	
class AddProject(FlaskForm):
	project = StringField('project', validators=[InputRequired()])
	submit = SubmitField()
	
class SearchImages(FlaskForm):
	submit = SubmitField()