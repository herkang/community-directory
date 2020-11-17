"""CRUD operations."""

from model import db, User, Category, Resource, UserResource, connect_to_db

"""
For all user related functions, returns will be something like:
 <ID=1 Username=Jet>
"""
def create_user(username, password):
    """ Create and return a new user instance """

    new_user = User(username=username, password=password)
    
    db.session.add(new_user)
    db.session.commit()

    return new_user

def get_user(id):
    """ Return user by primary key """

    return User.query.filter(User.id==id).first()
    
def get_user_by_username(username):
    """ Return user by username """

    return User.query.filter(User.username==username).first()

def create_category(category):
    """ Create and return a new category instance """

    new_category = Category(category=category)

    db.session.add(new_category)
    db.session.commit()

    return new_category

def get_category():
    """ Returns all categories in a list:
        [<ID=1 Category=Africans>, <ID=2 Category=American Indian>]
    """ 

    return Category.query.all()

#TODO: Add category relationship, resource functions not properly working


def create_resource(resource, phone_number, location):
    """ Create and return a new resource instance 
    Will return: 'Confederation of Somali'
    """
    
    new_resource = Resource(resource=resource, phone_number=phone_number, location=location)
    db.session.add(new_resource)
    db.session.commit()  

    return resource

""" 
BOTH get_all_resources and get_resource_by_id will return:
 [<ID=1 Category ID=None Resource=Confederation of Somali>]
"""

def get_all_resources():
    """ Returns all resources """

    return Resource.query.all()

def get_resource_by_id(id):
    """ Return resource by resource id """

    return Resource.query.filter(Resource.id==id).first()

# def add_bookmark_by_id(resource_id):
#     """ Create and return a bookmark resource instance """

#     new_bookmarks = UserResource(resource_id=resource_id)
#     db.session.add(new_bookmarks)
#     db.session.commit()

#     return new_bookmarks

# def get_bookmarks_by_user_id(user_id):
#     """ Return user's favorite """

if __name__ == '__main__':
    from server import app
    connect_to_db(app)