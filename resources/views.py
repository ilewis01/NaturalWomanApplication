
from flask import render_template, request
from app import app
from resources.functions import *

@app.route('/')
def index():
	content ={}
	content['title'] = "Natural Woman Salon | Home"
	content['post_data'] = 0
	return render_template('user/index.html', **content)

@app.route('/pricing')
def pricing():
	content = {}
	content['title'] = "Natural Woman Salon | Pricing"
	content['post_data'] = 4
	products = get_products()
	content['products'] = products
	print("Number of Products: " + str(len(products)))
	print(products)
	return render_template('user/pricing.html', **content)

@app.route('/about')
def about():
	content = {}
	content['title'] = "Natural Woman Salon | About Us"
	content['post_data'] = 3
	content['about'] = get_current_about()
	return render_template('user/about.html', **content)

@app.route('/blog')
def blog():
	content = {}
	content['title'] = "Natural Woman Salon | Blog"
	content['post_data'] = 5
	content['blogs'] = get_blog()
	return render_template('user/blog.html', **content)

@app.route('/gallery')
def gallery():
	content = {}
	content['title'] = "Natural Woman Salon | Users"
	content['post_data'] = 4
	content['users'] = get_users()
	return render_template('user/gallery.html', **content)