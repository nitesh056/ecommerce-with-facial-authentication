function addToCart(product_id) {
    console.log(product_id)
    $.ajax({
        url: "/cart/add-to-cart/"+product_id,
        type: "GET",
        success: function(resp){
            $("#nav-right").empty();
            $("#nav-right").append(resp);
            $("#toastMessage").text("Cart Updated!!!");
            $("#flashToast").fadeIn().delay(3000).fadeOut();
        }
    });
}