from app import app
import psycopg2
import psycopg2.extras
from resources.models import db, User, About, Blog, Product

def init_database():
	db.session.rollback()
	db.drop_all()
	db.create_all()

	s1 = "Wash & Go"
	s2 = "Perm"
	s3 = "Beat Yo Shit"
	u1 = User("Phony", "Dude", "phony@fuckmail.com", "passwerd123")
	u2 = User("Fake", "Bitch", "fake@hotmess.com", "dumbshit")
	b1 = Blog("Blog entry 1", "This is just some dumb ass shit that I am typing to create this")
	b2 = Blog("Put it up", "This is just another meaningless sentence")
	a1 = About("This is a dumb about statement")
	p1 = Product(s1, "Get that dirty shit smelling good", 30)
	p2 = Product(s2, "Is yo shit nappy? Come get a damn perm bitch", 40)
	p3 = Product(s3, "Get yo shit tight for the club tonight so you can ind yourself a man", 80)

	db.session.add(u1)
	db.session.add(u2)
	db.session.add(b1)
	db.session.add(b2)
	db.session.add(a1)	
	db.session.add(p1)
	db.session.add(p2)
	db.session.add(p3)
	db.session.commit()

def get_products():
	return Product.query.all()

def get_users():
	return User.query.all()

def get_blog():
	blogs = Blog.query.all()
	b_list = []
	for b in blogs:
		data = {}
		date = date_format(b.date)
		data['f_date'] = date
		data['blog'] = b
		b_list.append(data)
	return b_list


def date_format(date):
	format = date.strftime("%B %d, %Y [%I:%m %p]")
	return format

def get_current_about():
	abouts = About.query.all()
	current = None

	for a in abouts:
		if a.is_current == True:
			return a.statement





