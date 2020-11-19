"""Server for directories"""

from flask import (Flask, render_template, request, flash, session,
                   redirect, abort)
from flask_login import LoginManager, login_user, login_required, logout_user
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
login_manager = LoginManager()

app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

login_manager.init_app(app)

def is_safe_url(url):
    """TODO: implement later."""
    
    return True

@login_manager.user_loader
def load_user(user_id):

    return crud.get_user(int(user_id))

@app.route('/')
def homepage():
    """View homepage"""

    return render_template('homepage.html')

@app.route('/signup')
def signup_form():
    """View sign up form"""

    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def register_user():
    """Create a new user"""
    
    username = request.form.get('username')
    password = request.form.get('password')

    user = crud.get_user_by_username(username)

    if user:
        flash('Username already taken')
    else:
        crud.create_user(username, password)
        flash('Account created! Please log in')
    return redirect('/login')

@app.route('/login', methods=['POST'])
def login():

    username = request.form.get('username')
    password = request.form.get('password')

    user = crud.get_user_by_username(username)

    if user:
        # Check password, if password matches, call login_user
        if password == user.password:
            login_user(user)
            
            flash('Welcome back!')
            
            next_ = request.args.get('next')
            if not is_safe_url(next_):
                return abort(400)

            return redirect(next_ or '/profile')
        else:
            flash('Wrong password')
    else:
        # Tell user that the account doesn't exist
        flash("User doesn't exit")

    return redirect('/')

@app.route('/profile')
@login_required
def profile():
    """Return user profile"""

    return render_template('profile.html')

# @app.route('/resources')
# @login_required
# def resources():
#     """Return resources in categories"""

#     return render_template('resources.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

# @app.route('/login', methods=['POST'])
# def login():
#     """ Create user name """

#     return render_template('login.html')

#     username = request.form.get('username')
#     password = request.form.get('password')

#     if user:
#         session['user_id'] = users.id
#         return redirect('/profile')
#     else:
#         flash('Username or password is incorrect')
#         return redirect('/login')

@app.route('/categories')
def categories():
    """View all categories"""

    categories = crud.get_category()

    return render_template('all_categories.html', categories=categories)

@app.route('/resources')
def resources():
    """View all resources"""
#TODO: TypeError: get_resource_by_id() missing 1 required positional argument: 'id'
#Connect category and resources
    resources = crud.get_all_resources()

    return render_template('all_resources.html', resources=resources)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
