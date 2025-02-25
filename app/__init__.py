from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you_can_never_guess'  # 建议使用 secrets.token_hex(16) 或环境变量
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:abcd1234@localhost/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)  # 用户登录管理
login_manager.login_view = 'auth.login'  # 修正为蓝图端点 'auth.login'
csrf = CSRFProtect(app)  # CSRF 保护

# 配置登录管理器
@login_manager.user_loader
def load_user(user_id):
    from .models import Users  # 延迟导入，避免循环导入
    return Users.query.get(int(user_id))

# 导入并注册蓝图（修正导入路径）
from .views import auth_bp
app.register_blueprint(auth_bp)

from .models import Users  # 用户模型