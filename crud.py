"""CRUD operations."""

from model import db, User, Category, Resource, Bookmark, connect_to_db 

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

def get_categories():
    """Returns all categories in a list"""
        
    return Category.query.all()

# def get_category_id_by_name(category):

    # return Category.query(Category).get(category)
    # return Category.query(Category.id).filter_by(category=category).first()

def get_category_by_id(category_id):

    return Category.query.get(category_id)

def get_category_by_name(category):

    return Category.query.filter(category==category).all()

def create_resource(org_name, contact, address, location, category_id):
    """Create and return a new resource instance"""
    
    new_resource = Resource(org_name=org_name, contact=contact, address=address, location=location, category_id=category_id)
    db.session.add(new_resource)
    db.session.commit()  

    return new_resource 

def get_all_resources():
    """Returns all resources"""

    return Resource.query.all()

def get_resource_by_id(id):
    """Return resource by resource id"""

    return Resource.query.filter(Resource.id==id).first()

def get_resource_by_name(org_name):

    return Resource.query.filter_by(org_name=org_name).all()

def get_resources_by_category(category_id):

    return Resource.query.filter_by(category_id=category_id).all()
    
def create_bookmark(user_id, resource_id):
    """Create and commit it"""

    new_bookmark = Bookmark(user_id=user_id, resource_id=resource_id)
    db.session.add(new_bookmark)
    db.session.commit()

    return new_bookmark

def get_bookmark_by_id(user_id, resource_id):
    """Return user's bookmark"""

    return Bookmark.query.filter_by(user_id=user_id, resource_id=resource_id).all()

def get_bookmarks_by_user_id(user_id):
    """Return user's bookmarks"""

    return Bookmark.query.filter_by(user_id=user_id).all()

def delete_bookmark_by_user_id(user_id, resource_id):

    bookmark = Bookmark.query.filter_by(user_id=user_id, resource_id=resource_id).first()
    
    db.session.delete(bookmark)
    db.session.commit()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)