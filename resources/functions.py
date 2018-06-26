from app import app
from resources.models import db, User, About, Blog, Service, Product

def init_database():
	db.session.rollback()
	db.drop_all()
	db.create_all()

	s1 = User("Fake", "Nigga", "phony@fakeass.com", "password123")
	s2 = Service("Perm")
	s3 = Service("Beat Yo Shit")
	u1 = User("Phony", "Dude", "phony@fuckmail.com", "passwerd123")
	u2 = User("Fake", "Bitch", "fake@hotmess.com", "dumbshit")
	b1 = Blog("Blog entry 1", "This is just some dumb ass shit that I am typing to create this")
	b2 = Blog("Put it up", "This is just another meaningless sentence")
	a1 = About("This is a dumb about statement")

	db.session.add(s1)
	db.session.add(s2)
	db.session.add(s3)
	db.session.add(u1)
	db.session.add(u2)
	db.session.add(b1)
	db.session.add(b2)
	db.session.add(a1)
	db.session.commit()


def test_functions():
	print("ACCESSING FUNCTIONS MODULE")