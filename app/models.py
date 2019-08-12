from . import db
from . import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(post_id=id).all()
        
        return comments
   
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self,password):
        print(self.password_hash)
        print(password)
        return check_password_hash(self.password_hash,password)
    
    def __repr__(self):
        return f'User {self.username}'
    
class Post(db.Model):
    
    __tablename__ = 'posts'


    
    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_posts(cls):
        posts = Post.query.order_by('id').all()
        return posts

    @classmethod
    def get_post(cls,id):
        post = Post.query.filter_by(id=id).first()

        return post 
    
class Comment(db.Model):
    
    __tablename__ = 'comments'

 
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def delete_comment(cls,id):
        comment = Comment.query.filter_by(id=id).delete()

        return comment 

class Quote:
    '''
    Quote class to define Quote Objects
    '''

    def __init__(self, author, quote):
        self.author = author
        self.quote = quote