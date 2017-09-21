

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

    $('#box').datagrid({
        view: myview,
        singleSelect:false,
        emptyMsg: 'no records found',
        method:'GET',
        //width : function fixWidth(percent)  {
        //    return document.body.clientWidth * percent ; //这里你可以自己做调整
        //} ,
        url : '../whitelist/query',
        queryParams:
            {
                company :$('#ddlCompany').combobox('getValue'),
                IsCheck :$('#ddlIsCheck').combobox('getValue'),
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
                title: 'UID',
                width: 100,
                checkbox: true,
            },
            // {
            //     field: 'ProductName',
            //     title: 'Product Name',
            // },
            {
                field:'ProductName',
                title:'品名',
                formatter: function(value,row,index){
                    return '<a style="color:blue" target="_blank" href="../whitelist/details/index?uid='+row.UID+'">'+row.ProductName+'</a>';
                }
            },
            {
                field: 'LegalCopyright',
                title: '版权',
            },
            {
                field : 'Num',
                title : '数量',
            },
            {
                field : 'IsCheck',
                title : '白名单',
            },

        ]],
        pagination : true,
        pageSize : 15,
        pageList : [15, 30, 35],
        pageNumber : 1,
        pagePosition : 'bottom',
    
    });

    tool = {

         search : function () {
            $('#box').datagrid('load', {
                company :$('#ddlCompany').combobox('getValue'),
                IsCheck :$('#ddlIsCheck').combobox('getValue'),
            });
        },
        reload: function () {
            $('#box').datagrid('reload');
        },
        check: function () {
            var rows = $('#box').datagrid('getSelections');
            if (rows.length > 0) {
                $.messager.confirm('确定操作', '您正在要白名单所选的记录吗？', function (flag) {
                    if (flag) {
                        var uids = [];
                        for (var i = 0; i < rows.length; i++) {
                            uids.push(rows[i].UID);
                        }
                        $.ajax({
                            type: 'POST',
                            url: '../whitelist/check',
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
                $.messager.confirm('确定操作', '您正在要白名单所选的记录吗？', function (flag) {
                    if (flag) {
                        var uids = [];
                        for (var i = 0; i < rows.length; i++) {
                            uids.push(rows[i].UID);
                        }
                        $.ajax({
                            type: 'POST',
                            url: '../whitelist/check',
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













