from flask import Blueprint, request, render_template, Response, flash, redirect, g

from middlewares.auth import get_user_info_middleware, check_auth_middleware
from services.requests import get, post


cart_router = Blueprint('cart', __name__, url_prefix='/cart')

@cart_router.route('/')
@get_user_info_middleware
def get_cart_item():
    status_success = False
    if g.user is not None:
        response, status_success = get('PRODUCT_URL', '/cart/'+ str(g.user['id']))
    
    if status_success:
        return render_template('cart/nav-cart.html', cart=response, cartItems=response['cart_items'])
    else:
        return "<i class='fas fa-shopping-cart pl-4' style='padding-top: 12px;'></i>"
        

@cart_router.route('/add-to-cart/<product_id>', methods=['GET'])
@get_user_info_middleware
def add_to_cart(product_id):
    if g.user is not None:
        response, status_success = post('PRODUCT_URL', '/cart/add-cart-item', {
            'user_id': g.user['id'],
            'product_id': product_id,
        })
        return render_template('cart/nav-cart.html', cart=response, cartItems=response['cart_items'])
    return Response("Login to add to cart", status=401)


@cart_router.route('/remove-in-cart/<product_id>', methods=['GET'])
@get_user_info_middleware
def remove_in_cart(product_id):
    if g.user is not None:
        response, status_success = post('PRODUCT_URL', '/cart/remove-cart-item', {
            'user_id': g.user['id'],
            'product_id': product_id,
        })
        return render_template('cart/nav-cart.html', cart=response, cartItems=response['cart_items'])
    return "Login to add to cart"

@cart_router.route('/checkout', methods=['GET', 'POST'])
@check_auth_middleware
def showCheckout():
    if request.method == 'POST':
        response, status_success = post('PRODUCT_URL', '/cart/checkout', {
            'checkout': {
                'name': request.form['name'],
                'email': request.form['email'],
                'address': request.form['address'],
                'phone_no': request.form['phone_no'],
                'status': "pending",
                'remarks': request.form['remarks'],
                'cart_id': request.form['cart_id']
            }
        })

        if status_success:
            response, status_success = post('NOTIFICATION_URL', '/notification/g/create', {
                "notification": {
                    "message": f"New Checkout Submitted by {request.form['name']}",
                    "redirect_to": "/admin/checkout/",
                    "group_type": "admin"
                }
            })
            
            flash("Your order has been saved", "info")
            return redirect("/")
        else:
            return response
            
    if request.method == 'GET':
        response, status_success = get('PRODUCT_URL', '/cart/' + str(g.user['id']))
        if status_success:
            
            return render_template('cart/checkout.html', cart=response, cartItems=response['cart_items'])
        else:
            flash("No cart to checkout", "danger")
            return redirect("/")

    
