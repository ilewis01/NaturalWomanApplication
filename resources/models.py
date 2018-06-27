from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime
from app import app
from resources.functions import *

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    __tablename__ = "users"
    id      = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    fname   = db.Column('fname', db.String(120), nullable=False)
    lname   = db.Column('lname', db.String(120), nullable=False)
    email   = db.Column('email', db.String(120), nullable=False, unique=True)
    password = db.Column('password', db.Binary(60), nullable=False)
    authenticated = db.Column('is_authenticated', db.Boolean, default=False)

    def __init__(self, fname, lname, email, plaintext_password):
        self.email = email
        self.fname = fname
        self.lname = lname
        self.authenticated = False
        password = bcrypt.generate_password_hash(plaintext_password)
        self.password = password

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)
        db.session.commit()

    def is_correct_password(plaintext_password):
        return bcrypt.check_password_hash(self.password, plaintext_password)

    def __repr__(self):
        name = str(self.fname) + " " + str(self.lname)
        return '<User: %s>' % name

class Product(db.Model):
    __tablename__ = "products"
    id          = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    service     = db.Column('service', db.String(250), unique=True, nullable=False)
    description = db.Column('description', db.String(3000))
    price       = db.Column('price', db.Integer)

    def __init__(self, service, description, price):
        self.service = service
        self.description = description
        self.price = price

    def __repr__(self):
        rep = str(self.service) + " $" + str(self.price)
        return '<Product: %s>' % rep
  
class Blog(db.Model):
    __tablename__ = "blogs"
    id      = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    subject = db.Column('subject', db.String(400))
    content = db.Column('content', db.String(20000))
    date    = db.Column('date', db.TIMESTAMP)

    def __init__(self, subject, content):
        self.subject = subject
        self.content = content
        self.date = datetime.now()

    def __repr__(self):
        rep = str(self.date) + " - " + str(self.subject)
        return '<Blog Post: %s>' % rep
 
class About(db.Model):
    __tablename__ = "about"
    id          = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    statement   = db.Column('statement', db.String(2000))
    is_current  = db.Column('is_current', db.Boolean)

    def __init__(self, statement):
        self.statement = statement
        self.is_current = True

    def __repr__(self):
        return '<About Us: %r>' % self.statement









