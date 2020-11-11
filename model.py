""" Models for minority community resource directory """

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import PhoneNumber 

db = SQLAlchemy()

class User(db.Model):
    """ Creates an User object """

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    username = db.Column(db.String, nullable=False, unique= True)
    password = db.Column(db.String)

    #db.create_all() 
    #test_user = User(username='herrikang', password='test')
    #db.session.add(test_user)
    #db.session.commit()
    #user = User.query.first()
    #user

    def __repr__(self):
        """ Show user informations """
        
        return f'<User user_id={self.user_id} username={self.username}>'

class Res_cat(db.Model):
    """ Creates a resource category object """

    __tablename__ = 'resource_categories'

    res_cat_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    res_cat_name = db.Column(db.String)

    def __repr__(self):
        """ Show user informations """
        
        return f'<Resource Category res_cat_id={self.res_cat_id} Resource category name res_cat_name={self.res_cat_name}>'

    #db.create_all() 
    #test_resource = Res_cat(res_cat_name='help')
    #db.session.add(test_resource)
    #db.session.commit()
    #res_cat = Res_cat.query.first()
    #res_cat

class Resource(db.Model):
    """ Creates a resource object """

    __tablename__ = 'resources'

    resource_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    res_cat_id = db.Column(db.Integer, 
                            db.ForeignKey('resource_categories.res_cat_id'))
    resource_name = db.Column(db.String)
    phone_number = db.Column(db.String)
    location = db.Column(db.String)
    
    resource = db.relationship('Res_cat', backref='directs')

    #db.create_all() 
    #test_res_cat = Resource(resource=test_resource, resource_name='mental', phone_number='651-234-5423', location='MN')
    #db.session.add(test_res_cat)
    #db.session.commit()
    #test_res_cat = Resource.query.first()
    #test_res_cat

    def __repr__(self):
        """ Show user information """
        
        return f'<Resource resource_id={self.resource_id} resource name resource_name={self.resource_name}>'


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
