from wtforms import SubmitField, FileField
from flask_wtf import Form
from wtforms.validators import InputRequired

class FileForm(Form):
	image = FileField('Upload', validators=[InputRequired()])
	submit = SubmitField()
	
class FileForm(Form):
	image = FileField('Upload', validators=[InputRequired()])
	submit = SubmitField()