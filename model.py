""" Models for minority community resource directory """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """ Create users table """

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    username = db.Column(db.String,
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

    return f'<Id user_id={self.user_id} username={self.username} bookmarks ={seld.bookmarks}>'

class Category(db.Model):
    """ Create a resource categories table """

    __tablename__ = 'categories'

    category_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    category = db.Column(db.String)

    def __repr__(self):
        """ Show category information """

    return f'<Id category_id={self.category_id} Category category={self.category}>'

class Resource(db.Model):
    """ Create a resources table """

    __tablename__ = 'resources'

    resource_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    category_id = db.Column(db.Integer,
                            db.ForeignKey('categories.category_id'))
    resource = db.Column(db.String)
    phone_number = db.Column(db.String)
    location = db.Column(db.String)

    category = db.relationship('Category', backref='resources')

    def __repr__(self):
        """ Show resource information """

    return f'<Id resource_id={self.resource_id} Category category={self.category} Resource resource={self.resource}>'

class UserResource(db.Model):
    """ Create a user resources table """

    __tablename__ = 'user_resources'

    user_res_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    user_id = db.Column(db.Integer,
                            db.ForeignKey('users.user_id'))
    resource_id = db.Column(db.Integer,
                            db.ForeignKey('resources.resource_id'))

    user_id = db.relationship('User', backref='user_resources')
    user_resource = db.relationship('Resource', backref='user_resources')

    def __repr__(self):
        """ Show user resource information """

    return f'<user_id={self.user_id}, resource_id={self.resource_id} user_resource={self.user_resource}>'

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
