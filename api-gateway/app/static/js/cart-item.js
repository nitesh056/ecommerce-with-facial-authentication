function addToCart(product_id) {
    console.log(product_id)
    $.ajax({
        url: "/cart/add-to-cart/"+product_id,
        type: "GET",
        success: function(resp){
            $("#nav-right").empty();
            $("#nav-right").append(resp);
            $("#toastMessage").text("Item added!!!");
            $("#flashToast").fadeIn().delay(3000).fadeOut();
        }
    });
}

function removeInCart(product_id) {
    $.ajax({
        url: "/cart/remove-in-cart/"+product_id,
        type: "GET",
        success: function(resp){
            $("#nav-right").empty();
            $("#nav-right").append(resp);
            $("#toastMessage").text("Item Removed!!!");
            $("#flashToast").fadeIn().delay(3000).fadeOut();
        }
    });
}