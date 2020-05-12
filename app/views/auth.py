from flask import Blueprint, render_template, request, redirect, session, url_for
from app.models import db, User

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # 从 POST 的表单中获取用户的登录数据
        username = request.form.get('uid')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        # 判断账号密码是否与数据库中一致
        if user is not None and user.password == password:
            session['uid'] = user.username
            return 'success'
        else:
            return 'fail'
    else:
        return render_template('login.html')


@auth.route('/register', methods=['post', 'get'])
def register():
    if request.method == 'POST':
        username = request.form.get('uid'),
        # 从前端 POST 的数据中获取用户的注册信息
        new_user = User(
            username=username,
            password=request.form.get('password'),
            phone=request.form.get('telephone'),
            email=request.form.get('email'),
            occupation=request.form.get('occupation'),
            introduction=request.form.get('introduction')
        )
        # 判断用户注册的 ID 是否已经存在
        if User.query.filter_by(username=username).first() is not None:
            return 'uid_existed'
        else:
            db.session.add(new_user)
            db.session.commit()
            return 'success'
    else:
        return render_template('register.html')


@auth.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return 'logout'


@auth.route('/userInfo')
@auth.route('/userInfo/changePassword')
def user_info():
    username = session.get('uid')
    if username:
        user = User.query.filter_by(username=username).first()
        return render_template('userinfo.html', account=user)
    else:
        return redirect(url_for('auth.login'))


@auth.route('/userInfo/modify', methods=['POST'])
def modify_user_info():

    user = User.query.filter_by(username=session['uid']).first()
    new_username = request.form.get('username')
    new_user = User.query.filter_by(username=new_username).first()
    if new_user is not None and new_user != user:
        return 'uid_existed'
    if user is not None:
        User.query.filter_by(username=session['uid']).update({
            'username': new_username,
            'phone': request.form.get('phone'),
            'occupation': request.form.get('occupation'),
            'introduction': request.form.get('introduction')
        })
        db.session.commit()
        return 'success'


@auth.route('/userInfo/doChangePassword', methods=['POST'])
def modify_password():
    user = User.query.filter_by(username=session['uid']).first
    if user.password != request.form.get('oldPassword'):
        return 'fail'
    else:
        User.query.filter_by(username=session['uid']).update({
            'password': request.form.get('newPassword')
        })
        return 'success'


@auth.route('/')
@auth.route('/home')
def home():
    return redirect(url_for('project.project_list'))
