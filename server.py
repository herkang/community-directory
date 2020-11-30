"""Server for directories"""

from flask import (Flask, render_template, request, flash, session,
                   redirect, abort, jsonify)
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from model import connect_to_db, User, Bookmark, Resource, Category
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

    categories = crud.get_categories()

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
        return redirect('/')

@app.route('/', methods=['POST'])
def login():

    username = request.form.get('username')
    password = request.form.get('password')

    user = crud.get_user_by_username(username) 

    if user:
        if password == user.password:
            login_user(user)
            flash('Welcome back!')
            next_ = request.args.get('next')
            if not is_safe_url(next_):
                return abort(400)
            return redirect(next_ or '/profile' )
        else:
            flash('Wrong password, try again.') 
    else:
        flash("User doesn't exit, please sign up!")
    return redirect('/')
    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/') 

@app.route('/profile')
@login_required
def profile():
    """Return user profile and saved resources"""

    user_id = current_user.get_id()
    bookmarks = crud.get_bookmarks_by_user_id(user_id)

    return render_template('profile.html', bookmarks=bookmarks) #setting it to empty to work

@app.route('/profile', methods=['POST'])
@login_required
def delete_bookmark_in_profile():

    resource_id = request.form.get('bookmark')
    user_id = current_user.get_id()

    bookmarks = crud.get_bookmarks_by_user_id(user_id)
    crud.delete_bookmark_by_user_id(user_id, resource_id)

    return redirect('/profile')

@app.route('/categories') 
def categories():
    """View all categories"""

    categories = crud.get_categories()
    return render_template('all_categories.html', categories=categories)

@app.route('/categories/<category_id>')
def category_resource(category_id):

    category = crud.get_category_by_id(category_id)
    resources = crud.get_resources_by_category(category_id)
    
    return render_template('category.html', category=category, resources=resources)

@app.route('/bookmark', methods=['POST'])
@login_required
def create_bookmark():
   
    resource_id = request.form.get('resource')
    user_id = current_user.get_id()

    bookmark = crud.get_bookmark_by_id(user_id, resource_id)

    if not bookmark:
        new_bookmark = crud.create_bookmark(user_id, resource_id)
        flash('Bookmark created!')

    else:
        flash('Already bookmarked resource')
    return redirect('/categories') #TODO: redirect back to minority page

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
