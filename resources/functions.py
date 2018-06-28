from app import app
import psycopg2
import psycopg2.extras
from resources.models import *

def init_database():
	db.session.rollback()
	db.drop_all()
	db.create_all()

	s1 = "Wash & Go"
	s2 = "Perm"
	s3 = "Beat Yo Shit"
	u1 = User("Phony", "Dude", "phony@fuckmail.com", "passwerd123")
	u2 = User("Fake", "Bitch", "fake@hotmess.com", "dumbshit")
	u3 = User("Test", "User", "test@test.com", "1234")
	b1 = Blog("Blog entry 1", "This is just some dumb ass shit that I am typing to create this")
	b2 = Blog("Put it up", "This is just another meaningless sentence")
	a1 = About("This is a dumb about statement")
	p1 = Product(s1, "Get that dirty shit smelling good", 30)
	p2 = Product(s2, "Is yo shit nappy? Come get a damn perm bitch", 40)
	p3 = Product(s3, "Get yo shit tight for the club tonight so you can find yourself a man", 80)

	a2 = About("This is another about us statement.")
	a3 = About("Writing stuff to fill up this third about us statement.")
	a2.is_current = False
	a3.is_current = False

	db.session.add(u1)
	db.session.add(u2)
	db.session.add(u3)
	db.session.add(b1)
	db.session.add(b2)
	db.session.add(a1)
	db.session.add(a2)
	db.session.add(a3)	
	db.session.add(p1)
	db.session.add(p2)
	db.session.add(p3)
	db.session.commit()

def index_content():
	content = {}
	content['title'] = "Natural Woman Salon"
	content['btn_data'] = -1
	return content

def home_content():
	content = {}
	content['title'] = "Natural Woman Salon | Home"
	content['btn_data'] = 0
	return content

def about_content():
	content = {}
	content['title'] = "Natural Woman Salon | About Us"
	content['btn_data'] = 1
	about = About.query.all()
	current = None
	for a in about:
		if a.is_current == True:
			current = a.statement
	content['about'] = current
	return content

def product_content():
	content ={}
	content['title'] = "Natural Woman Salon | Services"
	content['btn_data'] = 2
	content['products'] = Product.query.all()
	return content

def gallery_content():
	content = {}
	content['title'] = "Natural Woman Salon | Gallery"
	content['btn_data'] = 3
	return content

def blog_content():
	content = {}
	content['title'] = "Natural Woman Salon | Lora's Blog"
	content['btn_data'] = 4
	blogs = Blog.query.all()
	b_list = []
	for b in blogs:
		data = {}
		date = date_format(b.date)
		data['f_date'] = date
		data['blog'] = b
		b_list.append(data)
	content['blogs'] = b_list
	return content

def contact_content():
	content = {}
	content['title'] = "Natural Woman Salon | Contact Us"
	content['btn_data'] = 5
	return content

def admin_home_content():
	content = {}
	content['title'] = "Natural Woman Salon | Administration"
	content['btn_data'] = 6
	return content

def new_blog_content():
	content = {}
	content['title'] = "Natural Woman Salon | New Blog Post"
	content['btn_data'] = 6
	return content

def blog_tool_content():
	content = {}
	content['title'] = "Natural Woman Salon | Manage Blog Post"
	content['btn_data'] = 7
	content['blogs'] = get_formatted_blogs()
	return content

def about_tool_content():
	content = {}
	content['title'] = "Natural Woman Salon | Administration"
	content['btn_data'] = 8
	current = About.query.filter_by(is_current=True).one()
	abouts = About.query.all()
	a_list = []
	for a in abouts:
		if a.id != current.id:
			a_list.append(a)
	content['current'] = current
	content['inactive'] = a_list
	return content

def product_tool_content():
	content = {}
	content['title'] = "Natural Woman Salon | Product Management"
	content['btn_data'] = 9
	content['products'] = Product.query.all()
	return content

def gallery_tool_content():
	content = {}
	content['title'] = "Natural Woman Salon | Gallery Management"
	content['btn_data'] = 10
	return content

def company_tool_content():
	content = {}
	content['title'] = "Natural Woman Salon | Admin Tools"
	content['btn_data'] = 11
	return content

def account_tool_content():
	content = {}
	content['title'] = "Natural Woman Salon | My Account"
	content['btn_data'] = 12
	return content

def user_tool_content():
	content = {}
	content['title'] = "Natural Woman Salon | User Management"
	content['btn_data'] = 13
	content['users'] = get_model_list("User") #be sure to edit this and limit who shows up
	return content

def get_formatted_blogs():
	blogs = Blog.query.all()
	b_list = []
	for b in blogs:
		data = {}
		date = date_format(b.date)
		data['f_date'] = date
		data['blog'] = b
		b_list.append(data)
	return b_list

