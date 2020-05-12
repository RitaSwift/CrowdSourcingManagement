from flask import Blueprint, request, render_template
from app.models import Project, db
import datetime

manager = Blueprint('projectManagement', __name__, url_prefix='/projectManagement')


@manager.route('/')
def manage_project():
    pid = request.args.get('pid')
    project = Project.query.filter_by(pid=pid).first()
    return render_template('projectManagement.html', project=project)


@manager.route('/stopCollection')
def stop_collection():
    pid = request.args.get('pid')
    if pid:
        Project.query.filter_by(pid=pid).update({'pstate': '0'})
        db.session.commit()
        return 'success'


@manager.route('/startCollection')
def start_collection():
    pid = request.args.get('pid')
    new_close_time = request.args.get('newClosedTime')
    if datetime.datetime.strptime(new_close_time, '%Y-%m-%d') < datetime.datetime.now():
        return 'fail'
    else:
        Project.query.filter_by(pid=pid).update({
            'pstate': '1',
            'pclosed_time': new_close_time
        })
        db.session.commit()
        return 'success'
