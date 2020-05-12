from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


# 用户表
class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'mysql_engine': 'InnoDB'}  # 支持事务操作和外键
    uid = db.Column(db.Integer, doc='UID', primary_key=True, nullable=False, unique=True, autoincrement=True)  # 编号
    username = db.Column(db.String(80), doc='用户名', nullable=False, unique=True)
    password = db.Column(db.String(50), doc='密码', nullable=False)
    phone = db.Column(db.String(50), doc='电话', nullable=False)
    email = db.Column(db.String(50), doc='邮箱', nullable=False, unique=True)
    occupation = db.Column(db.String(32), doc='职业')
    introduction = db.Column(db.String(255), doc='个人简介')
    projects = db.relationship('Project', backref='user')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False


# 项目表
class Project(db.Model):
    __tablename__ = 'project'
    __table_args__ = {'mysql_engine': 'InnoDB'}  # 支持事务操作和外键
    pid = db.Column(db.Integer, doc='PID', primary_key=True, nullable=False, unique=True, autoincrement=True)  # 编号自动填写
    pname = db.Column(db.String(80), doc='项目名称', nullable=False)
    ppublisher = db.Column(db.String(80), db.ForeignKey('user.username'), doc="项目发布者")
    planguage = db.Column(db.String(50), doc='项目语言')
    pstate = db.Column(db.CHAR(1), doc='项目状态', default='1')
    pfield = db.Column(db.String(80), doc='项目领域')
    pdescription = db.Column(db.Text, doc='项目描述', nullable=False)
    pcreated_time = db.Column(db.DateTime, doc='项目创建时间', nullable=False, default=datetime.datetime.now())
    pclosed_time = db.Column(db.DateTime, doc='项目停止征集时间', nullable=False)


# 需求表
class Requirement(db.Model):
    __tablename__ = 'requirement'
    __table_args__ = {'mysql_engine': 'InnoDB'}  # 支持事务操作和外键
    rid = db.Column(db.Integer, doc='RID', primary_key=True, nullable=False, unique=True, autoincrement=True)  # 编号自动填写
    pid = db.Column(db.Integer, db.ForeignKey('project.pid'), doc="项目ID")
    uid = db.Column(db.String(80), db.ForeignKey('user.username'), doc="项目发布者")
    rname = db.Column(db.Text, doc='需求名称', nullable=False)
    description = db.Column(db.Text, doc='需求描述', nullable=False)
    rtype = db.Column(db.Text, doc='需求分类')
    priority = db.Column(db.Integer, doc="需求优先级")
    selected = db.Column(db.Integer, doc="是否被选中", nullable=False, default=1)
    posttime = db.Column(db.DateTime, doc='需求发布时间', nullable=False, default=datetime.datetime.now())
    img = db.Column(db.String(20), doc='图片资源', nullable=True)
    similar = db.Column(db.Integer, doc="相似需求", nullable=True)
