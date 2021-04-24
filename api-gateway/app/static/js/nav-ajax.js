$(function () {
    $.ajax({
        url: "/list-brand",
        type: "GET",
        success: function(resp){
            $("#brandList").append(resp);
        }
    });
});

$(function () {
    $.ajax({
        url: "/u/check_auth",
        type: "GET",
        success: function(resp){
            $("#navAuth").append(resp);
        }
    });
});

$(function () {
    $.ajax({
        url: "/cart",
        type: "GET",
        success: function(resp){
            $("#nav-right-cart").append(resp);
        }
    });
});

$(function () {
    $.ajax({
        url: "/notification",
        type: "GET",
        success: function(resp){
            $("#nav-right-notification").append(resp);
        }
    });
});
