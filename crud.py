"""CRUD operations."""

from model import db, User, Category, Resource, UserResource, connect_to_db

def create_user(username, password):
    """ Creates and return new user """

    user = User(username=username, password=password)
    
    db.session.add(user)
    db.session.commit()

    return user

def get_user(user_id):
    """ Returns user by primary key """

    return User.query.get(user_id)

def get_user_by_username(username):
    """ Return a user by username """

    return User.query.filter(User.username == username).first()


def creates_category(category_name):
    """ Creates a category object """

    category = Category(category_name=category_name)
    db.session.add(category)
    db.session.commit()

    return category

def get_category(category_id):
    """ Returns a resource category by id """ 

    category_instance = Category.query.get(category_id)

    return category_instance

# def creates_resource(category_instance, resource_name, phone_number, location):
#     """ Creates a resource object"""
#     #TODO: Fix TypeError: 'res_cat' is an invalid keyword argument for Resource

#     resource = Resource(category_instance=category_instance, resource_name=resource_name, phone_number=phone_number, location=location)
#     db.session.add(resource)
#     db.session.commit()  

#     return resource

# def create_user_resource(saved_resource):
#     """ Creates user's resource object """
#     #TODO: Fix NameError: name 'resource' is not defined

#     user_resource = User_resource(saved_resource=resource)
#     db.session.add(saved_resource)
#     db.session.commit()

#     return user_resource

if __name__ == '__main__':
    from server import app
    connect_to_db(app)