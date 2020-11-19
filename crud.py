"""CRUD operations."""

from model import db, User, Category, Resource, Bookmark, connect_to_db 

"""
For all user related functions, returns will be something like:
 <ID=1 Username=Jet>
"""
def create_user(username, password):
    """Create and return a new user instance"""

    new_user = User(username=username, password=password)
    
    db.session.add(new_user)
    db.session.commit()

    return new_user
def create_login():
    """Create logins"""
    username = User.query.get(username)
    password = User.query.get(password)

def get_user(id):
    """Return user by primary key"""

    return User.query.filter(User.id==id).first()
    
def get_user_by_username(username):
    """Return user by username"""

    return User.query.filter(User.username==username).first()

def create_category(category):
    """Create and return a new category instance"""

    new_category = Category(category=category)

    db.session.add(new_category)
    db.session.commit()

    return new_category

def get_category():
    """Returns all categories in a list"""
        
    return Category.query.all() #will return [<ID=1 Category=Africans>, <ID=2 Category=American Indian>]

def create_resource(resource, contact, location, category):
    """Create and return a new resource instance"""
#TODO: Relationsip not working     
    
    new_resource = Resource(resource=resource, contact=contact, location=location, category=new_category)
    db.session.add(new_resource)
    db.session.commit()  

    return resource #will return 'Confederation of Somali'

""" TODO: Fix relationship for resource-category
BOTH get_all_resources and get_resource_by_id will return:
 [<ID=1 Category ID=None Resource=Confederation of Somali>]
""" 
def get_all_resources():
    """Returns all resources"""
#TODO: Fix querying for all resource

    return Resource.query.all()

def get_resource_by_id(id):
    """Return resource by resource id"""

    return Resource.query.filter(Resource.id==id).first()

def get_resources_by_category(category):

    return Resource.query.filter(Resource.category_id==category).all()
    
def add_bookmark_by_id(user, resource, bookmark):
    """Create and return a bookmark resource instance"""

    new_bookmarks = Bookmarks(user=user, resouce=resource, bookmark=bookmark)
    db.session.add(new_bookmarks)
    db.session.commit()

    return new_bookmarks

def get_bookmarks_by_user_id(user_id):
    """Return user's favorite"""

    return Bookmark.quey.all(user_id)

if __name__ == '__main__':
    from server import app
    connect_to_db(app)