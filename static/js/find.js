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

$(function () {

    $('#box').datagrid({
        view: myview,
        emptyMsg: 'no records found',
        method:'GET',
        //width : function fixWidth(percent)  {
        //    return document.body.clientWidth * percent ; //这里你可以自己做调整
        //} ,
        url : 'find',
        queryParams:{guid:$.trim($('input[name="guid"]').val()) },
        //title : '文件搜索报告',
        rowStyler: function(index,row){
            return 'font-size:x-large;background-color:#6293BB;color:#fff;';
        },
        width: $(window).width() - 100,
        fitColumns: true,
        columns : [[
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
                field : 'FileName',
                title : '文件名',
            },
            {
                field : 'FilePath',
                title : '文件路径',
            },
        ]],
        pagination : true,
        pageSize : 5,
        pageList : [5, 10, 15],
        pageNumber : 1,
        pagePosition : 'bottom',
        //onLoadSuccess:function(data){
        //    if(data.total>0)return;
        //    $('#box').datagrid('appendRow',{
        //        column: 'there is no related records'
        //    });
        //}
    });

});













