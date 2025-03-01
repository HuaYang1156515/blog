from app import db

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class Posts(db.Model):
    post_id =db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(60),nullable=False)
    content=db.Column(db.Text, nullable=False)

class Comments(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    content=db.Column(db.Text, nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('users.user_id'),nullable=False)
    post_id=db.Column(db.Integer,db.ForeignKey('posts.post_id'),nullable=False)
    created_time=db.Column(db.DateTime,nullable=False)
    updated_time=db.Column(db.DateTime,nullable=False)
