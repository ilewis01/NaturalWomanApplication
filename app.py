
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://redd:Oxley.5610@localhost:5433/natural_woman_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# print("Running import test...")

from resources.views import *
from resources.functions import *
from resources.models import *

init_database()
# product = fetch_product(1)
# print("Product: " + str(product.service))

if __name__ == '__main__':
    app.debug = True
    app.run()