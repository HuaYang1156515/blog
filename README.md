# 这是blog博客Flask Blog Project


## Project Structure
flaskProject/
├── app/
│   ├── __init__.py         # 应用初始化，定义 Flask 实例、数据库、扩展等
│   ├── models.py          # 数据库模型定义（如 Users、Post、Comment）
│   ├── views.py           # 路由和视图逻辑，使用蓝图（Blueprint）组织
│   ├── forms.py           # 表单定义（如注册、登录、文章表单）
│   └── config.py          # 配置设置（如数据库 URI、密钥等，可选）
├── static/                # 静态文件（如 CSS、JavaScript、图片）
│   ├── css/
│   ├── js/
│   └── images/
├── templates/             # HTML 模板文件
│   ├── base.html         # 基础模板，包含布局和导航
│   ├── home.html         # 主页模板
│   ├── login.html        # 登录页面模板
│   ├── register.html     # 注册页面模板
│   ├── post_list.html    # 文章列表模板
│   ├── post_form.html    # 文章创建/编辑表单模板
│   └── post_detail.html  # 文章详情模板
├── migrations/            # 数据库迁移文件（由 Flask-Migrate 生成）
├── venv/                  # 虚拟环境，隔离项目依赖
├── run.py                 # 启动文件，运行 Flask 应用
├── requirements.txt       # 依赖列表
└── README.md              # 项目说明文档（你正在添加）
