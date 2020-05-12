from flask import Flask
from app.views import auth, project, projectManagement, requirementManage
from app.config import Dev
from app.models import db
from app.data import data_init
import pymysql

def create_app():
    pymysql.install_as_MySQLdb()
    app = Flask(__name__)
    app.register_blueprint(auth.auth)
    app.register_blueprint(project.project)
    app.register_blueprint(projectManagement.manager)
    app.register_blueprint(requirementManage.requirementManage)
    app.config.from_object(Dev)
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    data_init()
    return app
