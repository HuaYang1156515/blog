# 这是blog博客Flask Blog Project


## Project Structure
- blog/
  - app/
      - __init__.py           # Application initialization (Flask app, extensions)
      - app.py             # Blog-related routes and views using Blueprints
      - config.py             # Configuration settings (database URI, secret key, etc.)
      - extends.py            # Utility functions or extensions (optional)
      - models.py             # Database models (Users, Posts, Comments)
      - views.py              # Additional routes and views for the app
  - static/
      - css/                  # CSS stylesheets
      - js/                   # JavaScript files
      - images/               # Image assets
  - templates/
      - home.html             # Homepage template
      - login.html            # Login page template
      - register.html         # Registration page template
  - migrations/               # Database migration files (generated by Flask-Migrate)
  - venv/                     # Virtual environment for dependency isolation
  - requirements.txt          # List of project dependencies
  - .gitignore                # Git ignore file for excluding unnecessary files

