""" Server for directories """

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined
app = Flask(__name__)

app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """ View homepage """

    return render_template('homepage.html')

@app.route('/user')
def users():
    """ View user """

    return render_template('user_details.html')
    
@app.route('/register', methods=['POST'])
def register_user():
    username = request.form['username']
    password = request.form['password']

    user = get_user_by_username(username):
    if user:
        return 'Username is already taken'
        else:
            create_user(username, password)
            return redirect('/')

@app.route('/categories')
def categories():
    """ View all categories """

    categories = crud.get_category()

    return render_template('category_details.html', categories=categories)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
