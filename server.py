""" Server for directories """

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

app = Flask(__name__)


@app.route('/')
def homepage():
    """ View homepage """

    return render_template('homepage.html')

@app.route('/users')
def users():
    """ View user """

    return render_template('user_details.html')

@app.route('/categories')
def categories():
    """ View categories """

    return render_template('category_details.html')

@app.
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
