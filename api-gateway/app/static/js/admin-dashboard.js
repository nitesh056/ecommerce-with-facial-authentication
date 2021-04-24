$(function () {
    $.ajax({
        url: "/notification",
        type: "GET",
        success: function(resp){
            $("#nav-right-notification").append(resp);
        }
    });
});