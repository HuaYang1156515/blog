'''
# from flask import Blueprint, render_template, request, redirect, url_for
# from flask_login import login_required
# from app.models import Users
# auth_bp=Blueprint('auth',__name__)
#
# @auth_bp.route('/')  # 添加根路由
# def index():
#     return redirect(url_for('auth.home'))
# @auth_bp.route('/home')
# def home():
#     return render_template('home.html')
# @auth_bp.route('/login',methods=['get','post'])
# def login():
#     if request.method=='get':
#        return render_template('login.html')
#     elif request.method=='post':
#         password=request.form.get('password')
#         username=request.form.get('username')
#         user=Users.query.filter_by(username=username,password=password).first()
#         if user:
#             response=redirect('/login')
#             response.set_cookie('user_id',str(user.id),max_age=3600)
#             return response
#         else:
#             return "fail"
#
#
'''

''' 
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, LoginManager
from app.models import Users  # 改为 Users
from app import db,login_manager  # 确保导入数据库实例

auth_bp = Blueprint('auth', __name__)

# # 初始化 LoginManager（确保在 app/__init__.py 中已配置）
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))  # 改为 Users

@auth_bp.route('/')
def index():
    return "hello world!"

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
        user = Users.query.filter_by(username=username).first()  # 改为 Users
        if user and user.check_password(password):
            login_user(user)
            flash('登录成功！', 'success')
            return redirect(url_for('auth.home'))
        else:
            flash('登录失败，请检查用户名或密码。', 'error')
            return render_template('login.html')
'''
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required
from app.models import Users
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

@auth_bp.route('logout')
def logout():
    pass
@auth_bp.route('/register',methods=['get','post'])
def register():
    pass
@auth_bp.route('/comment',methods=['get','post'])
def comment():
    pass