

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
        url : '../details/query',
        queryParams:{uid:$.trim($('input[name="uid"]').val()) },
        //title : '文件搜索报告',
        rowStyler: function(index,row){
            return 'font-size:x-large;background-color:#6293BB;color:#fff;';
        },
        width: $(window).width() - 100,
        fitColumns: true,
        toolbar: '#tool',
        columns : [[
  
            {
                field:'ProductName',
                title:'品名',               
            },
            {
                field: 'LegalCopyright',
                title: '版权',
            },        
            {
                field: 'Computer',
                title: '计算机',
            },
            {
                field: 'UserName',
                title: '工号',
            },
            {
                field: 'FileName',
                title: '文件名',
            },
            {
                field: 'FilePath',
                title: '安装路径',
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
         
            });
        },
        reload: function () {
            $('#box').datagrid('reload');
        },
    };


});













