import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__)

app.config['SECRET_KEY'] = 'WEwillCHANGElater'


##################################
######## --- DATABASE --- ########
######### --- sqlite --- #########
##################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

#________________________________#


##################################
###### --- LOGIN CONFIG --- ######
###### --- LoginManager --- ######
##################################

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

#________________________________#


##################################
####### --- BLUEPRINTS --- #######
######## --- Register --- ########
##################################


from study_app.core.views import core
from study_app.users.views import users
from study_app.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)