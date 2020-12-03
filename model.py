"""Models for minority community resource directory"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    """Create users table"""

    __tablename__ = 'users'

    id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    username = db.Column(db.String(80),
                        nullable=False, 
                        unique= True)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        """Show user information"""

        return f'<ID={self.id} Username={self.username}>'
        
    def get_id(self):
        """Override flask_login.UserMixin."""
        
        return str(self.id)

class Category(db.Model):
    """Create a resource categories table"""

    __tablename__ = 'categories'

    id = db.Column(db.String,
                        primary_key=True,
                        unique=True)

    def __repr__(self):
        """Show category information"""

        return f'<Category id={self.id}>'

class Resource(db.Model):
    """Create a resources table"""

    __tablename__ = 'resources'

    id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    category_id = db.Column(db.String,
                            db.ForeignKey('categories.id'))
    org_name = db.Column(db.String)
    contact = db.Column(db.String)
    address = db.Column(db.String)
    location = db.Column(db.String)
    
    category = db.relationship('Category', backref='resources')

    def __repr__(self):
        """Show resource information"""

        return f'<ID={self.id} Category ID={self.category_id} org_name={self.org_name}>'

class Bookmark(db.Model):
    """Create a user resources table"""

    __tablename__ = 'bookmarks'

    id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    user_id = db.Column(db.Integer,
                            db.ForeignKey('users.id'))
    resource_id = db.Column(db.Integer,
                            db.ForeignKey('resources.id'))

    user = db.relationship('User', backref='bookmarks')
    resource = db.relationship('Resource', backref='bookmarks')

    def __repr__(self):
        """Show user resource information"""

        return f'<User_Resource ID={self.id} User ID={self.user_id}, Resource ID={self.resource_id}>'


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