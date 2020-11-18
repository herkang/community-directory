""" Server for directories """

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined
app = Flask(__name__)

app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

"""
Cookies are name/string-value pair stored by the client (browser) 
The server tells client to store requests:
Site                Cookie Name                     Value

ubermelon.com      number_visits                 “10”
ubermelon.com      customer_type                 “Enterprise”
localhost:5000     favorite_color                “blue”

The client sends cookies to the server with each request

Cookies (A Conversation)
Browser: I’d like to get the resource /upcoming-events.
Server: Here’s some HTML. Also, please remember this piece of information: favorite_color is "blue".
Browser (stores this somewhere on the computer)
Browser: I’d like to get the resource /event-detail. Also, you told me to remind you that favorite_color is "blue".
Server: Here’s the HTML for that.
Browser: I’d like to get the resource /calendar.jpg. Also, you told me to remind you that favorite_color is "blue".
…"""

"""
Methods: GET and POST
GET vs POST
GET: passes arguments via the URL

If you know the arguments, you can change the URL
Many websites operate this way
No side effect of the request (e.g. refreshing the page)

POST: from additional data in request (like a dictionary!)
Used for requests with side effects (e.g. saving data to a database)
“Are you sure you want to resubmit?”
"""


@app.route('/')
def homepage():
    """ View homepage """

    return render_template('homepage.html')
   
@app.route('/user', methods=['POST'])
def register_user():
    """ Create a new user """

    username = request.form.get['username']
    password = request.form.get['password']

    user = crud.get_user_by_username(username)

    if user:
        flash('Username already taken')
    else:
        crud.create_user(username, password)
        flash('Account created! Please log in')
    return redirect('/')

@app.route('/profile')
def profile():
    """ Return user profile """

    return render_template('profile.html')

@app.route('/login', methods=['POST'])
def login():
    """ Create user name """

    return render_template('login.html')

    username = request.form.get('username')
    password = request.form.get('password')

    if user:
        session['user_id'] = users.id
        return redirect('/profile')
    else:
        flash('Username or password is incorrect')
        return redirect('/login')

@app.route('/categories')
def categories():
    """ View all categories """

    categories = crud.get_category()

    return render_template('category_details.html', categories=categories)

@app.route('/resources')
def resources():
    """ View all resources """

    resources = crud.get_resource()

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
