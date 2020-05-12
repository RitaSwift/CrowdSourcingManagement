/**
 * 登录
 */
function login() {
    var submit = $("#loginSubmit");

    var inputUid = $("#inputUid");
    var inputPassword = $("#inputPassword");

    var uid = inputUid.val();
    var password = hex_md5(inputPassword.val());

    var data = {uid: uid, password: password};

    $.ajax({
        url: '/login',
        data: data,
        type: 'POST',
        dataType: 'text',
        beforeSend: function () {
            submit.attr('disabled', 'disabled');
            submit.text('登录中...');
        },
        success: function(msg){
            if(msg === "fail"){
                alert("用户名或密码错误，登录失败");
                // console.log(msg)
                window.location.reload()
            }else if(msg === "success") {
                if(getUrlRelativePath() === "/login"){
                    window.location.href = "/";
                }else{
                    window.location.reload();
                }
            }
        },
        error: function (exc) {
            alert("发生错误，请重试");
            window.location.reload();
            console.log(exc);
        },
        complete: function () {
            submit.removeAttr('disabled');
            submit.text('登录');
        }
    });

    return false;
}
/**
 * 注册
 */
function register() {
    let submit = $("#registerSubmit");

    let inputUid = $("#inputUid");
    let inputPassword = $("#inputPassword");
    let inputRePassword = $("#inputRePassword");
    let inputName = $("#inputName");
    let inputTelephone = $("#inputTelephone");
    let inputEmail = $("#inputEmail");
    let inputOccupation = $("#inputOccupation");
    let inputIntroduction = $("#inputIntroduction");

    let uid = inputUid.val();
    let password = hex_md5(inputPassword.val());
    let rePassword = hex_md5(inputRePassword.val());
    let name = inputName.val();
    let telephone = inputTelephone.val();
    let email = inputEmail.val();
    let occupation = inputOccupation.val();
    let introduction = inputIntroduction.val();

    let data = {uid:uid, password: password, rePassword:rePassword, name:name,
        telephone:telephone, email:email, occupation:occupation, introduction:introduction};

    $.ajax({
        url: '/register',
        data: data,
        type: 'POST',
        dataType: 'text',
        beforeSend: function () {
            submit.attr('disabled', 'disabled');
            submit.text('注册中...');
        },
        success: function(msg){
            if(msg === "uid_existed"){
                alert("用户名已存在，注册失败");
                window.location.reload();
                return false;
            }else if(msg === "wrong_uid_pattern"){
                alert("用户名格式错误");
                window.location.reload();
                return false;
            }else if(msg === "wrong_password_length"){
                alert("密码未经加密");
                window.location.reload();
                return false;
            }else if(msg === "different_password"){
                alert("两次输入的密码不同");
                window.location.reload();
                return false;
            }else if(msg === "wrong"){
                alert("注册错误，请重试");
                window.location.reload();
                return false;
            }else if(msg === "fail"){
                alert("注册失败，请重试");
                window.location.reload();
                return false;
            }else if(msg === "success") {
                alert("注册成功！");
                window.location.href="/login"
            }
        },
        error: function (exc) {
            alert("Something wrong, please try again.");
            window.location.reload();
            console.log(exc);
        },
        complete: function () {
            //让登陆按钮重新有效
            submit.removeAttr('disabled');
            submit.text('注册');
        }
    });

    return false;
}

/**
 * 修改个人信息
 */
function modifyUserInfo() {
    $.ajax({
        url: '/userInfo/modify',
        data: $("#userInfoForm").serialize(),
        type: 'POST',
        success: function(msg){
            if(msg === "fail"){
                alert("修改失败，请重试");
                return false;
            }else if(msg === "success") {
                alert("修改成功");
                window.location.reload();
            }
            else if (msg === 'uid_existed') {
                alert('用户名已经存在');
            }
        },
        error: function (exc) {
            alert("发生错误，请重试");
            console.log(exc);
        }
    });

    return false;
}

/**
 * 修改密码
 */
function changePassword() {

    let inputOldPassword = $("#inputOldPassword");
    let inputNewPassword = $("#inputNewPassword");
    let inputRePassword = $("#inputRePassword");

    let oldPassword = hex_md5(inputOldPassword.val());
    let newPassword = hex_md5(inputNewPassword.val());
    let rePassword = hex_md5(inputRePassword.val());
    console.log(newPassword+"  "+rePassword);
    if (newPassword !== rePassword) {
        alert("两次密码不一致");
    }
    let data = {oldPassword: oldPassword, newPassword: newPassword};

    $.ajax({
        url: '/userInfo/doChangePassword',
        data: data,
        type: 'POST',
        success: function(msg){
            if(msg === "fail"){
                alert("旧密码错误，请重试");
                window.location.reload();
                return false;
            }else if(msg === "success") {
                alert("密码修改成功");
                window.location.href="/userInfo";
            }
        },
        error: function (exc) {
            alert("发生错误，请重试");
            console.log(exc);
            window.location.reload();
        }
    });

    return false;
}
