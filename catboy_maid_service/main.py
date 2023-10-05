## main.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from orangehrm import OrangeHRM
from mautic import Mautic
from config import Config
import os

# Initialize Flask
app = Flask(__name__)

# Load configuration
config = Config()

# Load configuration values from environment variables
for package in ['FLASK', 'SQLALCHEMY', 'ORANGEHRM', 'MAUTIC']:
    for key in config.get(package):
        env_var = f'{package}_{key}'.upper()
        if env_var in os.environ:
            config.set(package, key, os.environ[env_var])

# Configure Flask
app.config.from_mapping(config.get('FLASK'))

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Configure SQLAlchemy
app.config.from_mapping(config.get('SQLALCHEMY'))

# Initialize OrangeHRM
orangehrm = OrangeHRM(config.get('ORANGEHRM'))

# Initialize Mautic
mautic = Mautic(config.get('MAUTIC'))

# Import and register routes
from . import views
app.register_blueprint(views.bp)

if __name__ == "__main__":
    app.run()
