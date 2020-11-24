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

def get_category_by_id(id):

    return Category.query.get(id)

# def get_category_by_name(category):

#     return Category.query.get(Category.category==category).first()

def create_resource(resource, contact, location, new_category):
    """Create and return a new resource instance"""
    
    new_resource = Resource(resource=resource, contact=contact, location=location, category=new_category)
    db.session.add(new_resource)
    db.session.commit()  

    return new_resource 

def get_all_resources():
    """Returns all resources"""

    return Resource.query.all()

def get_resource_by_id(id):
    """Return resource by resource id"""

    return Resource.query.filter(Resource.id==id).first()

def get_resources_by_category(category_id):

    return Resource.query.filter(Resource.category_id==category_id).all()
    
def create_bookmark(user_id, resource_id):
    """Create and commit it"""

    new_bookmark = Bookmark(user_id=user_id, resource_id=resource_id)
    db.session.add(new_bookmark)
    db.session.commit()

    return new_bookmark

def get_bookmark_by_id(user_id, resource_id):
    """Return user's bookmark"""

    #return Bookmark.query.filter(Bookmark.id==id).one()

    #return with bookmark class
    return Bookmark.query.filter(Bookmark.user_id==user_id, Bookmark.resource_id==resource_id).first()

def get_bookmarks_by_user_id(user_id):
    """Return user's bookmarks"""

    return Bookmark.query.filter(Bookmark.user_id==user_id).all()

def add_to_bookmark_list(user_id):
    """ Bookmark resource associated with user_id to list"""
    bookmark_list=[]

    user_bookmark = Bookmark.query.filter(user_id==user_id).all() #get all usrr bookmark by user_id

    for bookmark in user_bookmark:
        resource = Bookmark.query.filter(Bookmark.user_id==user.id).one() #get resource from Bookmark
        bookmark_list.append(resource)
    return bookmark_list

def delete_bookmark_by_user_id(user_id):
    
    return db.session.delete(Bookmark.user_id)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)