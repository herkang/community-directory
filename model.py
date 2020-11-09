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

    def __repr__(self):
        """ Show user informations """
        
        return f'<User user_id={self.user_id} username={self.username}>'

class Resource_category(db.Model):
    """ Creates a resource category object """

    __tablename__ = 'resource_categories'

    resource_category_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    resource_category_name = db.Column(db.String)

    def __repr__(self):
        """ Show user informations """
        
        return f'<Resource Category resource_category_id={self.resource_category_id} Resource category name resource_category_name={self.resource_category_name}>'

class Resource(db.Model):
    """ Creates a resource object """

    __tablename__ = 'resources'

    resource_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    resource_category_id = db.Column(db.Integer, 
                            db.ForeignKey('users.user_id'))
    resource_name = db.Column(db.String)
    # To do, add url to resource_name 
    # https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#module-sqlalchemy_utils.types.phone_number

    service = db.Column(db.String)
    _phone_number = db.Column(db.Unicode(20))
    country_code = db.Column(db.Unicode(8))

    phone_number = db.orm.composite(
        PhoneNumber, 
        _phone_number, 
        country_code
    )

#Testing 
#user = User(phone_number=PhoneNumber('0401234567', 'FI'))

#user.phone_number.e164  # u'+358401234567'
#user.phone_number.international  # u'+358 40 1234567'
#user.phone_number.national  # u'040 1234567'
#user.country_code  # 'FI'
    location = db.Column(db.String)
    #To do, figure out how to put location in from txt file
    
    resource = db.relationship('Resource_category', backref='resource_categories')

    def __repr__(self):
        """ Show user information """
        
        return f'<Resource resource_id={self.resource_id} resource name resource_name={self.resource_name}>'

if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
