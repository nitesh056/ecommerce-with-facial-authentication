$(function () {
    $.ajax({
        url: "/cart",
        type: "GET",
        success: function(resp){
            $("#nav-right").append(resp);
        }
    });
});