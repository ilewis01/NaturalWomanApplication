
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

@app.route('/admin_home', methods=['POST', "GET"])
def admin_home():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		content = admin_home_content()
	else:
		content = admin_home_content()
	return render_template('admin/home.html', **content)	

@app.route('/new_blog')
def new_blog():
	content = new_blog_content()
	return render_template('admin/new_blog.html', **content)

@app.route('/blog_tool')
def blog_tool():
	content = blog_tool_content()
	return render_template('admin/blog_tool.html', **content)

@app.route('/about_tool')
def about_tool():
	content = about_tool_content()
	return render_template('admin/about_tool.html', **content)

@app.route('/product_tool')
def product_tool():
	content = product_tool_content()
	return render_template('admin/product_tool.html', **content)

@app.route('/gallery_tool')
def gallery_tool():
	content = gallery_tool_content()
	return render_template('admin/gallery_tool.html', **content)

@app.route('/company_tool')
def company_tool():
	content = company_tool_content()
	return render_template('admin/company_tool.html', **content)

@app.route('/account_tool')
def account_tool():
	content = account_tool_content()
	return render_template('admin/account_tool.html', **content)

@app.route('/user_tool')
def user_tool():
	content = user_tool_content()
	return render_template('admin/user_tool.html', **content)

@app.route('/email')
def email():
	content = {}
	return render_template('admin/email.html', **content)


















