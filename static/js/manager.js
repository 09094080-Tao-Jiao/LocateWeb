/**
 * 根据showQueryMark值2，改变隐藏状态
 *
 */
function changeShow() {
    var queryMoreObj = document.getElementById("queryMore");
    var moreQuery = document.getElementById("moreQuery");
    var littleQuery = document.getElementById("littleQuery");
    if ( document.getElementById("showQueryMark").value != "2") {
        queryMoreObj.style.display = "none";
        littleQuery.style.display = "none";
        moreQuery.style.display = ""
    } else {
        queryMoreObj.style.display = "";
        littleQuery.style.display = "";
        moreQuery.style.display = "none";
    }
}
/**
 * 更多查询执行，点击更多查询，将showQueryMark赋值为2
 *
 */
function getMoreQuery() {
    document.getElementById("showQueryMark").value = "2";
    $("#queryMore").css("display", "");
    $("#moreQuery").css("display", "none");
    $("#littleQuery").css("display", "");
}

/**
 * 简要查询执行，点击简要查询，将showQueryMark赋值为1
 *
 */
function setLittleQuery() {
    document.getElementById("showQueryMark").value = "1";
    $("#queryMore").css("display", "none");
    $("#moreQuery").css("display", "");
    $("#littleQuery").css("display", "none");
}


var myview = $.extend({},$.fn.datagrid.defaults.view,{
onAfterRender:function(target){
        $.fn.datagrid.defaults.view.onAfterRender.call(this,target);
        var opts = $(target).datagrid('options');
        var vc = $(target).datagrid('getPanel').children('div.datagrid-view');
        vc.children('div.datagrid-empty').remove();
        if (!$(target).datagrid('getRows').length){
            var d = $('<div class="datagrid-empty"></div>').html(opts.emptyMsg || 'no records').appendTo(vc);
            d.css({
                position:'absolute',
                left:0,
                top:50,
                width:'100%',
                textAlign:'center'
            });
        }
    }
});

/**
 * 页面初始化
 *
 */

