
from flask import render_template, request
from app import app
from resources.functions import *

@app.route('/')
def index():
	content = index_content()
	return render_template('user/index.html', **content)

@app.route('/home')
def home():
	content = home_content()
	return render_template('user/index.html', **content)

@app.route('/about')
def about():
	content = about_content()
	return render_template('user/about.html', **content)

@app.route('/products')
def products():
	content = product_content()
	return render_template('user/pricing.html', **content)

@app.route('/gallery')
def gallery():
	content = gallery_content()
	content['users'] = get_users()
	return render_template('user/gallery.html', **content)

@app.route('/blog')
def blog():
	content = blog_content()
	return render_template('user/blog.html', **content)

@app.route('/contact')
def contact():
	content = contact_content()
	return render_template('user/contact.html', **content)

