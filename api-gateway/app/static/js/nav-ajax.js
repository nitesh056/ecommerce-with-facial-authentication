$(function () {
    $.ajax({
        url: "/cart",
        type: "GET",
        success: function(resp){
            $("#nav-right").append(resp);
        }
    });
});

$(function () {
    $.ajax({
        url: "/list-brand",
        type: "GET",
        success: function(resp){
            $("#brandList").append(resp);
        }
    });
});