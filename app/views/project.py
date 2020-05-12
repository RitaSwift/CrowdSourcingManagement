from flask import Blueprint, render_template, request, redirect, session, url_for
from app.models import db, Project, Requirement
from werkzeug.utils import secure_filename
import datetime
import os

project = Blueprint('project', __name__, template_folder='templates', url_prefix='/post')


@project.route('/')
def test():
    return render_template('basicLayout.html')


# 项目列表
@project.route('/projectList')
@project.route('/projectList?page=<int:page>')
def project_list(page=1):
    # 查询出所有的项目
    all_project = Project.query.all()
    # 根据 URL 中的 page 参数确定显示的项目
    projectList = all_project[(page - 1) * 10: page * 10]
    page_number = len(all_project) // 10 + 1
    # print(page_number)
    return render_template('projectList.html', header="项目列表", projectList=projectList, pageNumber=page_number)


# 创建项目 api
@project.route('/createProject', methods=['POST'])
def create_project():
    if request.method == 'POST':
        new_project = Project(
            pname=request.form.get('name'),
            planguage=request.form.get('language'),
            pfield=request.form.get('field'),
            pclosed_time=request.form.get('closedTime'),
            pcreated_time=datetime.datetime.now(),
            pdescription=request.form.get('description'),
            ppublisher=session.get('uid')
        )
        db.session.add(new_project)
        db.session.commit()
        return 'success'


@project.route('/sendProject', methods=['GET'])
def send_project():
    pid = request.args.get('pid')
    project = Project.query.filter_by(pid=pid).first() or None
    return render_template('sendProject.html', project=project)


@project.route('/editProject', methods=['POST'])
def edit_project():
    pid = request.args.get('pid')
    data = dict(pname=request.form.get('name'),
                planguage=request.form.get('language'),
                pfield=request.form.get('field'),
                pclosed_time=request.form.get('closedTime'),
                pcreated_time=datetime.datetime.now(),
                pdescription=request.form.get('description'),
                ppublisher=session.get('uid'))
    Project.query.filter_by(pid=pid).update(data)
    db.session.commit()
    return 'success'


@project.route('/myProjects')
@project.route('/myProjects?page=<int:page>')
def my_project(page=1):
    username = session.get('uid')
    if username:
        all_project = Project.query.filter_by(ppublisher=username).all()
        projectList = all_project[(page - 1) * 10: page * 10]
        page_number = len(all_project) // 10 + 1
        return render_template('projectList.html', header="我的项目", projectList=projectList, pageNumber=page_number)
    else:
        return redirect(url_for('auth.login'))


@project.route('/project')
def project_detail():
    pid = request.args.get('pid')
    page = int(request.args.get('page')) or 1
    project = Project.query.filter_by(pid=pid).first()
    all_requirement = Requirement.query.filter_by(pid=pid).all()
    pageNumber = len(all_requirement) // 10 + 1
    requirementList = all_requirement[(page-1) * 10: page * 10]
    return render_template('projectPost.html', project=project, requirementList=requirementList, pageNumber=pageNumber, numOfRequirement=len(all_requirement))


@project.route('/sendRequirement')
def send_requirement():
    requirement = Requirement.query.filter_by(rid=request.args.get('rid')).first()
    return render_template('sendRequirement.html', requirement=requirement)


# 创建需求
@project.route('/createRequirement', methods=['POST'])
def create_requirement():
    pid = request.args.get('pid')
    file = request.files.get('file')
    new_requirement = Requirement(
        pid=pid,
        uid=session.get('uid'),
        rname=request.form.get('name'),
        rtype=request.form.get('type'),
        priority=request.form.get('priority'),
        description=request.form.get('description'),
    )
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(os.getcwd(), 'app', 'static', 'upload', filename))
        new_requirement.img = filename
    db.session.add(new_requirement)
    db.session.commit()
    return 'success'


# 编辑需求
@project.route('/editRequirement', methods=['POST'])
def edit_requirement():
    rid = request.args.get('rid')
    file = request.files.get('file')
    filename = None
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(os.getcwd(), 'app', 'static', 'upload', filename))
    Requirement.query.filter_by(rid=rid).update({
        'rname': request.form.get('name'),
        'description': request.form.get('description'),
        'img': filename,
        'rtype': request.form.get('type'),
        'priority': request.form.get('priority')
    })
    db.session.commit()
    return 'success'


@project.route('/searchResult', methods=['GET'])
def search_project():
    title = request.args.get('title')
    search_title = '%' + title + '%'
    search_title = Project.pname.ilike(search_title)
    all_project = Project.query.filter(search_title).all()
    return render_template('projectList.html', header="搜索结果", projectList=all_project, pageNumber=1)
