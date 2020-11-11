"""CRUD operations."""

from model import db, User, Res_cat, Resource, connect_to_db

def create_user(username, password):
    user = User(username=username, password=password)

    db.session.add(user)
    db.session.commit()
    return user

def create_res_cat(res_cat_name):
#TODO: needs to check on create_res_cat fucntion
    res_cat_name = Res_cat(res_cat_name=res_cat_name)
    db.session.add(res_cat)
    db.session.commit()
    return res_cat_name 

if __name__ == '__main__':
    from server import app
    connect_to_db(app)