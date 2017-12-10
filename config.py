from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://pubmupmhagrshg:99f9def95ffb68fc3c943de3cf22488c6957645ebeb5b7820fa2b8d90852c273@ec2-54-227-237-223.compute-1.amazonaws.com:5432/ddkgm2fojt63dl'
app.config['SECRET_KEY'] = 'jfeiios;alsei*#@@!fdkj;sa'
db = SQLAlchemy(app)
