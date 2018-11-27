from app import db
from models import BlogPost

# create database and tables
db.create_all()

db.session.add(BlogPost('First post', 'First content'))
db.session.add(BlogPost('Second post', 'Second content'))
db.session.commit()