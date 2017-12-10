from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123qweasdzxc!@#@localhost/briney'
app.config['SECRET_KEY'] = 'jfeiios;alsei*#@@!fdkj;sa'
db = SQLAlchemy(app)
