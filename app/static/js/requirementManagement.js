/**
 * 进入筛选需求
 * @param pid
 */
function goToFiltrateRequires(pid) {
    window.location.href = '/filtrateRequires?pid=' + pid;
}

/**
 * 跳转筛选结果页
 * @param pid
 */
function goToFiltrateResult(pid) {
    window.location.href = '/filtrateResult?pid=' + pid;
}

/**
 * 下载文档
 * @param pid
 */

function downloadDoc(pid) {
    window.location.href = '/downloadDoc?pid=' + pid;
}

/**
 * 全选
 */

function selectAll() {
    let checkboxes = $('input[type="checkbox"]');
    checkboxes.prop('checked', true);
}

function cancelAll() {
    let checkboxes = $('input[type="checkbox"]');
    checkboxes.prop('checked', false);
}

/**
 * 跳转到生成优先级和分类的界面
 * @param pid
 */

function goToPriorityAndClass(pid) {

    let checkedbox = $('input[type="checkbox"]:checked');
    if (checkedbox.length === 0) {
        alert("请至少选择一个需求！");
    } else {
        let rid = [];
        for (let i = 0; i < checkedbox.length; i++) {
            rid.push(checkedbox[i].nextElementSibling.value);
        }
        let data = {
            'selected': rid
        };
        console.log(JSON.stringify(data));
        $.ajax({
            url: '/selectRequirement?pid=' + pid,
            data: JSON.stringify(data),
            type: 'POST',
            contentType: 'application/json',
            dataType: 'text',
            success: function (msg) {
                if (msg === 'success') {
                    window.location.href = '/priorityAndClass?pid=' + pid + "&page=1"
                }
            },
            error: function () {
                alert("Error");
            }
        })

    }

    // if(!isCheck){
    // alert("请至少选中一个！");
    // }else{
    // alert("进入下一步");
    //   window.location.href = '/priorityAndClass?pid=' + pid + "&page=1";
    // }
//    alert("check+"+ cond);
//        var isCheck=$("#check").get(0).checked;//获取选中状态，返回true或者false

}

