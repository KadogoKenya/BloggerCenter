from . import db
from app import login_manager
from flask_login import UserMixin
from datetime import datetime



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(1000), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    # blogposts = db.relationship('Blog',backref='author', lazy='dynamic')
    
    @login_manager.user_loader
    def get_user(user_id):
        return User.query.get(user_id)


    def __repr__(self):
        return f'User{self.name}'


class Blog(db.Model):
    __tablename__ = 'blogposts'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    # users_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)


    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    dateposted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('blogposts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"Comment('{self.content}', '{self.dateposted}')"