def exclude_current_about(aid):
	results = []
	aid = int(aid)
	a_list = fetch_about(aid)
	for a in a_list:
		if int(a.id) != aid:
			results.append(a)
	return results

def get_users():
	return User.query.all()

def get_model_list(m_type):
	m_type = str(m_type)
	model = None
	if m_type == "About":
		model = About.query.all()
	elif m_type == "Blog":
		model = Blog.query.all()
	elif m_type == "Product":
		model = Product.query.all()
	elif m_type == "User":
		model = User.query.all()

def fetch_product(p_id):
	product = Product.query.filter_by(id=p_id).one()
	return product

def fetch_about(p_id):
	about = About.query.filter_by(id=p_id).one()
	return about

def fetch_blog(p_id):
	blog = Blog.query.filter_by(id=p_id).one()
	return blog

def fetch_user(p_id):
	user = User.query.filter_by(id=p_id).one()
	return user

def fetch(model_type, m_id):
	m_id = int(m_id)
	model = -1
	if model_type == "About":
		model = fetch_about(m_id)
	elif model_type == "Blog":
		model = fetch_blog(m_id)
	elif model_type == "Product":
		model = fetch_product(m_id)
	elif model_type == "User":
		model = fetch_user(m_id)
	return model


def date_format(date):
	format = date.strftime("%B %d, %Y [%I:%m %p]")
	return format

def new_blog(subject, content):
	subject = str(subject)
	content = str(content)
	blog = -1
	if len(subject) != 0 and len(content) != 0:
		blog = Blog(subject, content)
		db.session.add(blog)
		db.session.commit()
	return blog

def new_product(service, description, price):
	product = -1
	q = Product.query.filter_by(Product.service==str(service)).one()
	if q != []:
		if len(str(service)) != 0 and len(str(description)) != 0 and str(price) != "0":
			product = Product(str(service), str(description), int(price))
			db.session.add(product)
			db.session.commit()
	return product

def new_about(statement, kepp_old):
	about = -1
	current = -1
	statement = str(statement)
	abouts = About.query.all()
	for a in abouts:
		if a.is_current == True:
			current = a
			break
	if keep_old == True:
		current.is_current = False
		about = About(statement)
		db.session.add(about)
		db.session.commit()
	else:
		no_entries = len(abouts)
		if no_entries != 1:
			about = About(statement)
			db.session.delete(current)
			db.session.add(about)
			db.session.commit()
	return about

def new_user(fname, lname, email, password):
	user = -1
	q = User.query.filter_by(User.email==str(email)).one()
	if q != []:
		user = User(str(fname), str(lname), str(email), str(password))
		db.session.add(user)
		db.session.commit()
	return user

def delete_user(u_id):
	user = fetch_user(u_id)
	if user != -1:
		db.session.delete(user)
		db.commit()
	return user

def delete_about(a_id):
	about = fetch_about(a_id)
	if about != -1:
		db.session.delete(about)
		db.commit()
	return user

def delete_blog(b_id):
	blog = fetch_about(b_id)
	if blog != -1:
		db.session.delete(blog)
		db.commit()
	return user

def update_user_name(fname, lname, u_id):
	user = fetch_user(u_id)
	if user != -1:
		user.fname = fname
		user.lname = lname
		db.session.commit()
	return user

def update_email(email, u_id):
	user = fetch_user(u_id)
	if user != -1:
		user.email = email
		db.session.commit()
	return user

def update_password(password, u_id):
	user = fetch_user(u_id)
	if user != -1:
		user.set_password()
	return user

def update_product(description, price, p_id):
	p = fetch_product(p_id)
	if p != -1:
		if len(str(description)) != 0:
			p.description = str(description)
		if str(price) != "0":
			p.price = int(price)
		db.session.commit()
	return p

def update_about(statement):
	changed = False
	current = About.query.filter_by(About.is_current==True).one()
	if current != []:
		if len(str(statement)) != 0:
			current.statement = str(statement)
			changed = True
	return changed

def update_blog(subject, content, b_id):
	b = fetch_blog(b_id)
	if b != -1:
		if len(str(subject)) != 0:
			b.subject = str(subject)
		if len(str(content)) != 0:
			b.content = str(content)
		db.session.commit()
	return b

def swap_about_statement(a_id):
	a = fetch_about(a_id)
	if a != -1:
		current = About.query.filter_by(About.is_current==True).one()
		current.is_current = False
		a.is_current = True
		db.session.commit()
	return a

# def auth(email, password):
# 	user = -1
# 	email = str(email)
# 	password = str(password)
# 	q = User.query.filter_by(str(User.email)==email).one()
# 	if q != []:
# 		if q.is_correct_password(password):
# 			user = q
# 			user.authenticated = True
# 			db.session.commit()
# 	return user

# def logout(u_id):
# 	user = fetch_user(u_id)
# 	if user != -1:
# 		if user.authenticated == True:
# 			user.authenticated = False
# 			db.session.commit()
# 	return user











































