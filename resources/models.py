from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import app

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "Users"
    id 		= db.Column(db.Integer, primary_key=True)
    fname 	= db.Column(db.String(120))
    lname 	= db.Column(db.String(120))
    email 	= db.Column(db.String(120), unique=True)

    def __init__(self, fname, lname, email, password):
        self.email = email
        self.fname = fname
        self.lname = lname

    def __repr__(self):
    	name = str(self.fname) + " " + str(self.lname)
        return '<User: %s>' % name

class Service(db.Model):
	__tablename__= "Services"
	id 		= db.Column(db.Integer, primary_key=True)
	service = db.Column(db.String(250), unique=True)

	def __init__(self, service):
		self.service = service

	def __repr__(self):
		return '<Service: %r>' % self.service

class Product(db.Model):
    __tablename__ = "Products"
    id 			= db.Column('id', db.Integer, primary_key=True)
    service_id 	= db.Column('service_id', db.Integer, db.ForeignKey('Services.id'))
    description = db.Column('description', db.String(3000))
    price 		= db.Column('price', db.Integer)
 
    service = db.relationship('Service', foreign_keys=service_id)

    def __init__(self, service_id, description, price):
    	self.service_id = service_id
    	self.description = description
    	self.price = price

    def __repr__(self):
    	rep = str(service.service) + " $" + str(self.price)
    	return '<Product: %s>' % rep
  
class Blog(db.Model):
   __tablename__ = "Blogs"
    id 		= db.Column('id', db.Integer, primary_key=True)
    subject = db.Column('subject', db.String(400))
    content = db.Column('content', db.String(20000))
    date 	= db.Column('date', db.Date)

    def __init__(self, subject, content):
    	self.subject = subject
    	self.content = content
    	self.date = datetime.now()

    def __repr__(self):
    	rep = str(self.date) + " - " + str(self.subject)
    	return '<Blog Post: %s>' % rep
 
class About(db.Model):
    __tablename__ = "About Us"
    id 			= db.Column('id', db.Integer, primary_key=True)
    statement 	= db.Column('statement', db.String(2000))
    is_current 	= db.Column('is_current', db.Boolean)

    def __init__(self, statement):
    	self.statement = statement
    	self.is_current = True

    def __repr__(self):
    	return '<About Us: %r>' % self.statement









