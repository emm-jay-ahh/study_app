from study_app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


### USER class
class User(db.Model,UserMixin):
    
    ### TABLE NAME: users
    __tablename__ = 'users'

    ### COLUMNS
    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(64), nullable=False, default='default_profile.png')
    email = db.Column(db.String(60), unique=True, index=True)
    username = db.Column(db.String(40), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    book_posts = db.relationship('BookPost', backref='author', lazy=True)
    video_posts = db.relationship('VideoPost', backref='author', lazy=True)
    cert_posts = db.relationship('CertPost', backref='author', lazy=True)


    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Username {self.username}"


### BOOKPOST class
class BookPost(db.Model):

    users = db.relationship(User)

    id = db.Column(db.Integer,primary_key=True)

    #CONNECT TO USERS id above
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)

    # PUBLISH DATE - Change to another date type later on
    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    
    # TITLE OF BOOK  (BLOG TITEL)
    title = db.Column(db.String(140),nullable=False)
    # BLOG POST  - CHANGE
    text = db.Column(db.Text,nullable=False)

    def __init__(self,title,text,user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    # FOR DEBUG PURPOSES
    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} --- {self.title}"


class VideoPost(db.Model):

    users = db.relationship(User)

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)

    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    title = db.Column(db.String(140),nullable=False)
    text = db.Column(db.Text,nullable=False)

    def __init__(self,title,text,user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} --- {self.title}"


class CertPost(db.Model):

    users = db.relationship(User)

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)

    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    title = db.Column(db.String(140),nullable=False)
    text = db.Column(db.Text,nullable=False)

    def __init__(self,title,text,user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} --- {self.title}"
