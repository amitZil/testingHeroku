window.onload = function() {
   $(function() {
    $('#upload-file-btn').click(function() {
        $('#ajaxResponse')[0].className = "";
        $('#ajaxResponse')[0].innerText='';
        var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/uploadfile',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function(data) {
                $('#ajaxResponse')[0].className = "alert alert-success";
                $('#ajaxResponse')[0].innerText=data
            },
            error: function(data) {
                $('#ajaxResponse')[0].className = "alert alert-danger";
                $('#ajaxResponse')[0].innerText=JSON.stringify(data)
            },
        });
    });
    $('#delete-file-btn').click(function() {
        $('#ajaxResponse')[0].className = "";
        $('#ajaxResponse')[0].innerText='';
        var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/deleteRecords',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function(data) {
                $('#ajaxResponse')[0].className = "alert alert-success";
                $('#ajaxResponse')[0].innerText=data
            },
            error: function(data) {
                $('#ajaxResponse')[0].className = "alert alert-danger";
                $('#ajaxResponse')[0].innerText=JSON.stringify(data)
            },
        });
    });
});
};

