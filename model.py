""" Models for minority community resource directory """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """ Creates an users table """

    __tablename__ = 'users'cd 

    user_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    username = db.Column(db.String, nullable=False, unique= True)
    password = db.Column(db.String)

    # bookmarks: List[Resource]
    bookmarks = db.relationship(
        "Resource",
        secondary="user_resources",
        backref="users",
    )

    def add_bookmark_by_id(self, resource_id):
    """ Creates an instance of resource """

    # get resource
        self.bookmarks.append(resource)

class Category(db.Model):
    """ Creates a resource categories table """

    __tablename__ = 'categories'

    category_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    category_name = db.Column(db.String)

class Resource(db.Model):
    """ Creates a resources table """

    __tablename__ = 'resources'

    resource_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    category_id = db.Column(db.Integer,
                            db.ForeignKey('categories.category_id'))
    resource_name = db.Column(db.String)
    phone_number = db.Column(db.String)
    location = db.Column(db.String)

    category = db.relationship('Category', backref='resources')

class UserResource(db.Model):
    """ Creates a user resources table """

    __tablename__ = 'user_resources'

    user_res_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    user_id = db.Column(db.Integer,
                            db.ForeignKey('users.user_id'))
    resource_id = db.Column(db.Integer,
                            db.ForeignKey('resources.resource_id'))

def connect_to_db(flask_app, db_uri='postgresql:///directs', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
