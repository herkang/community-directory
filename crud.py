"""CRUD operations."""

from model import db, User, Res_cat, Resource, connect_to_db

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

if __name__ == '__main__':
    from server import app
    connect_to_db(app)