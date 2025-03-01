from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required
from app.models import Users, Posts, Comments
from app import db, login_manager  # 确保导入 login_manager

auth_bp = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@auth_bp.route('/')
def index():
    return render_template('home.html')

@auth_bp.route('/home')
@login_required
def home():
    return render_template('home.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
        return render_template('login.html')

  elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = Users.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('登录成功！', 'success')
            return redirect(url_for('auth.home'))
        else:
            flash('登录失败，请检查用户名或密码。', 'error')
            return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    pass
@auth_bp.route('/register',methods=['get','post'])
def register():
    pass

@auth_bp.route('/comment/<int:post_id>',methods=['get','post'])
def comment(post_id):
    post=Posts.query.get_or_404(post_id)
    if request.method=='get':
        return render_template('comment.html',post=post)
    elif request.method=='post':
        content=request.form.get('content')
        if not content:
            flash('评论不能为空','error')
            return render_template('comment',post=post)
        new_comment=Comments(content=content,post_id=post.id)
        db.session.add(new_comment)
        db.session.commit()

        flash('评论发布成功','success!')
        return redirect(url_for('auth.post_detail',post_id=post.id))







