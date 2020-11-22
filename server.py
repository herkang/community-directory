"""Server for directories"""

from flask import (Flask, render_template, request, flash, session,
                   redirect, abort, jsonify)
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

    categories = crud.get_category()

    return render_template('homepage.html', categories=categories)

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
        flash('Username taken! Please create one.')
        return redirect('/signup')
    else:
        crud.create_user(username, password)
        flash('Account created! Please log in.')    
        return redirect('/login')

@app.route('/login')
def login_form():

    return render_template('login.html')

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
            print('***********', user.id, 'in terminal***********')
            
            next_ = request.args.get('next')
          
            if not is_safe_url(next_):
                return abort(400)
            return redirect(next_ or '/profile' )

        else:
            flash('Wrong password, try again.')
            
    else:
        # Tell user that the account doesn't exist
        flash("User doesn't exit, please sign up!")

    return redirect('/')

@app.route('/profile')
@login_required
def profile():
    """Return user profile and saved resources"""

    return render_template('profile.html', bookmarks=[])

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/categories') 

@app.route('/categories', methods=['POST'])
def create_category(category):

    return crud.create_category(category)


@app.route('/categories') #already shown in hompage
def categories():
    """View all categories"""

    categories = crud.get_category()

    return render_template('all_categories.html', categories=categories)

@app.route('/categories/<category_id>')
def category(category_id):

    category = crud.get_category_by_id(category_id)

    return render_template('category.html', category=category)

# @app.route('/categories', methods=['POST'])
# def create_category(category):
#return crud.create_category(category)
#create something similiar for resource 

@app.route('/resources/<category_id>')
def create_resource(resource, contact, location, category_id):

    resource = crud.create_resource(resource, contact, location, category_id)

    return render_template('resource.html', resource=resource, contact=contact, location=location, category_id=category_id)

@app.route('/resources')
def all_resources():
    """View all resources in category"""

    resources = crud.get_all_resources()

    return render_template('all_resources.html', resources=resources)

@app.route('/resources/<resource_id>')
def resource(resource_id):
    """View selected category resource"""

    resource = crud.get_resource_by_id(resource_id)

    return render_template('resources.html', resource=resource)
########## Create Bookmark ##########

@app.route('/profile/<user_id>')
@login_required
def user_resource(user_id):
    """Return user profile and saved resources"""

    bookmarks = crud.get_bookmarks_by_user_id(user_id)

    return render_template('profile.html', bookmarks=bookmarks)

@app.route("/bookmark-info.json")
def bookmark_info():
    """Return info about a bookmark as JSON."""

    # In real life, we would probably get this info
    # from our database
    bookmark = {
        "id": "1",
        "username": "test1",
        "bookmark": ["US", "CA", "MX"]
    }

    return jsonify(bookmark)

@app.route('/resources', methods=['POST'])
@login_required
def add_resource():

    user_resource = request.form.get('bookmark')

    flash('Your resource has been bookmarked!')

    bookmark= crud.add_bookmark(user.id, resource)

    return redirect('/resources') 

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
