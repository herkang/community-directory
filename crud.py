"""CRUD operations."""

from model import db, User, Category, Resource, UserResource, connect_to_db

def create_user(username, password):
    """ Creates and return new user """

    user = User(username=username, password=password)
    
    db.session.add(user)
    db.session.commit()

    return user

def get_user():
    """ Return user by primary key """

    return User.query.get(user_id)

def get_user_by_username(username):
    """ Return user by username """

    return User.query.filter(User.username == username).first()


def create_category(category):
    """ Create a category instance """

    category = Category(category=category)
    db.session.add(category)
    db.session.commit()

    return category

def get_category():
    """ Return resource categories """ 

    return Category.query.all()

def create_resource(category, resource, phone_number, location):
    """ Creates a resource object"""
   
    resource = Resource(category=category, resource=resource, phone_number=phone_number, location=location)
    db.session.add(resource)
    db.session.commit()  

    return resource

def get_resource():
    """ Return all resources """

    return Resource.query.all()

def add_bookmark_by_id(resource_id):
    """ Creates an instance of bookmark resource"""

    bookmarks = User_resource(resource_id=resource_id)
    db.session.add(bookmarks)
    db.session.commit()

    return bookmarks

def get_bookmarK_by_user_id(user_id):
    """ Return user's favorite """

    #TODO: Get resource and create a list for favorites


if __name__ == '__main__':
    from server import app
    connect_to_db(app)