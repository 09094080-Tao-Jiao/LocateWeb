$(function () {

    $('#box').datagrid({
        method:'GET',
        width : 800,
        url : 'find',
        queryParams:{guid:$.trim($('input[name="guid"]').val()) },
        //title : '文件搜索报告',
        rowStyler: function(index,row){
            return 'font-size:x-large;background-color:#6293BB;color:#fff;';
        },
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
    });

});













