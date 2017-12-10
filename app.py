from config import app
from models import projects, authentication
from views import projects, authentication, display
from forms import projects, authentication	






if __name__ == '__main__':
	app.jinja_env.auto_reload = True
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.config['DEBUG'] = True
	app.run()