$(function () {

    //初始化隐藏区域状态
    var showQueryMark = document.getElementById("showQueryMark");
    if (!showQueryMark || showQueryMark.value != "2") {
        $("#queryMore").css("display", "none");
        $("#moreQuery").css("display", "");
        $("#littleQuery").css("display", "none");

    } else {
        changeShow();
    }

    $('#etprdp').combobox({
        valueField : 'value',
        textField : 'text',
        url : '../manager/etprdp',
        method:'GET',
    });

    $('#software').combobox({
        valueField : 'value',
        textField : 'text',
        url : '../manager/software',
        method:'GET',
    });

    $('#box').datagrid({
        view: myview,
        singleSelect:false,
        emptyMsg: 'no records found',
        method:'GET',
        //width : function fixWidth(percent)  {
        //    return document.body.clientWidth * percent ; //这里你可以自己做调整
        //} ,
        url : '../manager',
        queryParams:
            {
                emplid:$.trim($('input[name="emplid"]').val()),
                date_from : $('input[name="date_from"]').val(),
                date_to : $('input[name="date_to"]').val(),
                IsWF :$('#ddlIsWF').combobox('getValue'),
                //company : $('input[name="company"]').val(),
                company :$('#ddlCompany').combobox('getValue'),
                IsCheck :$('#ddlIsCheck').combobox('getValue'),
                etprdp : $('input[name="etprdp"]').val(),
                software :$('#software').combobox('getValue'),
            },
        //title : '文件搜索报告',
        rowStyler: function(index,row){
            return 'font-size:x-large;background-color:#6293BB;color:#fff;';
        },
        width: $(window).width() - 100,
        fitColumns: true,
        toolbar: '#tool',
        columns : [[
            {
                field: 'UID',
                title: '自动编号',
                width: 100,
                checkbox: true,
            },
            {
                field: 'IsCheck',
                title: '是否合法',
            },
            {
                field: 'IsWF',
                title: '是否iWorkflow',
            },
            {
                field : 'company',
                title : 'Company',
            },
            {
                field : 'etprdp',
                title : '厂区',
            },

            {
                field : 'Computer',
                title : '计算机名',
            },
            {
                field : 'UserName',
                title : '登陆账号',
            },
            {
                field : 'Mac',
                title : 'Mac地址',
            },
            {
                field : 'CreateOn',
                title : '创建日期',
            },
            {
                field : 'chinam',
                title : '姓名',
            },
            {
                field : 'shonam',
                title : '部门',
            },
            {
                field : 'software',
                title : '软件',
            },
            {
                field : 'FileName',
                title : '文件名',
            },
            {
                field : 'FilePath',
                title : '文件路径',
            },

        ]],
        pagination : true,
        pageSize : 15,
        pageList : [15, 30, 35],
        pageNumber : 1,
        pagePosition : 'bottom',
        //onLoadSuccess:function(data){
        //    if(data.total>0)return;
        //    $('#box').datagrid('appendRow',{
        //        column: 'there is no related records'
        //    });
        //}
    });

    tool = {
        reload: function () {
            $('#box').datagrid('reload');
        },
        redo: function () {
            $('#box').datagrid('unselectAll');
        },
        download: function () {
           var req="../manager/download?emplid="+$.trim($('input[name="emplid"]').val())+"&date_from="+$('input[name="date_from"]').val()+"&date_to="+$('input[name="date_to"]').val()+"&IsWF="+$('#ddlIsWF').combobox('getValue')+"&company="+ $('#ddlCompany').combobox('getValue')+"&etprdp="+$('input[name="etprdp"]').val()+"&IsCheck="+$('#ddlIsCheck').combobox('getValue')+"&etprdp="+$('#etprdp').combobox('getValue')+"&software="+$('#software').combobox('getValue');
           window.location.href=req;
        },
        search : function () {
            $('#box').datagrid('load', {
                emplid : $.trim($('input[name="emplid"]').val()),
                date_from : $('input[name="date_from"]').val(),
                date_to : $('input[name="date_to"]').val(),
                //IsWF : $('select[name="IsWF"] option[selected]').val(),
                //IsWF : $("#ddlIsWF option:selected").text(),
                IsWF :$('#ddlIsWF').combobox('getValue'),
                //company : $('input[name="company"]').val(),
                company :$('#ddlCompany').combobox('getValue'),
                IsCheck :$('#ddlIsCheck').combobox('getValue'),
                etprdp : $('#etprdp').combobox('getValue'),
                software :$('#software').combobox('getValue'),
            });
        },

        uncheck: function () {
            var rows = $('#box').datagrid('getSelections');
            if (rows.length > 0) {
                $.messager.confirm('确定操作', '您正在要取消合法所选的记录吗？', function (flag) {
                    if (flag) {
                        var uids = [];
                        for (var i = 0; i < rows.length; i++) {
                            uids.push(rows[i].UID);
                        }
                        $.ajax({
                            type: 'POST',
                            url: '../manager/check',
                            data: {
                                typeOP:0,
                                uids: uids.join(','),
                            },
                            beforeSend: function () {
                                $('#needs').datagrid('loading');
                            },
                            success: function (data) {
                                if (data) {
                                    $('#box').datagrid('loaded');
                                    $('#box').datagrid('load');
                                    $('#box').datagrid('unselectAll');
                                    $.messager.show({
                                        title: '提示',
                                        msg:  '成功！',
                                    });
                                }
                            },
                        });
                    }
                });
            } else {
                $.messager.alert('提示', '请选择记录！', 'info');
            }
        },

        check: function () {
            var rows = $('#box').datagrid('getSelections');
            if (rows.length > 0) {
                $.messager.confirm('确定操作', '您正在要合法所选的记录吗？', function (flag) {
                    if (flag) {
                        var uids = [];
                        for (var i = 0; i < rows.length; i++) {
                            uids.push(rows[i].UID);
                        }
                        $.ajax({
                            type: 'POST',
                            url: '../manager/check',
                            data: {
                                typeOP:1,
                                uids: uids.join(','),
                            },
                            beforeSend: function () {
                                $('#needs').datagrid('loading');
                            },
                            success: function (data) {
                                if (data) {
                                    $('#box').datagrid('loaded');
                                    $('#box').datagrid('load');
                                    $('#box').datagrid('unselectAll');
                                    $.messager.show({
                                        title: '提示',
                                        msg:  '成功！',
                                    });
                                }
                            },
                        });
                    }
                });
            } else {
                $.messager.alert('提示', '请选择记录！', 'info');
            }
        },

        checkno: function () {
            var rows = $('#box').datagrid('getSelections');
            if (rows.length > 0) {
                $.messager.confirm('确定操作', '您正在要非法所选的记录吗？', function (flag) {
                    if (flag) {
                        var uids = [];
                        for (var i = 0; i < rows.length; i++) {
                            uids.push(rows[i].UID);
                        }
                        $.ajax({
                            type: 'POST',
                            url: '../manager/check',
                            data: {
                                typeOP:2,
                                uids: uids.join(','),
                            },
                            beforeSend: function () {
                                $('#needs').datagrid('loading');
                            },
                            success: function (data) {
                                if (data) {
                                    $('#box').datagrid('loaded');
                                    $('#box').datagrid('load');
                                    $('#box').datagrid('unselectAll');
                                    $.messager.show({
                                        title: '提示',
                                        msg:  '成功！',
                                    });
                                }
                            },
                        });
                    }
                });
            } else {
                $.messager.alert('提示', '请选择记录！', 'info');
            }
        },

    };


});













