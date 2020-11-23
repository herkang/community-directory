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
    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/') 

@app.route('/profile')
@login_required
def profile():
    """Return user profile and saved resources"""

    return render_template('profile.html', bookmarks=[]) #setting it to empty to work

# @app.route('/profile', methods=['POST'])
# @login_required
# def add_bookmark(user_id):
#     """Return create resource by user_id"""

#     return crud.add_to_bookmark_list(user_id)

# @app.route('/profile/<user_id>')
# @login_required
# def get_user_resource(user_id):
#     """Returning bookmarks by id to profile template"""

#     bookmarks = crud.get_bookmarks_by_user_id(user_id)

#     return render_template('profile.html', bookmarks=bookmarks)

# @app.route('/profile/<user_id>')
# @login_required
# def delete_user_resource(user_id):
#     """Delecting bookmarks by user id"""

#     return crud.delete_bookmark_by_user_id(user_id)

@app.route('/categories', methods=['POST'])
def create_category(category):

    return crud.create_category(category) #create data in server terminal

@app.route('/categories') 
def categories():
    """View all categories"""
    # categories = crud.get_category()
    # return render_template('all_categories.html', categories=categories)
    return redirect('/') #redirect to homepage

# @app.route('/categories/<category_id>')
# def category(category_id):

#     category = crud.get_category_by_id(category_id)

#     return render_template('category.html', category=category)

@app.route('/categories/<category_id>')
def category_resource(category_id):

    category = crud.get_category_by_id(category_id)
    resources = crud.get_resources_by_category(category_id)
    return render_template('category.html', category=category, resources=resources)

#create on server side
# @app.route('/resources', methods=['POST'])
# def create_resource(resource, contact, location, category):

#     return crud.create_resource(resource, contact, location, category)

# @app.route('/resources')
# def all_resources():
#     """View all resources in category"""

#     resources = crud.get_all_resources()

#     return render_template('all_resources.html', resources=resources)

# @app.route('/resources', methods=['POST']) #Method Not Allowed
# @login_required
# def add_resource():

#     bookmarks = request.form.get('bookmark')

#     flash('Your resource has been bookmarked!')

#     # return redirect('/resources')
#     #or add eventlister or ajax drop down?
#     #or call crud.add_to_bookmark_list
    
#     return render_template('/profile.html', bookmarks=bookmarks)

# @app.route('/resources/<category_id>')
# def resource(category_id):
#     """View selected category resource"""

#     resource = crud.get_resource_by_id(category_id)

#     return render_template('resources.html', resource=resource)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
