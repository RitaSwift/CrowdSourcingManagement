from app.models import User, Project, Requirement, db
from datetime import datetime
import os
import hashlib


def data_init():
    lock_file = os.path.join(os.getcwd(), 'data_init.lock')
    if os.path.exists(lock_file):
        return
    hl = hashlib.md5()
    hl.update('123456'.encode('utf-8'))
    # 插入用户
    # 插入用户
    user1 = User(username='JoyXu', password=hl.hexdigest(), phone='13212564378', email='2504589627@qq.com', occupation='学生',
                 introduction='平平凡凡，普普通通')
    db.session.add(user1)
    user2 = User(username='JoyXuNju', password=hl.hexdigest(), phone='13212564765', email='MF1832201@smail.nju.edu.cn',
                 occupation='学生', introduction='做最美的祖国花朵')
    db.session.add(user2)

    # 插入项目
    project1 = Project(pid=1, pname='众包需求预处理系统', ppublisher='JoyXu', planguage='Python', pfield='NLP,众包',
                       pdescription='众包需求预处理系统是一个用于收集大众志愿者提供的软件需求，支持项目发布者管理需求，自动化分析需求',
                       pclosed_time=datetime(2019, 12, 30, 23, 59))
    db.session.add(project1)
    project2 = Project(pid=2, pname='院前急救分诊系统（微信版）', ppublisher='JoyXuNju', planguage='Java,Js,Html', pfield='急救系统，医疗',
                       pdescription='用于在患者到达医院之前，可提前获悉患者的信息（基本信息、既往病史等等），让院内可以提前做好救治准备，为患者的救治争分夺秒。',
                       pclosed_time=datetime(2019, 12, 30, 23, 59))
    db.session.add(project2)
    project3 = Project(pid=3, pname='keepass', ppublisher='JoyXuNju', planguage='Java', pfield='Office/Business,Database,Security',
                   pdescription='A lightweight and easy-to-use password manager',
                   pclosed_time=datetime(2019, 12, 30, 23, 59))
    db.session.add(project3)

    project4 = Project(pid=4, pname='winmerge', ppublisher='JoyXu', planguage='C++', pfield='Storage,Filesystems,Embedded systems',
                   pdescription='Windows visual diff and merge for files and directories',
                   pclosed_time=datetime(2019, 12, 30, 23, 59))
    db.session.add(project4)

    project5 = Project(pid=5, pname='dban', ppublisher='JoyXu', planguage='C++',
                       pfield='Darik Boot and Nuke',
                       pdescription='A hard drive disk wipe and data clearing utility',
                       pclosed_time=datetime(2019, 12, 30, 23, 59))
    db.session.add(project5)

    db.session.commit()
    # 插入需求
    # Usability 可用性
    # Security 安全性
    # Reliability 可靠性
    # Performance 性能
    # Lifecycle
    # Capability
    # Software Interface
    frequirement1 = Requirement(pid=1, uid='JoyXu', rname='注册', description='注册用户，输入用户的用户名，密码，确认密码，联系电话和电子邮箱，点击注册',
                                rtype='Capability', priority=5)
    db.session.add(frequirement1)
    frequirement2 = Requirement(pid=1, uid='JoyXu', rname='登录', description='登录时，输入用户名和密码，点击登录', rtype='Capability',
                                priority=5)
    db.session.add(frequirement2)
    frequirement3 = Requirement(pid=1, uid='JoyXu', rname='个人信息修改', description='可以修改注册时候的个人信息，如联系电话、电子邮箱等等',
                                rtype='Capability', priority=5)
    db.session.add(frequirement3)
    frequirement4 = Requirement(pid=1, uid='JoyXu', rname='密码修改', description='可以修改密码，输入旧密码和新密码', rtype='Capability',
                                priority=5)
    db.session.add(frequirement4)
    frequirement5 = Requirement(pid=1, uid='JoyXu', rname='新建项目',
                                description='用户登录的情况下，点击发布项目，输入新建项目的名称、语言、领域、描述和截止日期，点击提交', rtype='Capability',
                                priority=5)
    db.session.add(frequirement5)
    frequirement6 = Requirement(pid=1, uid='JoyXu', rname='发布需求',
                                description='选取一个还在征集中的项目，提交新需求，提交需求的名称、类型、优先级、详细描述，提交需求图片为可选项', rtype='Capability',
                                priority=5)
    db.session.add(frequirement6)
    frequirement7 = Requirement(pid=1, uid='JoyXu', rname='整合需求',
                                description='一个项目征集结束后，项目所有者进入需求管理界面，点击整合按钮，系统自动将重复的需求归一起，方便后续用户筛选', rtype='Capability',
                                priority=5)
    db.session.add(frequirement7)
    frequirement8 = Requirement(pid=1, uid='JoyXu', rname='筛选需求', description='项目所有者整合好重复的需求后，选择想要的需求，重复的需求只选择一个就可以了',
                                rtype='Capability', priority=5)
    db.session.add(frequirement8)
    frequirement9 = Requirement(pid=1, uid='JoyXu', rname='自动分类和分析优先级', description='筛选后的需求，会根据一定的算法，进行自动分类和优先级的计算',
                                rtype='Capability', priority=5)
    db.session.add(frequirement9)
    frequirement10 = Requirement(pid=1, uid='JoyXu', rname='查找项目',
                                 description='用户在搜索栏或者查找项目中都可以搜索自己想要的项目，搜索后返回符合条件的项目列表', rtype='Capability', priority=5)
    db.session.add(frequirement10)
    frequirement11 = Requirement(pid=1, uid='JoyXu', rname='查找项目',
                                 description='用户在搜索栏或者查找项目中都可以搜索自己想要的项目，搜索后返回符合条件的项目列表', rtype='Capability', priority=5)
    db.session.add(frequirement11)

    srequirement1 = Requirement(pid=2, uid='JoyXuNju', rname='添加急救患者',
                                description='该功能提供给急救车上的随车的医护人员，由该医护人员添加急救患者的信息。', rtype='Capability', priority=5)
    db.session.add(srequirement1)
    srequirement2 = Requirement(pid=2, uid='JoyXuNju', rname='申请急救通道',
                                description='该功能提供给急救车上的随车的医护人员，由该医护人员为患者申请急救通道。', rtype='Capability', priority=5)
    db.session.add(srequirement2)
    srequirement3 = Requirement(pid=2, uid='JoyXuNju', rname='修改急救患者',
                                description='该功能提供给急救车上的随车的医护人员，由该医护人员修改急救患者的信息。', rtype='Capability', priority=5)
    db.session.add(srequirement3)
    srequirement4 = Requirement(pid=2, uid='JoyXuNju', rname='删除急救患者', description='该功能提供给急救车上的随车的医护人员，由该医护人员删除急救患者。',
                                rtype='Capability', priority=5)
    db.session.add(srequirement4)
    srequirement5 = Requirement(pid=2, uid='JoyXuNju', rname='文字输入',
                                description='该功能提供给急救车上的随车的医护人员，该医护人员可给受理端的医护人员发送文字。', rtype='Capability', priority=5)
    db.session.add(srequirement5)
    srequirement6 = Requirement(pid=2, uid='JoyXuNju', rname='生命体征', description='该功能提供给急救车上的随车的医护人员，采集患者生命体征数据发送给受理端。',
                                rtype='Capability', priority=5)
    db.session.add(srequirement6)
    srequirement7 = Requirement(pid=2, uid='JoyXuNju', rname='拍照、拍视频',
                                description='该功能提供给急救车上的随车的医护人员，拍摄患者照片或视频发送给受理端。', rtype='Capability', priority=5)
    db.session.add(srequirement7)
    srequirement8 = Requirement(pid=2, uid='JoyXuNju', rname='FAST评分',
                                description='该功能提供给急救车上的随车的医护人员，对患者进行卒中识别评估，并将FAST评分结果发送给受理端。', rtype='Capability',
                                priority=5)
    db.session.add(srequirement8)
    srequirement9 = Requirement(pid=2, uid='JoyXuNju', rname='简易NIHSS评分',
                                description='该功能提供给急救车上的随车的医护人员，对患者进行简易NIHSS评分，并将评分结果发送给受理端。', rtype='Capability',
                                priority=5)
    db.session.add(srequirement9)
    srequirement10 = Requirement(pid=2, uid='JoyXuNju', rname='Grace评分',
                                 description='该功能提供给急救车上的随车的医护人员，给患者进行Grace评分，并将评分结果发送给受理端。', rtype='Capability',
                                 priority=5)
    db.session.add(srequirement10)
    srequirement11 = Requirement(pid=2, uid='JoyXuNju', rname='兼容性需求', description='兼容适应Android 4.4.2及以上各个版本。',
                                 rtype='Performance', priority=3)
    db.session.add(srequirement11)
    srequirement12 = Requirement(pid=2, uid='JoyXuNju', rname='故障处理要求', description='在系统运行异常甚至发生故障时，能提供故障恢复能力。',
                                 rtype='Reliability', priority=3)
    db.session.add(srequirement12)
    srequirement13 = Requirement(pid=2, uid='JoyXuNju', rname='界面简单', description='功能操作不超过三级菜单；系统信息自动变更，无需手工刷新或重复操作。',
                                 rtype='Usability', priority=3)
    db.session.add(srequirement13)
    srequirement14 = Requirement(pid=2, uid='JoyXuNju', rname='权限需求', description='系统具有角色的应用功能权限管理能力，以及数据访问权限管理能力',
                                 rtype='Security', priority=5)
    db.session.add(srequirement14)
    srequirement15 = Requirement(pid=2, uid='JoyXuNju', rname='操作易学', description='清晰的导航；用户手册准确、易懂；简单的在线提示',
                                 rtype='Usability', priority=2)
    db.session.add(srequirement15)
    srequirement16 = Requirement(pid=2, uid='JoyXuNju', rname='高可用', description='保证系统持续、稳定运行。计划外停机时间控制在全年的5%以内',
                                 rtype='Usability', priority=2)
    db.session.add(srequirement16)
    srequirement17 = Requirement(pid=2, uid='JoyXuNju', rname='性能高', description='服务器平均利用率不大于75%。服务器处理并发连接数维持在1000以内。',
                                 rtype='Performance', priority=2)
    db.session.add(srequirement17)
    
    krequirement1 = Requirement(pid=3, uid='JoyXu', rname='System Tray, Retype master password', description='I have 2 suggestions for improvements. 1. Allow an option, that when the program is minimzed it  goes to the systm tray. 2. When you type in a new master password when you  first create a database, you should be asked to retype  it.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement1)

    krequirement2 = Requirement(pid=3, uid='JoyXu', rname='GUI improvements', description='1. Add these style flags to the list-view of passwords:  LVS_EX_HEADERDRAGDROP | LVS_EX_INFOTIP 2. In the dialog of &quot;File&quot;-&gt;&quot;Open Database...&quot; add filter  for .pwd files. 3. In the database view, open browser when clicking the  address. 4. In the database view, copy username to clipboard  when clicking the username. Thanks, Moshe',
                            rtype='Capability', priority=5)
    db.session.add(krequirement2)

    krequirement3= Requirement(pid=3, uid='JoyXu', rname='AutoLogin for web passwords', description='I think that could it be a great idea to let user autologin  into web sites. I\'m thinking about to ways: 1. The user provides: - login form page url  - form input control for username  - form input control for password ...then application builds a HttpRequest with login n  password as Post Data and send it to login form page. 2. The application parse data - User provides the login form page url - The app parses that url and reads each form input  control name, presenting its to user and leting him to  choose whitch match &quot;username&quot; and whitch does  for &quot;password&quot;. Please send me your impressions about it. Thanks a lot. Marco marco_sanjuan@hotmail.com',
                            rtype='Capability', priority=5)
    db.session.add(krequirement3)

    krequirement4= Requirement(pid=3, uid='JoyXu', rname='PocketPC support', description='One of the most useful pieces of software i know of is Illum Software\'s eWallet. This is a similar program but has a client that works on both the Win PC and the Pocket PC, thus allowing you to carry around your passwords (also with security). I might try to write a Pocket PC version if you like Thanks, and great program Jed',
                            rtype='Capability', priority=5)
    db.session.add(krequirement4)

    krequirement5= Requirement(pid=3, uid='JoyXu', rname='Search for Password Groups', description='Hi there, currently I\'m evaluating your nice little Password tool. I  guess it looks great. But there is one option I would like to see: There should be a possibility for the User to search for a  password Group. I\'d like to add >1000 Password Groups an I need to have  a solution to find the one i need. Sorting in the Group List doesn\'t even Work. I would be glad if someone can realize this, though I\'m  not a programmer at all. Thank you for the nice work Matthias',
                            rtype='Capability', priority=5)
    db.session.add(krequirement5)

    krequirement6= Requirement(pid=3, uid='JoyXu', rname='Add Columns to password entries', description='I have fields such as Business, Account Number, and  Phone in my present Excel password file.  I would like  KeePass to give me the capability to add my own  columns to password entries - not individually but  globally would be fine. My email: nugentfm@erols.com',
                            rtype='Capability', priority=5)
    db.session.add(krequirement6)

    krequirement7= Requirement(pid=3, uid='JoyXu', rname='Change Master Key should prompt twice', description='Change Master Key should prompt twice for the  password - just like \"Set Master Key\" when creating a  new file.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement7)

    krequirement8= Requirement(pid=3, uid='JoyXu', rname='Double-click title opens Edit Entry dialog', description='Hi, Please add this feature: In the database view, double-clicking the title column  will open the \"Edit Entry\" dialog. Moshe Berger',
                            rtype='Capability', priority=5)
    db.session.add(krequirement8)

    krequirement9= Requirement(pid=3, uid='JoyXu', rname='add toolbar', description='add some icons for quick access of menu commands  like \"copy password\". although there are already  shortcuts like ctrl+c for this it could be convenient for  some users to be able to click on a button instead of  reaching out for the keyboard. it also might improve  speed of program usage. example scenery: maximize from taskbar, select desired  entry, hit \"copy to clipboard\" button. done. might be faster for the the people that prefer clicking  and shouldn\'t be too much work to program ;)',
                            rtype='Capability', priority=5)
    db.session.add(krequirement9)

    krequirement10= Requirement(pid=3, uid='JoyXu', rname='Toolbar', description='Could a toolbar be added to KeePass with some of the  most commonly used features, like New Entry, Save, and  Copy? This would be extremely helpful, especially for  laptop users like myself who do not have an external  mouse, and only their touchpad to rely on. Thanks!',
                            rtype='Capability', priority=5)
    db.session.add(krequirement10)

    krequirement11= Requirement(pid=3, uid='JoyXu', rname='Incorrect PW issue', description='I use just one KeePass DB file, which opens  automatically when I run keypass.exe. If I mistype the DB password, keepass \'forgets\' which DB  I\'m using, and I have to select \"open database\" and  locate it again. Would be better if it remembered the DB until I explicitly  open another one. Apart from that, it\'s brilliant!',
                            rtype='Capability', priority=5)
    db.session.add(krequirement11)

    krequirement12= Requirement(pid=3, uid='JoyXu', rname='First impressions', description='What a cool tool!  Here\'s a few things I noticed on my  first use: * Would be nice to be able to drag a password to a  different group. * Hide/show password isn\'t synced with edit item (i.e. if  you show all passwords the editted item still defaults to  hidden). * Create new database gives you a default set of  groups, would be nice if instead a dialog appeared with  a list of possible groups which you could select from. The only problems I came across where: * Importing csv failed initially because the items were  not in quotes.  You could either change this so it works  or at least give an error message. * Make a change to a database and minimize keePass,  on restore you get a \"save before close?\" dialog. Perhaps you should prompt for saving on minimze? Jon',
                            rtype='Capability', priority=5)
    db.session.add(krequirement12)

    krequirement13= Requirement(pid=3, uid='JoyXu', rname='Print Preview', description='It would be nice to have print preview with group or complete list printing.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement13)

    krequirement14= Requirement(pid=3, uid='JoyXu', rname='Smart Card', description='- what about using smart card like a key disk? - what about using smart card for password database?',
                            rtype='Capability', priority=5)
    db.session.add(krequirement14)

    krequirement15= Requirement(pid=3, uid='JoyXu', rname='Weblogin', description='Could it be possible to include the username and  password as parameters in the URL? Maybe like this: http//somesite?usr=%USERNAME% &passw=%PASSWORD% For some websites this URL would work, others need a  HTTP Post to login. So this URL would have to be converted to a HTTP  POST; there are lots of examples out there to do this. This would make a \'one click login\' a lot easier. Other possibilities could be to dynamicly add the  parameters in the webbrowser, line RoboForm does it.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement15)

    krequirement16= Requirement(pid=3, uid='JoyXu', rname='XML Import', description='Hi Dominik, KeePass just gets better and better... excellent stuff, man! I did see someone request that KeePass \"CSV import\" function include a group field, and you suggested making an \"Extended CSV\" format. Instead of an extended CSV import, would a better option be the ability for KeePass to import the XML file format that it exports? The reason I thought of that feature is because I use KeePass to store all my passwords at both home and work... and of course my KeePass database gets out of sync. The safest way for me to currently sync the db is to export all passwords and import them into the other db and then manually remove duplicates. Since I have 10 different groups, the easiest way to manage grouping is to export and import 10 CSV files. I did think of requesting a \"Merge\" or \"Sync\" function, but I know that\'d be a fairly substantial task since it would require a new \"db diff/merging/comparison\" window to be designed and created, I imagine. Pete',
                            rtype='Capability', priority=5)
    db.session.add(krequirement16)

    krequirement17= Requirement(pid=3, uid='JoyXu', rname='Default filename for exporting', description='Hi Dominik, Here\'s another low-priority feature request :) Current behaviour has default filenames of \"Export.xml\", \"Export.csv\", etc. It\'d be nice to have the default export filename set to... <database name>.<file extension>, when exporting the whole database <group name>.<file extension> when exporting a group. Pete',
                            rtype='Capability', priority=5)
    db.session.add(krequirement17)

    krequirement18= Requirement(pid=3, uid='JoyXu', rname='Option to display currently open database', description='Hi again! I guess the title is fairly self-explanatory. At the moment, there\'s no way to see which KeePass database file you have open. Maybe an option to display the currently open database filename and path in the title bar would be nice? eg: \"KeePass Password Safe - K:\\Stuff\\Petes Passwords.kdb\" ...or maybe just... \"KeePass Password Safe - Petes Passwords.kdb\" Pete',
                            rtype='Capability', priority=5)
    db.session.add(krequirement18)

    krequirement19= Requirement(pid=3, uid='JoyXu', rname='Copy to/Move to Group', description='It would be nice to copy or move records between groups. Look at these images to have see the possible design: http://www.kavdane.cz/stanekl/projects/keepass/images/CopyToGroup.png, http://www.kavdane.cz/stanekl/projects/keepass/images/ctxmenu.png',
                            rtype='Capability', priority=5)
    db.session.add(krequirement19)

    krequirement20= Requirement(pid=3, uid='JoyXu', rname='Open multiple databases', description='The possibility to open multiple databases would bring the secure copying/moving records between databases. We could forget all troubles with qualified export to CVS, text, HTML, and XML for reverse import and leave the export only for the option to export records into another format. Have a look at this: http://www.kavdane.cz/stanekl/projects/keepass/images/GroupTree.png Notice, that the database should have some name (not only filename).',
                            rtype='Capability', priority=5)
    db.session.add(krequirement20)

    krequirement21= Requirement(pid=3, uid='JoyXu', rname='File encryption', description='First - Love your program, thank you very much. Second - I\'d like to be able to use the same application  to encrypt small text and image files. I dont know if this  is possable with your current data file design but it may  be a feature that would expand the functionallity of  your application greatly while it would not require any  changes i can think of to the interface or the way you  have groups/entries setup. Thanks again, Drew O\'Connor drewuvm@mailcan.com',
                            rtype='Capability', priority=5)
    db.session.add(krequirement21)

    krequirement22= Requirement(pid=3, uid='JoyXu', rname='PINs Import', description='Hello, There are a excellent competitor called PINs : http://www.mirekw.com/winfreeware/pins.html That I actually uses. But seems to be no more supported :/ So I will probably switch to KeePass that I discovered in the SF list by luck. I think he is good too but problem, I don\'t really want do a manual conversion of all my list AHEM =) So, is it possible to see in a near future, the possibility to import PINs exported text file ? Look like this in the text file : Category;System;User;Password;URL/Comments;Custom;Start date;Expires;More info Exemple (login/pass changed of course :) the first line is a repeat that the precedent paragraph, it is normal, it is in the file) : Category;System;User;Password;URL/Comments;Custom;Start date;Expires;More info Commercial;Rueducommerce.com;essai;uejERzj120;http://www.rueducommerce.com/;;;Never; E-mail;Ifrance;mankindien;freedom45A;http://www.ifrance.com/;mankindien@Ifrance.com;;Never; E-mail;GMX NET;70215876;ior7Rha1;http://www.gmx.net/;;;Never;GMX FreeMail NG||Réception : Pop.Gmx.Net||Emission : Mail.Gmx.Net (Authentification Sécurisé) Jeux vidéo;Serveurs Goa;TManIC;fre4ERM5;http://www.goa.fr/;;;Never; Etc... || is for a \"return to line\" (sorry french, didn\'t know how say \"retour ŕ la ligne\"), when there are several lines in the \"More Info\" section. Sometimes Never can be replaced by \"Jamais\" (french) or Never in all other language. I cannot say more information about his composition. @ +',
                            rtype='Capability', priority=5)
    db.session.add(krequirement22)

    krequirement23= Requirement(pid=3, uid='JoyXu', rname='Option to generally unmask passwords', description='Hi Dominik, after I enter the MASTERPASS, I can be sure that only I sit in front of the screen. Therefore I would love to have the possibility to set a global option to unmask all passwords or mask all by default. Thank you Malte',
                            rtype='Capability', priority=5)
    db.session.add(krequirement23)

    krequirement24= Requirement(pid=3, uid='JoyXu', rname='Logins with differentiated acces to pwd groups', description='It could be extremely useful if it was possible to create  multiple logins to a password database with  differentiated access to the password groups. E.g. four logins are created: admin hotline 2level secadm \"Admin\" is granted access to all password groups in the  database. \"Hotline\" is granted access to the password  groups \"Frontline Servers\" and \"Customer Passwords\" \"2level\" is granted access to the password  groups \"Frontline Servers\", \"Backline Servers\"  and \"Customer Passwords\" \"secadm\" is granted access to the password  groups \"Network Devices\", \"Firewalls\", \"Frontline Servers\"  and \"Backline Servers\". All passwords are only written once in a single database,  but different users in different departments have  different access to different passwords within the  database - based on their login to the KeePass  database.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement24)

    krequirement25= Requirement(pid=3, uid='JoyXu', rname='Start minimized and locked', description='It would be nice if there was the possibility to start the  program minimized in the tray bar, with the database  already locked and without popping up the password  dialog.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement25)

    krequirement26= Requirement(pid=3, uid='JoyXu', rname='Remember window placement', description='It would be nice if the program stores the window  position, and restores it when started.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement26)

    krequirement27= Requirement(pid=3, uid='JoyXu', rname='Moving items between groups', description='It would be very usefult if it was possible to move one or  more items between groups and subsgroups with  drag&drop, instead of changing them one by one.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement27)

    krequirement28= Requirement(pid=3, uid='JoyXu', rname='create client application or port to PALM||PPC', description='that\'s nice what you guys created. however for me it has only partial usage - as i need to  have my password all the time with me. breta_passinger@seznam.cz',
                            rtype='Capability', priority=5)
    db.session.add(krequirement28)

    krequirement29= Requirement(pid=3, uid='JoyXu', rname='drag and drop', description='It would be nice if you could drag a selection of posts to  other groups.  The action taken could be one of the following: #Move post to that group #Make visible in that group also (since it\'s a database  there should be no problem displaying the same record in  different places). It should maybe not *copy* it, because  repeating strings in an encrypted text is not a good  thing..I think.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement29)

    krequirement30= Requirement(pid=3, uid='JoyXu', rname='SYNCH with PPC, AND a workgroup File', description='I miss synchronization options in Workgroups. For Teams sharing passwords. And a personal synchronization to PPC Version of  KeePass. Regards. waelder_at  at  hotmail.com',
                            rtype='Capability', priority=5)
    db.session.add(krequirement30)

    krequirement31= Requirement(pid=3, uid='JoyXu', rname='window position', description='It would be nice with a \"remember window  position\"-checkbox in the options dialogue. this should decide whether to include window position in  the ini-file.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement31)

    krequirement32= Requirement(pid=3, uid='JoyXu', rname='Auto-save', description='Typically when I use database-like applications I don\'t  have to click a save button to commit my changes.  It  just happends when I edit the field.  I thought this could  be a good feature to add to this program.  Maybe it  could be configurable in case someone would want to  click save everytime they make a change.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement32)

    krequirement33= Requirement(pid=3, uid='JoyXu', rname='Auto-save', description='Typically when I use database-like applications I don\'t  have to click a save button to commit my changes.  It  just happends when I edit the field.  I thought this could  be a good feature to add to this program.  Maybe it  could be configurable in case someone would want to  click save everytime they make a change.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement33)

    krequirement34= Requirement(pid=3, uid='JoyXu', rname='Auto-save', description='Typically when I use database-like applications I don\'t  have to click a save button to commit my changes.  It  just happends when I edit the field.  I thought this could  be a good feature to add to this program.  Maybe it  could be configurable in case someone would want to  click save everytime they make a change.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement34)

    krequirement35= Requirement(pid=3, uid='JoyXu', rname='moving password entries among Groups', description='It will be nice to allow moving password entries among  Groups.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement35)

    krequirement36= Requirement(pid=3, uid='JoyXu', rname='Drag & Drop', description='I have been using KeyWallet for a couple of years and  its capability to drag and drop username and password  directly into a form (in a web page, in a standard  program and even in an java applet) is really useful. Simple macro-scripting is unsubstituible as well Take a look at the flash demo: http://www.keywallet.com/ the_hobbit30@hotmail.com',
                            rtype='Capability', priority=5)
    db.session.add(krequirement36)

    krequirement37= Requirement(pid=3, uid='JoyXu', rname='Add a password history retention option', description='It would be nice to have a feature that would retain  passwords that you have previously used on an entry  whenever you change it.  This would be good for making  sure you don\'t use a password you\'ve used before or  you might have restored a system from backup and that  backup still is using an older password. nathand@perteet.com',
                            rtype='Capability', priority=5)
    db.session.add(krequirement37)

    krequirement38= Requirement(pid=3, uid='JoyXu', rname='Datepicker  in Password Generator', description='It would be nice to have a Datetime-Picker option in that 2 fields where I can input the expiration date etc. That is not to difficult and could easy be made in Version 0.95 Thanks',
                            rtype='Capability', priority=5)
    db.session.add(krequirement38)

    krequirement39= Requirement(pid=3, uid='JoyXu', rname='Keyring Interface', description='Is there any chance that you could import/export files to Keyring to support the Palm OS? See: http://gnukeyring.sourceforge.net/index.html',
                            rtype='Capability', priority=5)
    db.session.add(krequirement39)

    krequirement40= Requirement(pid=3, uid='JoyXu', rname='New Column Add and Column Name Change', description='Hi there - is it possible that KeePass has a option for  new customized column adding and name changing?',
                            rtype='Capability', priority=5)
    db.session.add(krequirement40)

    krequirement41= Requirement(pid=3, uid='JoyXu', rname='Output file with group information', description='Hi there - It will be nice if KeePass can output and  import group or subgroup information.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement41)

    krequirement42= Requirement(pid=3, uid='JoyXu', rname='Some similar features link PINs', description='I have used PINs for a long time. PINs  (http://www.mirekw.com/) has some nice features such  as \'SuperPaster\' and \'System-wide Hotkeys\'. I am looking  forward to seeing these features in your KeePass.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement42)

    krequirement43= Requirement(pid=3, uid='JoyXu', rname='Show database name on login screen', description='When working with more than one database and  with \"open last database on startup\" activated, it might  be helpful to see the name of the database to be loaded  to type in the correct password. In this place an \"open another database\" button would  be nice, too.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement43)

    krequirement44= Requirement(pid=3, uid='JoyXu', rname='Support for automatic username/password insertion', description='It would be nice if KeePass supported popular  applications, e.g. IE, and learn/insert usernames and  passwords automatically. The current cut and paste  process is tiring! Clearly the plug-ins will require registration, etc. but it  worth it.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement44)

    krequirement45= Requirement(pid=3, uid='JoyXu', rname='Auto reveal password in list', description='Hi, great software - looked at several PW managers but this  is awesome and the one I will use from now on. One feature that I miss a bit is the \"auto reveal  password\" that Password Keeper 2001 offers. It means that when you click on an entry in the lists of  passwords it just reveals that one password. KeePass only allows to show all PW or hide all - but not  conditional. You can check out the feature in the trial ware available  here: http://www.wolff- software.de/v2/en/f_page_pwk2001.html Do you think this option can be added? It allows to  check a single password without having the complete  list visible to anybody looking over your shoulder. Thanks in advance - Peter Weiss',
                            rtype='Capability', priority=5)
    db.session.add(krequirement45)

    krequirement46= Requirement(pid=3, uid='JoyXu', rname='command line version', description='I\'d like to see a text/terminal capable interface (at least for retrival)',
                            rtype='Capability', priority=5)
    db.session.add(krequirement46)

    krequirement47= Requirement(pid=3, uid='JoyXu', rname='Insert criptology with blowfish 448bit', description='Insert criptology with blowfish 448bit',
                            rtype='Capability', priority=5)
    db.session.add(krequirement47)

    krequirement48= Requirement(pid=3, uid='JoyXu', rname='Insert support for PGP 8 for key', description='Insert support for PGP 8 for key encription with private  and pubblic key',
                            rtype='Capability', priority=5)
    db.session.add(krequirement48)

    krequirement49= Requirement(pid=3, uid='JoyXu', rname='Group Organization : Drag and Drop', description='Hi, I have recently started using KeePass Password Safe  and I feel that it is a fantastic product. Excellent work.  I would like to see the ability to move entries from one  Password group to another for organizational purposes in  a future release.  Thanks. Best regards, Rick. lord_brimstone@hotmail.com',
                            rtype='Capability', priority=5)
    db.session.add(krequirement49)

    krequirement50= Requirement(pid=3, uid='JoyXu', rname='SmartCard instead of a master password', description='It would be nice to have the option to use a smartcard  instead of a master password or password disk for  password database. I have a notebook with built-in  smartcard reader and use the smartcard for online  banking authorization, and it would be great if I could  use an empty -- or even the bank\'s card as it has free  capacity too -- as a password card OR perhaps even for  storing the passwords database. Thanks -- KeePass is  GREAT piece of software, I love it! Jaromír,  jaromir@vicari.cz',
                            rtype='Capability', priority=5)
    db.session.add(krequirement50)

    krequirement51= Requirement(pid=3, uid='JoyXu', rname='Palm OS5 version would be great', description='I know there is a pocketpc version, but how about a  palm version for us palm users?',
                            rtype='Capability', priority=5)
    db.session.add(krequirement51)

    krequirement52= Requirement(pid=3, uid='JoyXu', rname='Palm OS v5 version would be great', description='A Palm OS v5 version would be great for us Palm Users!! Thanks for the great product. maxsteel@shaw.ca',
                            rtype='Capability', priority=5)
    db.session.add(krequirement52)

    krequirement53= Requirement(pid=3, uid='JoyXu', rname='Expiration Dates', description='Question First:  What will KeePass do when a password reaches expiration? Feature requested:  Allow to set cyclical expiration, like, \"Change Monthly\", etc.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement53)

    krequirement54= Requirement(pid=3, uid='JoyXu', rname='Improve database security', description='A very, very good start. There are so many things that make this tool great. So, it is difficult for me to say that it urgently needs 2  additional features... 1. a character map or keypad to enter passphrases while  defeating keyloggers 2. to the left of the entry panel, a small database status  panel that displays at all times a) database title b) database subject c) database comment d) database algorithm e) number of entries f) number of categories g) last saved h) any other anti-cloning device Its wonderful to see that the .EXE has been kept small  enough to fit on a floppy.  So, I suggest that any non- essential crypto-functions be added as stand-alone  applications & offered as part of a security suite. This security suite could include things like  disk wiper  file shredder  text editor with encryption features',
                            rtype='Capability', priority=5)
    db.session.add(krequirement54)

    krequirement55= Requirement(pid=3, uid='JoyXu', rname='Shorter Passwords on lock', description='I have used DMSpassman, for managing my passwords  but its getting a bit dated, however a couple of nice  features in it are the default master password has to be  a minimum length (32 characters).  However once entered and you have the program  running you have the option to specify a shorter  temporary password, eg 4 characters which is valid just  for that session.  This is great as if you lock the password manager after  a set time period you just have to enter the temporary  password (or the master key if you forget the temporary  password) to unlock the database without having to  enter your whole passphrase each time.  Another nice feature in DMSpassman, rather than  copying and pasting to the clipboard, is that you can  right click on the minimised taskbar entry, select a title  entry and then send the username and/or password to  the current cursor position. This is great when you are  using it to fill in online forms etc.  It would be great to see similar features in KeePass,  which looks to be a good package in its own right. I like  keypass\'s small portable size with its standalone mode  and ability to keep configuration settings in its own ini  file. Keep up the good work!',
                            rtype='Capability', priority=5)
    db.session.add(krequirement55)

    krequirement56= Requirement(pid=3, uid='JoyXu', rname='Customizable Icon Library', description='No doubt that this feature request will sound trivial but...  Since KeePass let users choose an icon for groups, subgroups, and entries could you separate the icon library from the executable so one could create a custom icon library and share them. For example I could inset a little plane for a group containing airline frequent flyer accounts.  If you do so, please, make this library editable by standard graphic tools.  Thanks a lot for your work Sea',
                            rtype='Capability', priority=5)
    db.session.add(krequirement56)

    krequirement57= Requirement(pid=3, uid='JoyXu', rname='Force Strong Master PW', description='I might like to provide this program to my users, but ONLY if I can force them to choose a strong master password.  There should be an admin-friendly version that will ensure their master passwords meet minimum requirements that *I* set.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement57)

    krequirement58= Requirement(pid=3, uid='JoyXu', rname='Closed groups', description='Wow this program is great, ive tried a few password  managers and this is by the far the best.   one small interface suggestion would be that everytime i  go back to my password database it remembers how i  left my groups with the tab open or closed - it\'d be  better if there was an option for it to remember or to  leave them all closed as default. I often have someone hovering around when im in the  database and i dont want them seeing everything i have  in there - although i have names and passwords *\'d  out.  (By the way username *\'ing doesnt seem to do it  when you open the entry)',
                            rtype='Capability', priority=5)
    db.session.add(krequirement58)

    krequirement59= Requirement(pid=3, uid='JoyXu', rname='Hover password reveal', description='When the mouse is held motionless over the password column of a row reveal the password in a balloon',
                            rtype='Capability', priority=5)
    db.session.add(krequirement59)

    krequirement60= Requirement(pid=3, uid='JoyXu', rname='clipboard password reveal', description='in between all hidden or all revealed exposing the password currently in the clipboard would allow a quick verification that the value is the one expected. Possibly a different (shorter) timeout.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement60)

    krequirement61= Requirement(pid=3, uid='JoyXu', rname='icon nickname', description='It would be nice to accompany the ison with their conventional usage nickname.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement61)

    krequirement62= Requirement(pid=3, uid='JoyXu', rname='password generation (pronouncable)', description='Additional password generation options: 1) euphonic (pronouncable) sequence between x and y characters long option FugDemKet 2) Dictionary word between x and y characters long as a sequence option 2) Sequence symbol/custom Sequence FugDem=Partly 3) Sequence separator Sequence separator Sequence FugDem:partly6dark 4) alliteration, each sequence should begin with the same letter/phoneme FugDem[ford]phule http://zaph.com/ has python code that joins two words with a random number/symbol',
                            rtype='Capability', priority=5)
    db.session.add(krequirement62)

    krequirement63= Requirement(pid=3, uid='JoyXu', rname='form filler', description='Can a form filler be added?  Maybe a seperate project  that would work with the keepass database.  And to add  to it a program that would import roboform data.  sonyboy851@cybercoment.com',
                            rtype='Capability', priority=5)
    db.session.add(krequirement63)

    krequirement64= Requirement(pid=3, uid='JoyXu', rname='Quepasa password generator', description='See http://quepasa.sourceforge.net/ for a good  description of quepasa.  Quepasa is useful for creating  strong passwords that can be recreated or recovered by  use of a catchphrase.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement64)

    krequirement65= Requirement(pid=3, uid='JoyXu', rname='Admin Security Features', description='Along the lines of the suggestion to let an admin FORCE  users to select a strong MASTER PW, I would also  propose allowing an admin to LOCKDOWN the software  as desired.  For example, I would NOT want my users to  be able to print or export the database.  It\'s too easy  this way for them to lose control of all their passwords  in one fell swoop. Clearly, my concerns relate to wanting to help users in a  large corporate network keep up with their ever- expanding password universe.  (Single sign-on, indeed!) I expect that as the number of passwords they must  remember increases and the complexity increases, the  overall security decreases.  Why, because they write  them down or use the same one on all systems.... Anyway, thanks for a great program!',
                            rtype='Capability', priority=5)
    db.session.add(krequirement65)

    krequirement66= Requirement(pid=3, uid='JoyXu', rname='Adding A Personal Information Book', description='One thing that I\'ve always tried to keep up with is  personal information for my family.  This is just as  important as passwords, in my opinion. A nice feature would be to somehow add a personal  information book to the program, which could have  entries for a person (title) and have columns such as  social security number, date of birth, drivers license  number, etc.  I am constantly calling my parents or wife  to ask for the information, because Im afraid to write  the information down anywhere, for fear of losing it. Adding this feature to KeePass would eliminate the need  to keep doing this. Thanks for the wonderful program!',
                            rtype='Capability', priority=5)
    db.session.add(krequirement66)

    krequirement67= Requirement(pid=3, uid='JoyXu', rname='Sorting and Initiallization Features', description='A few things that would be helpful... Have the program save off the last folder group that it  was last in, instead of always reverting back  to \"General.\" In many Wondoze programs, the column fields (e.g.,  Title, Username, Password, etc.) allow you to select the  way the items are organized, by title, username, etc,  simply by clicking on the column title. If the column is  already selected, it changes from ascending to  descending (indicated by a little up or down triangle). Another feature would be to have the program  automatically sort entries based on the currently  selected sort by setting.  This would be a nice  feature, as when adding a new entry, you must sort the  items again to get them back in order. Wow, you must be busy with all the feature requests. Good luck getting them implemented.  (You might want  to consider getting a Paypal account so people can  send you money!)',
                            rtype='Capability', priority=5)
    db.session.add(krequirement67)

    krequirement68= Requirement(pid=3, uid='JoyXu', rname='Java verison for mobile phones', description='i\'m interest for a version for JAVA mobile phones to use the same database on the way... sorry, my english is not so good. Thx, Matze',
                            rtype='Capability', priority=5)
    db.session.add(krequirement68)

    krequirement69= Requirement(pid=3, uid='JoyXu', rname='Import from Personal Vault', description='I love this program, but I purchased the program  Personal Vault and to date I have over 1500 entries in  this program. THe program only exports text files and they are not  really formatted that well.  Example of text file that PV exports below. The program  does work off a database. I was hoping that you might  be able to create an import from the database file. ---------------------- Account:      Big Hoods User Name:    username Password:     password Hyperlink:    www.domainname.com Comments:     Account ---------------------- Account:      Briar Patch User Name:    username Password:     password Hyperlink:    www.domainname.com Comments:     Account ----------------------',
                            rtype='Capability', priority=5)
    db.session.add(krequirement69)

    krequirement70= Requirement(pid=3, uid='JoyXu', rname='Default settings for Password Generator', description='In KeePass 0.94a, the settings in the password generator are set to the program\'s defaults each time the generator is opened. If you prefer different settings by default, they must be changed each time. I would like to suggest a \"set as defaults\" button that changes the default settings for the password generator.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement70)

    krequirement71= Requirement(pid=3, uid='JoyXu', rname='start at last used group', description='I apologize if this request has already been made.  Could Keepass be enhanced so that when it starts, it  starts with the last used Group selected, instead of the  top-most group? If not this, then, atleast, allow the use of the down- arrow key to quickly go to the desired group. The top- most group is selected when Keepass starts, but it  is \"grey\" selected. Thanks',
                            rtype='Capability', priority=5)
    db.session.add(krequirement71)

    krequirement72= Requirement(pid=3, uid='JoyXu', rname='quicker startup', description='I use keepass in a 133Mhz laptop. There is a 2-3  seconds delay between when I doubleclick on Keepass  and when the prompt for the master key shows up.  Other  password management programs startup faster.  Of course, they are lesser programs. Please keep the  startup time fast! Thanks',
                            rtype='Capability', priority=5)
    db.session.add(krequirement72)

    krequirement73= Requirement(pid=3, uid='JoyXu', rname='Ability to move entries', description='I would like to be able to drag an entry into a different  password group. An alternative would be the ability to  copy/paste an entire entry. Great product!',
                            rtype='Capability', priority=5)
    db.session.add(krequirement73)

    krequirement74= Requirement(pid=3, uid='JoyXu', rname='Credit cards and other info', description='It would be nice if KeePass knew about some other kinds of structured information. Credit cards, for example, would require * Type (visa, mc, amex, etc) * Issuing bank * Other identifier * Holder name (printed on front of card) * Company name (if a corporate-issued card) * Card number (usu. 16 digits, but not always) * Bank check number (3-digit number on back) * 1-800 number for bank I\'m abusing the existing columns to hold this information at the moment. Nice program, by the way.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement74)

    krequirement75= Requirement(pid=3, uid='JoyXu', rname='Multiple lines in Entry Summary', description='Hi, Impressed with KeePass - good job well done :) One  minor interface tweak I would like to see is to have the  summary of each entry in the grey box at the bottom on  multiple lines - one per field, rather than all together on  one line (with wrapping). Would make it a little easier  and quicker to spot the info you\'re looking for that way. Cheers, Luke',
                            rtype='Capability', priority=5)
    db.session.add(krequirement75)

    krequirement76= Requirement(pid=3, uid='JoyXu', rname='Expiring dates still not okay', description='In 0.94a, I wrote about what happens when a password expires.  You told me that an \"X\" would appear next to it.  It does.  I just installed 0.95a, and the expired password dates are the same as in 0.94a -- the \"X\" appears, but when I enter a new expiration date, the \"X\" stays.  Duplicating the entry copies the \"X\" with the dupe.  YET, when I request \"Show all expired entries\", nothing comes up in that display.  SO, it seems to me that handling expiration dates still isn\'t very useful. Ken Ruppel',
                            rtype='Capability', priority=5)
    db.session.add(krequirement76)

    # krequirement77= Requirement(pid=3, uid='JoyXu', rname='TAN wizard', description='The TAN wizard seems to eliminate all text characters,  only leaving numerics. This is unfortunate, since a lot of TANs are  alphanumeric, hence this feature is unfortunately not  suitable. Additional input formats, such as e.g. credit card  information, would also be very useful. Otherwsie a very nice and handy program. Many thanks! Kurt C',
    #                         rtype='Capability', priority=5)
    # db.session.add(krequirement77)

    # krequirement78= Requirement(pid=3, uid='JoyXu', rname='Storage .kdb database file online option', description='Hi It really would be great to open (read /write) the .kdb  files trough the web. For instance using the  MSN / Yahoo storage places  and / or via FTP. Many people use professional and personal password  mixed, to minimize the time and effort it cost to  administer these changes I propose to build in some web  sync option. Seamless (read / write) access from any  ware, 2 all my usernames and password is what I would  like to have!',
    #                         rtype='Capability', priority=5)
    # db.session.add(krequirement78)

    krequirement79= Requirement(pid=3, uid='JoyXu', rname='Total number of entries', description='I would like the total number of entries added to be  shown somewhere, e.g. statusbar or through a menu  function.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement79)

    krequirement80= Requirement(pid=3, uid='JoyXu', rname='Accelerators for dialogs', description='It would be nice if the dialogs had accelerators other  than &OK and &Cancel. For example, if the Add/Edit  Entry dialogs had Alt+T for Title, Alt+. for ... (show/hide  cleartext passwords), etc.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement80)

    krequirement81= Requirement(pid=3, uid='JoyXu', rname='Disc key size', description='Loved what you done this far with the code, excelent lil\'  program. There is one feature that needs to evolve:  Option to manage the size of the key file on the disk.  Yes I know process speed will suffer as the size of the  floppy file grows. But some high sec. uses migth not  mind, just let the end user deside it. = )',
                            rtype='Capability', priority=5)
    db.session.add(krequirement81)

    # krequirement82= Requirement(pid=3, uid='JoyXu', rname='Support for Sibylle', description='Sibylle (http://www.isecurelabs.com/) is a similar  system, but lacking many of the features of KeePass. Unfortunately, it is what we use at work, and as there is  no export feature (other than to its native DB type), we  will have difficulty moving from it into KeePass because  of the large databases each user has already built.  I  don\'t think that their DB format is documented  anywhere, so this may be an impossible request, but it  can\'t hurt to ask...',
    #                         rtype='Capability', priority=5)
    # db.session.add(krequirement82)
    #
    # krequirement83= Requirement(pid=3, uid='JoyXu', rname='Support for multiple databases', description='There are a fair number of shared passwords on our  network. I can see that making a group for shared  passwords and exporting/importing it each time one of  these changed would be doable, but it would also be  unwieldy. Perhaps the ability to open a number of  password databases simultaneously (and display them  as one tree) would allow the shared passwords to exist  in thier own database. Then by adding code to check  each open database for changes at each unlock of the  workspace (and with a manual refresh button), then  changes to this database could be automatically  propagated. This would make sharing passwords among  workgroups very easy, and the underlying OS could be  used to control who has write access to a file (and by  frequently checking for updates to the file, as well as  checking for updates before writing, the problem with  overwriting changes with multiple editors could be  greatly reduced). This could potentially address workgroup issues  mentioned frequently in the forum.',
    #                         rtype='Capability', priority=5)
    # db.session.add(krequirement83)

    krequirement84= Requirement(pid=3, uid='JoyXu', rname='Direct logon RDP, Telnet, drive map. etc', description='rvwestbr@hotmail.com I love this tool..!! Is it possible to add the following feature, direct connect to a rdp (remote desktop) or telnet  session or ftp, drive map etc. with your user name and  pw entry from the database. This would make live a lot easier.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement84)

    # krequirement85= Requirement(pid=3, uid='JoyXu', rname='mutiple hyperlink in one item (entry)', description='most of time, we have an item (person) has several  email addresses and website. I would like I can right  click and choose one of them to open, like the function  of PINs (Freeware  http://http://www.mirekw.com/index.html\\)',
    #                         rtype='Capability', priority=5)
    # db.session.add(krequirement85)

    krequirement86= Requirement(pid=3, uid='JoyXu', rname='Default Icon', description='An option for giving a new item contained within a group  the icon of it\'s parent group by default. ',
                            rtype='Capability', priority=5)
    db.session.add(krequirement86)

    krequirement87= Requirement(pid=3, uid='JoyXu', rname='Ctrl+A', description='it would be nice if this would select all. maybe insert  could be Add new',
                            rtype='Capability', priority=5)
    db.session.add(krequirement87)

    krequirement88= Requirement(pid=3, uid='JoyXu', rname='No Generated Password on New Item', description='An Option to not have a generated password by default  in a new item',
                            rtype='Capability', priority=5)
    db.session.add(krequirement88)

    krequirement89= Requirement(pid=3, uid='JoyXu', rname='Move Entry Via Group Tree', description='If you could move an entry or entrys to another group by  dragging the entry to the selected group tree item',
                            rtype='Capability', priority=5)
    db.session.add(krequirement89)

    krequirement90= Requirement(pid=3, uid='JoyXu', rname='Make a version for mac', description='Would be nice to have this program made for macs',
                            rtype='Capability', priority=5)
    db.session.add(krequirement90)

    # krequirement91= Requirement(pid=3, uid='JoyXu', rname='Make saving more intelligent', description='When minimizing the interface, it always asks if I want to save my changes even if nothing has changed. As far as I understood this is because the \"last access time\" is saved. This can be overriden by the \"save database automatically\" option, but this is too dangerous in case something valuable got changed by accident. I suggest having another option where \"last accesses\" are saved automatically. If nothing else has changed, then it should save it automatically. If something else has changed, then ask if it should be saved. (Or the other way round: give an option if you want to save the last access time. This would also solve the problem.) Excellent program by the way! I love it!',
    #                         rtype='Capability', priority=5)
    # db.session.add(krequirement91)

    krequirement92= Requirement(pid=3, uid='JoyXu', rname='Linux port', description='Any chance of a Linux port of this application?',
                            rtype='Capability', priority=5)
    db.session.add(krequirement92)

    krequirement93= Requirement(pid=3, uid='JoyXu', rname='Port to Java', description='Port this app to Java so it\'s platform independant. Many have a need to use Linux at work and PC/MAC at  home, would be nice to use the save database and UI.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement93)

    # krequirement94= Requirement(pid=3, uid='JoyXu', rname='Change keyboard shotcuts', description='(mb) The keyboard shortcuts are generally excellent but you might like to consider switching from Ctrl+A for the new (add) entry to say Ctrl+N. This would enable you to use Ctrl+A in the way that most other Windows programs do to \"Select all\" items in a pane.  At the moment in order to use the Mass Modify one has to use the Shift click procedure to select the relevant items.',
    #                         rtype='Capability', priority=5)
    # db.session.add(krequirement94)

    krequirement95= Requirement(pid=3, uid='JoyXu', rname='Change entry view font', description='(mb) Also, and again not essential, it would be nice if the font style and size in the bottom pane could match that selected for the main columns. On a high resolution screen the small text can be a little difficult to read (at least for my ageing eyes).',
                            rtype='Capability', priority=5)
    db.session.add(krequirement95)

    krequirement96= Requirement(pid=3, uid='JoyXu', rname='Status bar enhancement', description='(mb) And finally (and a low priority) it would be nice to have a count in the bottom status bar of the number of items in a Group or the number of items selected in the right hand pane - again rather like Windows Explorer.  Although not essential this would be helpful when checking that an import or export has worked correctly.',
                            rtype='Capability', priority=5)
    db.session.add(krequirement96)

    # krequirement97= Requirement(pid=3, uid='JoyXu', rname='Auto Lock', description='When you check the option \'Automatically lock workspace  after following number of seconds:\' and enter a value in  the text box, when the idle time is up to program comes  into focus and locks. It would be nice if the program did not come into focus  and either minimized to the tray or the taskbar depending  on the state of the \'Minimize to tray insted of taskbar\'  option... ah',
    #                         rtype='Capability', priority=5)
    # db.session.add(krequirement97)

    # krequirement98= Requirement(pid=3, uid='JoyXu', rname='Firefox Integration', description='I read that IE integration was in the works.  Pretty please also do Firefox integration.  Preferably a method that doesn\'t use the clipboard so any keyloggers/clipboard monitors can be defeated. Thank you for a great app.',
    #                         rtype='Capability', priority=5)
    # db.session.add(krequirement98)
    #
    # krequirement99= Requirement(pid=3, uid='JoyXu', rname='Order of columns not saved', description='If you rearrange the order that the columns appear (UserName, Password, URL, etc.)  and then close the program, they are not remembered the next time the program is run.  This would be useful. I found a thread from December 2003 in the Open Discussion Forum (http://sourceforge.net/forum/message.php?msg_id=2336119) that suggests the feature was added, however I just downloaded 0.95b and it doesn\'t appear to be there. Thanks!!  Great program!  Quality!!',
    #                         rtype='Capability', priority=5)
    # db.session.add(krequirement99)
    #
    # krequirement100= Requirement(pid=3, uid='JoyXu', rname='use any file as password jpg,exe etc.', description='It would be nice to be able to use any file as a  password  could use any combo of filename,size,snippet of file this way you could hide password in plain sight. How many files are on your computer? just an sugestion. great program keep up the good work',
    #                         rtype='Capability', priority=5)
    # db.session.add(krequirement100)







    wrequirement1= Requirement(pid=4, uid='JoyXuNju', rname='Third merge file', description='It would be good if one could save the merged result into a third file, instead of having to overwrite one of the two comparison files.',
                            rtype='Capability', priority=5)
    db.session.add(wrequirement1)

    # wrequirement2= Requirement(pid=4, uid='JoyXuNju', rname='Location bar a la Windiff', description='A Location bar (called Picture in windiff) that gives an overview of the changes, and where text blocks have been moved to would be really useful.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement2)

    # wrequirement3= Requirement(pid=4, uid='JoyXuNju', rname='&quot;Copy a difference to the clipboard&quot;.', description='Sure would be nice if you could &quot;Copy a difference to the clipboard&quot;. In a difference window, a right click on a highlighted difference could have an option in the popup window for Copy diff to clipboard. This would copy the single selected difference from the window selected to the clipboard. This would make discussing differences between files much easier. Thanks, Darrell Duffy Sunnyvale, CA http://www.bigfoot.com/~Darrell_Duffy/',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement3)
    #
    # wrequirement4= Requirement(pid=4, uid='JoyXuNju', rname='directory compare list can\'t be saved', description='I\'m using V1.7.1.222. I want to save the result list from compare: c:\\winnt\\system32 and d:\\backup\\system32. The list is shown correctly on the screen. I need to sort the List. So I indended to save the list to a file and work with EXCEL. Later on I generate a Batch file. Bye Bernd',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement4)

    # wrequirement5= Requirement(pid=4, uid='JoyXuNju', rname='add drag&amp;drop', description='Logged In: YES  user_id=39104 Browser: Mozilla/4.7 [de] (WinNT; I) it would be very helpful if the files which are to be compared could just be drag &amp; dropped into the blank startup window. [thanx, developers - winmerge is the best tool around !!! i love it.]',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement5)

    # wrequirement6= Requirement(pid=4, uid='JoyXuNju', rname='Be able to increase length of line shown', description='It would be nice to be able to increase the length of  the line that is shown before the line is truncated  and &quot;...&quot; is appended. I have been attempting to use WinMerge for the  analysis and merging of XML/XSL files, and some of the  lines can be indented quite a bit... even past the  maximum length allowed such that all that I see  if &quot;...&quot; for the line.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement6)

    # wrequirement7= Requirement(pid=4, uid='JoyXuNju', rname='Single Instance and Autoclose on no-diff', description='When diffing multiple files from WinCVS, it would be  handy if WinMerge could be configured to use only one  instance of itself, and load the additional files into  seperate MDI child windows. It would also be nice if WinMerge could be configured  to automatically close a file comparison window if  both files matched. Mark',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement7)

    wrequirement8= Requirement(pid=4, uid='JoyXuNju', rname='Refine differences', description='It would be nice to have a \'refine diference region\' a  la emacs.',
                            rtype='Capability', priority=5)
    db.session.add(wrequirement8)

    # wrequirement9= Requirement(pid=4, uid='JoyXuNju', rname='Saving without merging all.', description='I\'m familiar with using the \'gdiff\' on SGI  Workstations and WinDiff is pretty close. However, one  very important feature needs to be added. When you begin merging files, from one side to the  other, and then try to save, if there are any sections  of code you -have not- touched yet, you should be  given a warning message, moved to the appropriate  section of code and not allowed to save.  This would prevent losing some code that you  inadvertantly glanced over while scrolling through  them. This has happened well more than once, where I  have left out crucial sections of code, or missed a  closing brace on a function that wrecked havoc later  on.  Better color-coding would help too. Once a section of  code has been merged, it should change color. Any  missing sections that have not been touched should  have their own respective color....',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement9)

    # wrequirement10= Requirement(pid=4, uid='JoyXuNju', rname='Easily move to next file if at end', description='The next diff command should move to the next file  (perhaps with prompting) when in directory diff mode. This would make modifications in large directories  with lots of changes easier.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement10)

    # wrequirement11= Requirement(pid=4, uid='JoyXuNju', rname='add &quot;compare files&quot; option', description='In the directory diff window, if you select a file  which is different, add the &quot;compare files&quot; options  when right clicking. Add also the same options to the menu. (I have search it a while for this functionality,  before discovering it on the documentation) Good tool, guy, go on!!',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement11)

    # wrequirement12= Requirement(pid=4, uid='JoyXuNju', rname='Suppress inital splash screen', description='I\'d like to request an option to suppress the inital  splash screen.  It introduces a delay in workflow that  I don\'t think needs to be there.  The initial setting  for this should be to show the splash screen.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement12)
    #
    # wrequirement13= Requirement(pid=4, uid='JoyXuNju', rname='which difference selected indicator', description='I wish WinMerge would display which change is  currently highlighted.  Without this it\'s easy to get  lost. In the lower right corner of the status bar, have a  bit of text that says &quot;Difference 3 of 7&quot; (when the  third difference is highlighted out of seven total).',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement13)
    #
    # wrequirement14= Requirement(pid=4, uid='JoyXuNju', rname='Search and Replace', description='Search and replace functionality in one or both files  would be a nice feature.. coming back to a project  after closing the files if they have thousands of  lines of code in each file can be time consuming.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement14)

    wrequirement15= Requirement(pid=4, uid='JoyXuNju', rname='Allow WinMerge to merge CVS conflict files', description='It would be usefull if WinMerge could parse a CVS  conflict file and allow users to visual merge the file.',
                            rtype='Capability', priority=5)
    db.session.add(wrequirement15)

    # wrequirement16= Requirement(pid=4, uid='JoyXuNju', rname='Remove empty folders from view.', description='When doing a comparison of two folders, I need to know  what files exist in one folder, but not the other. Using the Show files only in Right view will show all  folders (VC++ - Debug and Release folders) that are  empty.  An option to not show folders should be  included and the default should be off.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement16)

    wrequirement17= Requirement(pid=4, uid='JoyXuNju', rname='Compare (diff) binary files', description='Can not make a binaries diff on files. I tried on zip  files and CHM files.',
                            rtype='Capability', priority=5)
    db.session.add(wrequirement17)

    # wrequirement18= Requirement(pid=4, uid='JoyXuNju', rname='Add line numbers to the display', description='I think it would be useful to have an option to  display the line numbers in each file.  That way, when  the compiler returns &quot;error on line 1234&quot; you can  quickly check the exact location in winmerge.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement18)

    # wrequirement19= Requirement(pid=4, uid='JoyXuNju', rname='don\'t cut off long lines', description='long lines are cutted off like this \'long line [schnipp] long line...\' But if the lines differ after the dots, there is no chance to dicide if you want to merge the line or  not.The Windows is scrollable, so why cut lines off ?',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement19)

    # wrequirement20= Requirement(pid=4, uid='JoyXuNju', rname='intuitive keybord navigation', description='what would make your programm even better would be to  adopt windiffs keyboard navigation. at the moment page-down and down-key worked same for  me. i had expected that the down-key would move the  cursor (or line) down a single line. ctrl-c and ctrl-v on windiff was really great as  well :) yeah, i know \'then go and buy a copy of windiff...\'.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement20)
    #
    # wrequirement21= Requirement(pid=4, uid='JoyXuNju', rname='Show &quot;diff-region&quot; within changed line', description='WinMerge currently markups only lines that are  different (added, removed, changed).  When only a part within a line has changed, it is  often usefull to markup/highlight this &quot;difference  region&quot; of this line (in addition). This feature is also supported by other DiffTools (,  but not by all). I find this feature rather usefull.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement21)

    # wrequirement22= Requirement(pid=4, uid='JoyXuNju', rname='Drag and drop facilty', description='Draging an file icon and dropping it on the winmerge  window should prompt for the second file and open the  in winmerge window, showing the differences.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement22)

    # wrequirement23= Requirement(pid=4, uid='JoyXuNju', rname='Sort columns in the same direction', description='Now that you\'ve added the left and right file dates in  the column view, I\'d like to be able to keep the sort  of the columns in the same direction.  For example, if  I click on a column and it is sorting by descending  order, then any other column I click, except this one,  should also sort by descending order.  If I click the  same column twice in a row, then, and only then,  should the sorting direction be changed.  By default,  every column header that\'s clicked gets sorted by  ascending order.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement23)

    # wrequirement24= Requirement(pid=4, uid='JoyXuNju', rname='Browse folders in non-recursive directory compare', description='It would be nice if the differences display view would  look like Windows Explorer.  This way, the user can  open and close folders to display the changed files. If a folder exists in one and not in the other, the  folder appears in a different color.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement24)

    # wrequirement25= Requirement(pid=4, uid='JoyXuNju', rname='Open one dir in read only', description='n some cases, there is a directory you NEVER want to change (in my case, the php code directory on my web server :-)  ) I wish I could open that directory in read-only mode (by ticking a checkbox in file/open). This could be easily implemented by disabling the arrows in that direction.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement25)

    # wrequirement26= Requirement(pid=4, uid='JoyXuNju', rname='Add integration with SQL Server', description='When developing for sqlserver, we keep master copies  of sql procedures in source safe. We would like to be  able to compare the sql procedures in source safe, or  in a directory with the copies in SQL Server Databases.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement26)
    #
    # wrequirement27= Requirement(pid=4, uid='JoyXuNju', rname='Allow preprocessing of files before comparing', description='Why?:   I actually have to merge two vb project (and it\'s a  real nightmare...)  There could be a module for vb so  I could compare sub instead of whole text file...  (I  speak frech so if you don\'t understand what I mean  fell free to ask :) Unfortunately I don\'t have time free right now to  contribute',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement27)

    # wrequirement28= Requirement(pid=4, uid='JoyXuNju', rname='copy enhancement', description='Hello, Thanks for your very good tool. It is very usefull and  well done. I would like to suggest an enhancement (I\'m  a smalltalk developper ;-) ) in the copy  fonctionality. It could be bery good , like in axaris  Merger, to have the following fonctionnalities : * replace adjacent change with the change * insert this change after the adjacent change * delete the change It is usefull because we can have to make the  following thing for instance : * a developper added a new fonction * another added another fonction * we want to merge the two fonctions in one of the two  files Best regards Xavier',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement28)

    # wrequirement29= Requirement(pid=4, uid='JoyXuNju', rname='Display Differences in Tree View', description='It would be more efficient if you would display the  file and folder differences in a tree view instead of  a report view.  Have all files appear in an Explorer- like view within a tree heirarchy.  Users would then  click on the folders of interest to display which  files are different or missing.  Basically, leave all  the information as is, but just put them in a tree  directory.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement29)

    # wrequirement30= Requirement(pid=4, uid='JoyXuNju', rname='Line numbering', description='It would be nice if WinMerge could display line  numbering in the file display panes. Should be optional, set from a check box in  preferences or something like that.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement30)
    #
    # wrequirement31= Requirement(pid=4, uid='JoyXuNju', rname='Allow cancelling long operations when editing', description='It would be nice to have: 1/ Copy diff (to clipboard) on the context menu. 2/ Line indication per pan. 3/ Edit command handler using thread so a user can  cancel in case the file is large (eg: 30M+)',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement31)

    # wrequirement32= Requirement(pid=4, uid='JoyXuNju', rname='Overwrite Read-Only file', description='It would be helpfull to have a option to &quot;Overwite  Read-Only File&quot; when copying from one directory to  another.  Currently it only gives you the &quot;Save as  Another Name&quot; option.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement32)

    # wrequirement33= Requirement(pid=4, uid='JoyXuNju', rname='Custom filters in dir comparison', description='It\'d be fantastic to filter files which will be  scanned in recursive directory comparisons.  You can  already block all *.bak files which is very nice - but  it would be great to say don\'t scan _vti_cnf  directories - ignore image files etc.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement33)

    wrequirement34= Requirement(pid=4, uid='JoyXuNju', rname='Line numbers', description='It would be realy great to have the line numbers in  the left part of the files. An option that can be  checked or not.',
                            rtype='Capability', priority=5)
    db.session.add(wrequirement34)

    # wrequirement35= Requirement(pid=4, uid='JoyXuNju', rname='Configuration for Editor to be used', description='It would be useful if the editor (which is invoked  by &quot;edit file&quot;) could be (optionally) selected by  (f.e.) a regitry key; example: Key:   ..\\WinMerge\\Settings\\Editor  Value: c:\\myeditor.exe -f $F -l $L where $F  is replaced by WinMerge at runtime thru the  pathname of the file to be edited $L  is replaced by WinMerge at runtime thru the current line number (the current text-position  in the WinMerge-Window) By the way: in diff.c (exported by cvs in Feb. 2002) a function-call of diff_2_files has to few arguments: val = failed ? 2 : diff_2_files (inf, depth); instead of val = failed ? 2 : diff_2_files (inf, depth, NULL);',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement35)
    #
    # wrequirement36= Requirement(pid=4, uid='JoyXuNju', rname='Three-pane view.', description='In StarTeam, different barnches can be split off a  project to create separate projects.  It would be nice  if WinMerge can perform a three-file compare. Original and two differences.  This way, when the two  branches have to be merged in the future, the user can  compare both to the original and merge them to each  other.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement36)

    # wrequirement37= Requirement(pid=4, uid='JoyXuNju', rname='Allow editing', description='Please consider allowing interactive editing of either  pane.  If the edit causes a difference, create a new  difference on the fly.  If the edit causes a  difference to go away, clear the difference on the  fly.  I bleive the Metrowerks IDE does this, for  example.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement37)

    # wrequirement38= Requirement(pid=4, uid='JoyXuNju', rname='ignore changes base on regex', description='Please consider allowing differences to be ignored, or  highlighted differently if the changes match some  specified regular expression.   For example, if you have two documents that are almost  the same, except that everywhere &quot;Bob&quot; appears in  one, &quot;Dave&quot; appears in the other.  Oh, and there\'s one  other small change between the documents. It can be very hard to pick out the one other small  change, if the names are used frequently.  If we could  say that those common differences are ok (to ignore,  or highlight differently) then the small difference  becomes very apparent. Implementation idea:  Load document A and document B  and run the search and replace regular expressions on  document A to create (behind the scenes, in RAM)  document C. Along with doing the normal diff of A to B; do a  hidden diff of C to B.  To get the feature I\'m asking  for, you could compare the two diffs themselves (if  both show a diff then it\'s a real difference; if only  the first shows a diff, it may be ignored (or shown  differently) as a difference). P.S.  If you do this, please consider allowing this on  directory compares by applying the search and  replacements on the file/directory names. So &quot;letter_from_bob.txt&quot; would compare  to &quot;letter_from_dave.txt&quot; as if they had the same name.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement38)

    # wrequirement39= Requirement(pid=4, uid='JoyXuNju', rname='Commandline parameters', description='Could you add some commandline parameters similar to the WinDiff application. It allows for comparison of files or directories which makes it controllable for other applications.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement39)

    # wrequirement40= Requirement(pid=4, uid='JoyXuNju', rname='Better filter selection UI', description='Create a double-pane list in a new (Projects) tab in  the properties dialog.  Add two edit boxes above  those.  The left edit box adds the name of the project  below it, while the right edit box adds the names of  the files below it.  The left hand pane will be sorted  alphabetically.  This will look something like this: |-------------------| |-------------------------------| |Visual Basic       | |*.vbp;*.frm;                   | |-------------------| |-------------------------------| |-------------------| |-------------------------------| |HTML               | |*.htm;*.html;                  | |Visual C++         | |*.c;*.cpp;*.h;*.tl*;*.inl;*.rc;| |                   | |                               | |                   | |                               | |                   | |                               | |                   | |                               | |-------------------| |-------------------------------| These two lists will be added to the open dialog\'s  extension\'s list at the very top.  This can be used as  a filtering setting instead of or in addition to the  normal history filtering that is currently in use.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement40)
    #
    # wrequirement41= Requirement(pid=4, uid='JoyXuNju', rname='Source Control', description='When using Visual Studio to check in/out files from  source control, all you have to do is use the  SourceControl toolbar to check in/out the files you  need no matter which source control software you use. It would be nice if Winmerge could use these same  macros to check in/out the files using any source  control.  This would allow for a generic way of  checking in/out files and users no longer need to  determine which software to use.  The registry key  that determines which application to use for source  control is located in: [HKEY_LOCAL_MACHINE\\SOFTWARE\\SourceCodeControlProvider] &quot;ProviderRegKey&quot;=&quot;Software\\\\Starbase\\\\MSIntegration3&quot;. We use StarTeam.  The rest are located under: [HKEY_LOCAL_MACHINE\\SOFTWARE\\SourceCodeControlProvider\\ InstalledSCCProviders] &quot;Microsoft Visual  SourceSafe&quot;=&quot;Software\\\\Microsoft\\\\SourceSafe&quot; &quot;StarTeam Source Code  Control&quot;=&quot;Software\\\\Starbase\\\\MSIntegration3&quot;.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement41)

    wrequirement42= Requirement(pid=4, uid='JoyXuNju', rname='Line numbers display', description='Hello, It should be a nice addittion that optional line  numbers are displayed in both of th files. rgds, Wilfried http://www.mestdagh.biz',
                            rtype='Capability', priority=5)
    db.session.add(wrequirement42)

    # wrequirement43= Requirement(pid=4, uid='JoyXuNju', rname='Display word diffs inside difference', description='Hi, One really nice feature that the emacs GUI diff  function had that I have not seen in any other GUI  diff program is that when you went to see each  difference, it would do a wdiff on the contents, and  highlight the word differences in a third color. So if  the lines were different because of a minor change, it  was immediately obvious just by looking at the small  section in the third color.  Unfortunately I don\'t have an MS dev environment  anymore, or I would implement it myself. Could you  please implement a feature like that in WinMerge?  If you need better explanation of the functionality,  or screenshots of it, let me know.  Thanks, Kevin',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement43)

    # wrequirement44= Requirement(pid=4, uid='JoyXuNju', rname='Add drag and drop support', description='rag and drop support for WinMerge would be a  beautiful addition, since it\'s much easier to browse  in, say, Explorer rather than in the Open File dialog  box. Extra, those who use tools such as Windows  Commander could easily see two folders at once and  drag files from those folders at their own discretion. Thanks',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement44)

    # wrequirement45= Requirement(pid=4, uid='JoyXuNju', rname='A few buttons enhancements', description='Here are a few enhancements I suggest, with regards to  buttons: 1. It seems to me more logical that the &quot;Previous  diff&quot; button (arrow up) comes before the &quot;Next diff&quot;  button. 2. &quot;Copy to right&quot; and &quot;Copy to left&quot; would seem more  appropiate for the &quot;Copy right&quot; and &quot;Copy left&quot;  buttons. Idem for &quot;All right&quot; and &quot;All left&quot; 3. It would be nice if there were also buttons  for : &quot;Insert to R/L&quot; (allowing to keep the modified  text and to also insert the difference) and &quot;Delete  R/L&quot; to delete a text that is wrong from either right  or left (this is usefull when someone added a debug  statement and one wants to remove it). Thanx.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement45)
    #
    # wrequirement46= Requirement(pid=4, uid='JoyXuNju', rname='configurable colors', description='I would really like to have highlight colors be configurable in &quot;Edit/Properties&quot;. Black text on red background is really hard to read on my monitor - the old one (white text on blue background) was much easier to read. This configuration can be added to &quot;Edit/Properties/Highlight&quot;. A more ambitious change would be to make all colors in the editor configurable.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement46)
    #
    # wrequirement47= Requirement(pid=4, uid='JoyXuNju', rname='Warn of other editors on edit command', description='It would be convenient to have the option to be  warned of other editors when you use the edit option  for a file. A dialog might pop up indicating others who  are editing the file concurrently, or if this is seems to  be difficult, just a dialog that indicates that others are  editing the file. The dialog might allow you to edit  anyway, or cancel the edit request. I find that it is  helpful to know when someone else is editing a file,  but it is annoying having to check editors every time  before you use the editors option. Having this done  automatically and transparently would be really  convenient.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement47)
    #
    # wrequirement48= Requirement(pid=4, uid='JoyXuNju', rname='Command Line File Descriptors', description='I am using WinMerge with a 3rd party VCS tool that can  pass file names and file descriptors as command line  params. WinMerge seems to only accept two file name  params. For example, it would be nice to see: &quot;MyFile.txt Revision 1.2&quot; || &quot;MyFile.txt Revision 1.3&quot; as  file descriptors instead of the long temporary path/file  names that the VCS tool creates. The VCS tool passes 4 params (can be in any order): &quot;$LF&quot; &quot;$LD&quot; &quot;$RF&quot; &quot;$RD&quot; ,  which are Left File, Left Descriptor, Right File, Right  Descriptor.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement48)

    wrequirement49= Requirement(pid=4, uid='JoyXuNju', rname='scrolling options', description='There should be an option to a)scroll both files at the same time with one scrollbar b)scroll only one file',
                            rtype='Capability', priority=5)
    db.session.add(wrequirement49)

    # wrequirement50= Requirement(pid=4, uid='JoyXuNju', rname='Unicode encoding support', description='The diff engine seemed to support utf-8 as lond as the  BOM is not at the beginning of the file (which is a bit of  a pain since Win OS append it all the time). The diff engine does not support utf-16 BE',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement50)

    wrequirement51= Requirement(pid=4, uid='JoyXuNju', rname='Show Line Numbers in margin', description='Small request, but it would be convient to have the  ability to switch on/off line numbers.',
                            rtype='Capability', priority=5)
    db.session.add(wrequirement51)
    #
    # wrequirement52= Requirement(pid=4, uid='JoyXuNju', rname='Show which files is newer', description='It would be great if as well as &quot;files are different&quot; you  could display the message &quot;Left is newer&quot; or &quot;Right is  newer&quot;, souly based ont he files modified date. Or something simular.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement52)

    # wrequirement53= Requirement(pid=4, uid='JoyXuNju', rname='Windows not scrollable enough', description='Long lines can not be infinitly scrolled (as ina nyother  win app) It would appear the author has hardcoded the  witdth applicable to the scrollbars :(',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement53)

    # wrequirement54= Requirement(pid=4, uid='JoyXuNju', rname='open files over HTTP', description='Trying to help our QA staff track changes to a very large  corporate site with many different environments. It would  be very useful to give them a quick way of comparing a  page in development environment to a page in  production environment.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement54)

    # wrequirement55= Requirement(pid=4, uid='JoyXuNju', rname='Add horizontal diff area', description='Even when using high-resolution monitors, most of my  difference lines extend beyond the display area. It is  sometimes difficult to see the differences for these lines -  especially for the right-hand file. I suggest adding (an optional) third area to the &quot;File  Comparison&quot; window - in addition to the 2 file areas. The  third area would be at the bottom of the &quot;File Comparison&quot;  window, spanning the whole horizontal area of the window.  In the file areas, if I click on any line with a difference, the  left-hand difference line would show in the new third area  over top of the right-hand difference line. (See included  example image.) Displaying a difference line in this fashion also makes  finding the differences on similar lines easier, since the  differences are physically closer together. If inline difference indicators are added to WinMerge, it  would be good to include those indicators in the new  display area also. Scott Carlson scarlson@columbus.rr.com btw. WinMerge is the best differences program I have  found.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement55)

    # wrequirement56= Requirement(pid=4, uid='JoyXuNju', rname='Problems and suggestions', description='I find Winmerge to be an extremely useful product. Bravo to the developers. Here are some remarks in order to make it still better: Problems using Winmerge: 1. Sometimes the diff gets out of phase in File Comparison, and outlines the lines following the diff, rather than the diff itself. 2. When replacing a large selection by a small one, the extra empty lines are still displayed Suggestions for improvements: 1. Add an Undo option 2. Add line numbers in the File Comparison display, as an option. Even when the option is off, always display the left &amp; right line numbers in the status bar. 3. When re-diff\'ing directories - close first the current File Comparison window 4. Start Winmerge with the Directory Comparison window maximized to the entire Winmerge window 5. Allow up/down arrows for moving in Directory Comparison 6. Add Store-and-rediff option for File Comparison display 7. Very vague: allow partial modifs. This means, for example, choosing which lines from one file are going to replace which lines in the other file Yours Harry McKame mckameh1@armadillo.fr',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement56)

    # wrequirement57= Requirement(pid=4, uid='JoyXuNju', rname='Print difference report', description='Feature request: It would be very helpful to be able to print difference reports.  I particularly need this functionality for directory comparisons, but it might also prove useful in file comparisons.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement57)

    # wrequirement58= Requirement(pid=4, uid='JoyXuNju', rname='Save directory compare report', description='Feature request:  Save difference report Particularly for directory comparisons, capability to save in some format a list of which files have changed. This could be as simple as an ASCII text list of filenames, although a CSV or HTML table with the full contents of the directory comparison page would be even better.  Currently the only workaround I have seen is to take a screen capture of the comparison page and save it as a .PNG; that\'s not a very useful workaround.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement58)

    # wrequirement59= Requirement(pid=4, uid='JoyXuNju', rname='Recompute difference', description='When the directory comparation is used it would be very  nice to be able to recompute the difference list. This is often used when you fix som differences and  wants to see the new result.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement59)

    # wrequirement60= Requirement(pid=4, uid='JoyXuNju', rname='Hide Binary Files that are Different', description='Would like and option added under the View menu that  will hide all of the files that are listed as &quot;Binary files are  Different&quot; like the option to hide the *.BAK files.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement60)

    # wrequirement61= Requirement(pid=4, uid='JoyXuNju', rname='Improved file extension filtering &amp; auto move to next diff', description='Greetings, I\'ve included a couple of images of changes I\'ve made to  a somewhat older version of Winmerge that I thought  would be useful in the current release.  The Projects.jpg  file shows a couple of listboxes that can be used to  create filter extensions in addition to the current one  available in the Open dialog box.  This just saves time  when dealing with certain developer projects. Bassam Abdul-Baki',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement61)
    #
    # wrequirement62= Requirement(pid=4, uid='JoyXuNju', rname='Folder diff like file diff', description='SourceSafe does it really well: Pretty much treat folder diff to have the exact same  interface as file diff: show a 2 pane window. On the left pane is the left  directory, on the right pane is the right directory If a file is in both directories but are different, the  background is colored with the difference color If a file is in both directories and is identical, the  background is white If a file is only in the left directory, show the file on  the left with a difference background and an empty  gray space on the right If a file is only in the right directory, show the file  on the right with a difference background and an  empty gray space on the left Navigating between differences would be  completely identical to navigating differences in  files: alt up/down arrow Copying a file from left to right/right to left alt right/left The View options would still be valid: Show Identical/Different/Left Unique/Right Unique All in all it would make a much more consistant  overall interface and much more intuitive for a new  user who would have to learn only one type of  interface. Plus I never know if the right arrow on  the files mean the file is unique on the right or if it  will copy it to the right. I also never remember  which folder is right and which is left. Plus this view would also be compatible with the  tree view suggested in another RFE which I think is  a brilliant suggestion. Thanks for the great software!',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement62)
    #
    # wrequirement63= Requirement(pid=4, uid='JoyXuNju', rname='User-selectable columns as in Explorer', description='I suggest going from the current fixed set of columns, to an adjustable set of columns, including some new ones such as Right Size, Left Size, Right Created, Left Created; i.e., taking some of the useful column choices from the choices available in Windows Explorer. I believe this would interoperate well with multicolumn sorting for the list control. I have a module to do that, which I could introduce. Click on a column to sort on it, but then ctrl-click on another column to select it as a secondary key, etc.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement63)
    #
    # wrequirement64= Requirement(pid=4, uid='JoyXuNju', rname='Mark file (to hide diff)', description='I\'d like right-click Mark file and in the view options, a View Marked items which is by default not checked, so that when I finish reviewing diffs in a file, I can Mark it, and it will disappear from the display. So as I work through items, they disappear, even if I do not perfectly reconcile them. Or maybe the verb should be &quot;Hide&quot;. right-click Hide item and at top, View Hidden Items (I just propose this as a safeguard to be able to get back all the items you hid)',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement64)

    wrequirement65= Requirement(pid=4, uid='JoyXuNju', rname='Diff navigation buttons should work in directory view', description='I think the &quot;scoll to the next/previous/first/last&quot; difference  buttons should work when viewing the directory diff window.',
                            rtype='Capability', priority=5)
    db.session.add(wrequirement65)

    # wrequirement66= Requirement(pid=4, uid='JoyXuNju', rname='Suggestion: add line numbers in File Comparison display', description='Suggest adding line numbers in the File Comparison display, as an option. Even when the option is off, should always display the left &amp; right line numbers in the status bar This item is also contained in Support Requests item #667648.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement66)

    # wrequirement67= Requirement(pid=4, uid='JoyXuNju', rname='Suggestion: re-diff to close File Comparison window', description='Suggest when re-diff\'ing directories to close first the current File Comparison window This item is also contained in Support Requests item #667648.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement67)
    #
    # wrequirement68= Requirement(pid=4, uid='JoyXuNju', rname='Directory compare window should remember its state', description='Suggest start Winmerge with the Directory Comparison window maximized to the entire Winmerge window This item is also contained in Support Requests item #667648.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement68)

    wrequirement69= Requirement(pid=4, uid='JoyXuNju', rname='Suggestion: up/down arrows in Directory Comparison', description='Suggest allow up/down arrows for moving in Directory Comparison. This item is also contained in Support Requests item #667648.',
                            rtype='Capability', priority=5)
    db.session.add(wrequirement69)

    wrequirement70= Requirement(pid=4, uid='JoyXuNju', rname='Suggest: Store-and-rediff for File Comparison', description='Suggest add Store-and-rediff option for File Comparison display. This item is also contained in Support Requests item #667648.',
                            rtype='Capability', priority=5)
    db.session.add(wrequirement70)

    # wrequirement71= Requirement(pid=4, uid='JoyXuNju', rname='Suggestion: allow partial modifs (per line merge)', description='Suggest allowing partial modifs. This means, for example, choosing which lines from the one file are going to replace which lines in the other file. The user interface can be very simple: select a range of lines on the left, another range on the right, then issue the replace. An option for &quot;Insert before/after selection&quot; should be welcome as well. This item is also contained in Support Requests item #667648.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement71)

    # wrequirement72= Requirement(pid=4, uid='JoyXuNju', rname='Add Windows Explorer shell integration', description='Hello, It could be nice if WinMerge could integrate with  Windows Explorer. For example, I would like to select two files in a  directory, then open the contextual menu and  select &quot;WinMerge&quot; for opening WinMerge with  differences between the two files. Idem with two directories. If it\'s too long to get this feature, it could be nice to have  the possibility to drag and drop two files in the  WinMerge application window and have the two files  compared. Thanks. Adriano Labate',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement72)
    #
    # wrequirement73= Requirement(pid=4, uid='JoyXuNju', rname='Show whitespace in editor', description='CrystalEditor supports showing whitespaces (spaces and tabs) as visible chars.  Like most editors do. This is useful for WinMerge too.  So let\'s enable it. I will ad &quot;View Whitespace&quot; item to &quot;View&quot; menu. I have working code for this.  Patch coming tomorrow.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement73)

    # wrequirement74= Requirement(pid=4, uid='JoyXuNju', rname='Save As...', description='I don\'t always want to overwrite existing files.  Instead I want to save new edited file to different name. So I\'m suggesting adding &quot;Save As...&quot; item to &quot;File&quot; menu.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement74)

    # wrequirement75= Requirement(pid=4, uid='JoyXuNju', rname='Save Left &amp; Save Right', description='WinMerge saves both files when saving.  There should be possibility to save only left or right file.  When merging files you can (accidentally, by mistake...) edit file you definitely do not want to edit.  And then what?  Saving saves both files, and that you do not want to do?  Close WinMerge without saving and lose all changes? Currently one (and only?) way around this is to not save, but close window.  Then WinMerge asks if you want to save left file and then if you want to save right file. I\'m suggesting adding &quot;Save Left&quot; &amp; &quot;Save Right&quot; to &quot;File&quot; menu.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement75)

    # wrequirement76= Requirement(pid=4, uid='JoyXuNju', rname='Save Left &amp; Save Right', description='WinMerge saves both files when saving.  There should be possibility to save only left or right file.  When merging files you can (accidentally, by mistake...) edit file you definitely do not want to edit.  And then what?  Saving saves both files, and that you do not want to do?  Close WinMerge without saving and lose all changes? Currently one (and only?) way around this is to not save, but close window.  Then WinMerge asks if you want to save left file and then if you want to save right file. I\'m suggesting adding &quot;Save Left&quot; &amp; &quot;Save Right&quot; to &quot;File&quot; menu.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement76)
    #
    # wrequirement77= Requirement(pid=4, uid='JoyXuNju', rname='Save Left &amp; Save Right', description='WinMerge saves both files when saving.  There should be possibility to save only left or right file.  When merging files you can (accidentally, by mistake...) edit file you definitely do not want to edit.  And then what?  Saving saves both files, and that you do not want to do?  Close WinMerge without saving and lose all changes? Currently one (and only?) way around this is to not save, but close window.  Then WinMerge asks if you want to save left file and then if you want to save right file. I\'m suggesting adding &quot;Save Left&quot; &amp; &quot;Save Right&quot; to &quot;File&quot; menu.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement77)
    #
    # wrequirement78= Requirement(pid=4, uid='JoyXuNju', rname='On merging current diff, autoscroll to the next diff', description='Instead of having a scroll to first diff checkbox, it should be an autoscroll checkbox. On merging the current diff, if the autoscroll option is selected, the app should automatically scroll to the next diff. The user does not need to click on the &quot;Next Diff&quot; option.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement78)
    #
    # wrequirement79= Requirement(pid=4, uid='JoyXuNju', rname='Optional dialogbars for filenames &amp; current line', description='I\'d like two optional dialogbars. #1) Displaying both fully qualified filenames (of currently displayed files) in editboxes, so I can easily check or copy the current filenames (stacked vertically so each editcontrol gets full width) #2) Displaying the current lines from both sides (stacked vertically so each line display gets full width) Both of these are for cases when the filenames or lines are sufficiently long that they wrap. A dialogbar with editcontrols stacked vertically would give me a view of the line or filename that is as wide as I can make my application, rather than less than half that width (because filenames in statusbar and lines in editor both get less than half the app width). the file names',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement79)

    # wrequirement80= Requirement(pid=4, uid='JoyXuNju', rname='Generate and apply patches', description='This would be a great GUI to generate and apply patch  files, with some nice features: * generate patch from diff * apply patch and resolve conflicts interactively * edit the operations in a patch file * generate an &quot;undo&quot; patch during manual edits of a  directory tree * generate a &quot;redo&quot; patch during manual edits of a  directory tree',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement80)
    #
    # wrequirement81= Requirement(pid=4, uid='JoyXuNju', rname='right-click &quot;Copy Path name(s)&quot;', description='I\'d like  Copy path name(s) and Copy file name(s) on the right-click menu from the main (directory) list, which would copy the name(s) of the selected item(s) to the clipboard. I\'m thinking that multiple names would be put on with carriage returns between them.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement81)
    #
    # wrequirement82= Requirement(pid=4, uid='JoyXuNju', rname='need a EXCLUDE filter', description='when I compare directories, I don\'t want the .class files  to be included.  An EXCLUDE filter would be a nice  addition.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement82)

    wrequirement83= Requirement(pid=4, uid='JoyXuNju', rname='Display only different lines', description='Add possibility to hide lines which are identical in both texts.',
                            rtype='Capability', priority=5)
    db.session.add(wrequirement83)

    # wrequirement84= Requirement(pid=4, uid='JoyXuNju', rname='Copy/Cut/Paste should ignore removed lines', description='Currently when doing Copy/Cut/Paste removed lines are included as empty lines. This is annoying and makes copying changes harder.  If you copy changed lines to another pane, removed lines are copied as empty lines and are seen as a difference then...',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement84)

    # wrequirement85= Requirement(pid=4, uid='JoyXuNju', rname='Possibility to not add commandline paths to MRU list', description='When using WinMerge as external diff program files are usually loaded from $temp directory.  After working a while MRU list is full of temp files. It should be possible to not add these $temp paths to MRU.  Files are removed from there anyway. Maybe best would be to add one or two new commandline switches.  One switch could prevent adding both paths to MRU or with two switches just another (or both) are not added to MRU.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement85)

    # wrequirement86= Requirement(pid=4, uid='JoyXuNju', rname='Support mac linefeeds', description='I have a platform which supports only mac linefeeds (single \\r) and it would be great to be able to use WinMerge for comaparing also those files.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement86)

    # wrequirement87= Requirement(pid=4, uid='JoyXuNju', rname='proportional fonts no longer available?', description='In 1.7.1 I used Arial in the File Comparison window, to  show as many characters as possible. 1.9.1.4 has some nice new features, but the Font  choices are limited to Fixed Pitch. Was this possibly necessary for the new in-place editing  or synchronized horizontal scrolling features? My workaround is to change FaceName in the registry. It messes up in-place editing, but that\'s OK for me - I  edit elsewhere anyway. Suggestion: If in-place editing is too hard with  proportional fonts, allow a non-Editing option that  supports proportional fonts.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement87)

    # wrequirement88= Requirement(pid=4, uid='JoyXuNju', rname='Compare binary files', description='Hi  The WinMerge executable (ver 1.9.1.4) provided  by &quot;amores perros&quot; is not providing the result as per  expectation. On selecting the files, the software reports  loads both the text file in the window and displays the  message &quot;Binary Files are different&quot;. When the OK  button is clicked no differences are displayed. Original problem reported : WinMerge is unable to identify difference between two  2meg text files. The difference is in line 30458 (2  character). Version of WinMerge used :1.7.1.222. OS is  Win2000. Memory is 254MB. Files are simple Text  files. &quot;Diff&quot; command shipped with WinCVS reports the  difference correctly. Would be very grateful if WinMerge problem is sorted  quickly. Note : Since only one file can be attached, I have  attached the Zipped version of the files. You need to  unzip the file to create comp1.txt and comp2.txt and  then use WinMerge to compare the same. Thanks Saurabh_Das@yahoo.com',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement88)

    # wrequirement89= Requirement(pid=4, uid='JoyXuNju', rname='Directory Synchronizer', description='First of all, thanks man, thanks for writing such a good  piece of software. I\'m look for a program which synchronizes 2 directories.  I think that WinMerge is a good program for  synchronizing the content in 2 files and it has a good  potential to be a useful DIrectory Synchronization tool -  the feature should be added to WInMerge is &quot;Directories  Comparison&quot; based on Modified Date &amp; Time  and &quot;Coping Files&quot; within the program. Don\'t you think  that?',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement89)
    #
    # wrequirement90= Requirement(pid=4, uid='JoyXuNju', rname='Dir Comp - based on Modified Date', description='First of all, thanks man, thanks for writing such a good  piece of software. I\'m look for a program which synchronizes 2 directories.  I think that WinMerge is a good program for  synchronizing the content in 2 files and it has a good  potential to be a useful DIrectory Synchronization tool -  the feature should be added to WInMerge is &quot;Directories  Comparison&quot; based on Modified Date &amp; Time  and &quot;Coping Files&quot; within the program. Don\'t you think  that?',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement90)

    # wrequirement91= Requirement(pid=4, uid='JoyXuNju', rname='Directories Synchronizer', description='First of all, thanks man, thanks for writing such a good  piece of software. I\'m look for a program which synchronizes 2 directories.  I think that WinMerge is a good program for  synchronizing the content in 2 files and it has a good  potential to be a useful DIrectory Synchronization tool -  the feature should be added to WInMerge is &quot;Directories  Comparison&quot; based on Modified Date &amp; Time  and &quot;Coping Files&quot; within the program. Don\'t you think  that?',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement91)

    # wrequirement92= Requirement(pid=4, uid='JoyXuNju', rname='multiple actions', description='Firstly great tool, When working in the directory compare it would be  really helpful if you could select multiple items and  perfrom the action on all items rather than having to do  each one individually. ie select three files and say copy  to a location. thanks Andy',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement92)

    # wrequirement93= Requirement(pid=4, uid='JoyXuNju', rname='BETA: Minor: \'Window\' menu doesn\'t list all open windows', description='I maximize the directory comaprison display window. When I double-click a file pair to diff, the diff window is  also maximized. To get back to the directory display, I must either kill the  diff window or use Ctrl-Tab to switch windows. All open windows should be listed under the &quot;Window&quot;  menu.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement93)

    # wrequirement94= Requirement(pid=4, uid='JoyXuNju', rname='Obey Scroll to first difference property for dir compare', description='Directory compare does not check &quot;Automatically scroll to first difference&quot; property.  It should.  If that property is set, we should scroll to first different file.  Consistency is a good thing.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement94)

    wrequirement95= Requirement(pid=4, uid='JoyXuNju', rname='drag and drop', description='It would be really cool if dragging two files into winmerge would start a diff',
                            rtype='Capability', priority=5)
    db.session.add(wrequirement95)

    # wrequirement96= Requirement(pid=4, uid='JoyXuNju', rname='Notice if file on disk changes underneath us', description='Track last modification time of files we\'re editing, and check it when we save files, so we notice if the files change underneath us, and can warn user. &quot;Another program has changed this file since WinMerge loaded it. If you proceed, WinMerge will overwrite the copy on disk with the copy WinMerge has. OK/Cancel&quot;',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement96)

    wrequirement97= Requirement(pid=4, uid='JoyXuNju', rname='Line Numbers', description='would like the option of viewing line numbers in files',
                            rtype='Capability', priority=5)
    db.session.add(wrequirement97)

    # wrequirement98= Requirement(pid=4, uid='JoyXuNju', rname='diff files with local folder and ftp', description='When programming web projects it\'s realy need for synhronizing files between remote servers or with remote server and local directory. So it would be realy great if there would be built in ftp client for doing such sinhronizations.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement98)

    # wrequirement99= Requirement(pid=4, uid='JoyXuNju', rname='Select &amp; copy multiple files in directory-wise comparison', description='When doing a directory wise comparison, it would  be very helpful if one could just select multiple  files and copy them to the other directory you are  looking at.  At the moment I have to do them one  at a time, or I have to find the files again in  Windows Explorer, and copy the files there.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement99)

    # wrequirement100= Requirement(pid=4, uid='JoyXuNju', rname='Option to delete files in directory-wise comaparison', description='It would be very useful to be able to delete files  that only exist in one pane of the comparison  window or the other.  Sometimes you do mean to  delete the files, but later have to synchronise with  another directory, but winmerge currently only  allows you to copy the files.  At the moment I have  to close Winmerge and then use explorer to delete  the files on the other directory after Winmerge has  told me which ones don\'t exist.',
    #                         rtype='Capability', priority=5)
    # db.session.add(wrequirement100)

    drequirement1 = Requirement(pid=5, uid='JoyXuNju', rname='Fully automated operation',
                                description='Is it possible to release a version for the RiSC chipset',
                                rtype='Capability', priority=5)
    db.session.add(drequirement1)

    drequirement2 = Requirement(pid=5, uid='JoyXuNju', rname='sata support',
                                description='I get errors with cdrom version and sata hard drive',
                                rtype='Capability', priority=5)
    db.session.add(drequirement2)

    drequirement3 = Requirement(pid=5, uid='JoyXuNju', rname='CESG Approval',
                                description='Does dban plan on going for CESG approval',
                                rtype='Capability', priority=5)
    db.session.add(drequirement3)

    drequirement4 = Requirement(pid=5, uid='JoyXuNju', rname='Emergency Stop Key',
                                description='There should be a key combination that serves as an emergency stop',
                                rtype='Capability', priority=5)
    db.session.add(drequirement4)

    drequirement5 = Requirement(pid=5, uid='JoyXuNju', rname='Dell 745',
                                description='Does not recognize the disks in the new Dell 745 series',
                                rtype='Capability', priority=5)
    db.session.add(drequirement5)

    drequirement6 = Requirement(pid=5, uid='JoyXuNju', rname='SPARC support',
                                description='Support for erasing sun SPARC systems',
                                rtype='Capability', priority=5)
    db.session.add(drequirement6)

    drequirement7 = Requirement(pid=5, uid='JoyXuNju', rname='FPS limitator',
                                description='I really want something that limits the FPS to 60',
                                rtype='Capability', priority=5)
    db.session.add(drequirement7)

    drequirement8 = Requirement(pid=5, uid='JoyXuNju', rname='Alphablending and other effects',
                                description='Alphableding and other effects should be supported',
                                rtype='Capability', priority=5)
    db.session.add(drequirement8)

    db.session.commit()
    with open(lock_file, 'w') as file:
        file.write("Data has already been inserted")
