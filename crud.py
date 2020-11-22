"""CRUD operations."""

from model import db, User, Category, Resource, connect_to_db 

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

def get_category_by_id(id):

    return Category.query.get(id)

def get_category_by_name(category):

    return Category.query.get(Category.category==category).first()

def create_resource(resource, contact, location, category):
    """Create and return a new resource instance"""
    
    new_resource = Resource(resource=resource, contact=contact, location=location, category=category)
    db.session.add(new_resource)
    db.session.commit()  

    return new_resource 

def get_all_resources():
    """Returns all resources"""

    return Resource.query.all()

def get_resource_by_id(id):
    """Return resource by resource id"""

    return Resource.query.filter(Resource.id==id).first()

def get_resources_by_category(category):

    return Resource.query.filter(Resource.category_id==category).all()
    
def add_bookmark(user_id, resource_id):
    """Create and return a bookmark resource instance"""

    new_bookmark = Bookmark(user_id=user_id, resource_id=resource_id)
    db.session.add(new_bookmark)
    db.session.commit()

    return new_bookmark

def create_bookmark_list(id):

    bookmark_list=[]

    for bookmark in user_resource:
        resource = User.query.filter(User.id==id).all()
        bookmark_list.append(resource)
    return bookmark_list

def get_bookmarks_by_user_id(id):
    """Return user's favorite"""

    return User.query.filter(User.id==id).all()

def delete_bookmark_by_id(bookmark_id):
    
    return db.session.delete(bookmark_id)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)