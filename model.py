""" Models for minority community resource directory """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """ Create users table """

    __tablename__ = 'users'

    id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    username = db.Column(db.String(80),
                        nullable=False, 
                        unique= True)
    password = db.Column(db.String)

    # bookmarks: List[Resource]
    bookmarks = db.relationship(
        "Resource",
        secondary="user_resources",
        backref="users",
    )

    def __repr__(self):
        """ Show user information """

        return f'<ID={self.id} Username={self.username}>'

class Category(db.Model):
    """ Create a resource categories table """

    __tablename__ = 'categories'

    id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    category = db.Column(db.String)

    def __repr__(self):
        """ Show category information """

        return f'<ID={self.id} Category={self.category}>'

class Resource(db.Model):
    """ Create a resources table """

    __tablename__ = 'resources'

    id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    category_id = db.Column(db.Integer,
                            db.ForeignKey('categories.id'))
    resource = db.Column(db.String)
    phone_number = db.Column(db.String)
    location = db.Column(db.String)

    category = db.relationship('Category', backref='resources')

    def __repr__(self):
        """ Show resource information """
    #TODO: Clarication on repr 
    #datatable looks like this: id | category_id | resource | phone_number | location

        return f'<ID={self.id} Category ID={self.category_id} Resource={self.resource}>'

class UserResource(db.Model):
    """ Create a user resources table """

    __tablename__ = 'user_resources'

    id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    user_id = db.Column(db.Integer,
                            db.ForeignKey('users.id'))
    resource_id = db.Column(db.Integer,
                            db.ForeignKey('resources.id'))

    user = db.relationship('User', backref='user_resources')
    resource = db.relationship('Resource', backref='user_resources')

    def __repr__(self):
        """ Show user resource information """

        return f'<User Resource ID={self.id} User ID={self.user_id}, Resource ID={self.resource_id}>'

def connect_to_db(flask_app, db_uri='postgresql:///directory', echo=True):
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