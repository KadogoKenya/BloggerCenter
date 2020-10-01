from . import db

from app import login_manager
from flask_login import UserMixin
from datetime import datetime



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(255), unique=True, nullable=False)
    
    email = db.Column(db.String(255), unique=True, nullable=False)
    
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())


    password = db.Column(db.String(255))
    
    @login_manager.user_loader
    def get_user(user_id):
        return User.query.get(user_id)

    def __repr__(self):
        return f'User{self.name}'

class blogposts(db.Model):
    __tablename__ = 'blogposts'
    id = db.Column(db.Integer, primary_key = True)

    title = db.Column(db.String(255),nullable=False)
    
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)

    blogpost_id = db.Column(db.Integer, db.ForeignKey('blogposts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    dateposted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def __repr__(self):
        return f"Comment('{self.content}', '{self.dateposted}')"

class Quote:
    """
    Blueprint class for quotes consumed from API

    """
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote