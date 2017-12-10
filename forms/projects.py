from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField

class ConcreteForm(FlaskForm):
	concrete = FileField('concrete')
	submit = SubmitField()
	
class DeckForm(FlaskForm):
	decks = FileField('decks')
	submit = SubmitField()
	
class GarageForm(FlaskForm):
	garages = FileField('garages')
	submit = SubmitField()	
	
class BasementForm(FlaskForm):
	basement = FileField('basement')
	submit = SubmitField()	
	
class BathroomForm(FlaskForm):
	bathroom = FileField('bathroom')
	submit = SubmitField()	
	
class TileForm(FlaskForm):
	tile = FileField('tile')
	submit = SubmitField()
	
class WallForm(FlaskForm):
	walls = FileField('walls')
	submit = SubmitField()
	
class OfficeForm(FlaskForm):
	office = FileField('office')
	submit = SubmitField()
	
class FencingForm(FlaskForm):
	fencing = FileField('fencing')
	submit = SubmitField()

class HandicapForm(FlaskForm):
	handicap = FileField('handicap')
	submit = SubmitField()
	
class SidingForm(FlaskForm):
	siding = FileField('siding')
	submit = SubmitField()
	
class IslandForm(FlaskForm):
	island = FileField('island')
	submit = SubmitField()
	
class FlooringForm(FlaskForm):
	flooring = FileField('flooring')
	submit = SubmitField()
	
class StairsForm(FlaskForm):
	stairs = FileField('stairs')
	submit = SubmitField()

class RailingForm(FlaskForm):
	railing = FileField('railing')
	submit = SubmitField()
	
class VanityForm(FlaskForm):
	vanity = FileField('vanity')
	submit = SubmitField()

class FireplaceForm(FlaskForm):
	fireplace = FileField('fireplace')
	submit = SubmitField()
	
class PlayhouseForm(FlaskForm):
	playhouse = FileField('playhouse')
	submit = SubmitField()
	
class BunkbedForm(FlaskForm):
	bunkbeds = FileField('bunkbeds')
	submit = SubmitField()
	
class PantryForm(FlaskForm):
	pantry = FileField('pantry')
	submit = SubmitField()

class StairForm(FlaskForm):
	stair = FileField('stair')
	submit = SubmitField()
	
class EgressForm(FlaskForm):
	egress = FileField('egress')
	submit = SubmitField()
	
class KitchenForm(FlaskForm):
	kitchen = FileField('kitchen')
	submit = SubmitField()
	
class WindowForm(FlaskForm):
	window = FileField('window')
	submit = SubmitField()
	
class RoofForm(FlaskForm):
	roof = FileField('roof')
	submit = SubmitField()