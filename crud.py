"""CRUD operations."""

from model import db, User, Res_cat, Resource, User_resource, connect_to_db

def create_user(username, password):
    """ Creates a user object """

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return user

def get_user(user_id):
    """ Returns user's information by user's id """

    user = User.query.get(user_id)

    return user

def creates_res_cat(res_cat_name):
    """ Creates a resource category object """

    res_cat_name = Res_cat(res_cat_name=res_cat_name)
    db.session.add(res_cat_name)
    db.session.commit()

    return res_cat_name 

def get_res_cat(res_cat_id):
    """ Returns a resource category by id""" 

    res_cat = Res_cat.query.get(res_cat_id)

    return res_cat

def creates_resource(res_cat, resource_name, phone_number, location):
    """ Creates a resource object"""
    #TODO: Fix TypeError: 'res_cat' is an invalid keyword argument for Resource

    resource = Resource(res_cat=res_cat, resource_name=resource_name, phone_number=phone_number, location=location)
    db.session.add(resource)
    db.session.commit()  

    return resource

def create_user_resource(saved_resource):
    """ Creates user's resource object """
    #TODO: Fix NameError: name 'resource' is not defined

    user_resource = User_resource(saved_resource=resource)
    db.session.add(saved_resource)
    db.session.commit()

    return user_resource

if __name__ == '__main__':
    from server import app
    connect_to_db(app)