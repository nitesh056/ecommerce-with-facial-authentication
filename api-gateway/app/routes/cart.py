from flask import Blueprint, request, render_template, flash, redirect
import requests

from services.requests import get, post


cart_router = Blueprint('cart', __name__, url_prefix='/cart')

@cart_router.route('/')
def get_cart_item():
    response, status_success = get('PRODUCT_URL', '/cart/1') # need to make this (1) dynamic from user_id
    return render_template('cart/nav-cart.html', cart=response, cartItems=response['cart_items'])

@cart_router.route('/add-to-cart/<product_id>', methods=['GET'])
def add_to_cart(product_id):
    response, status_success = post('PRODUCT_URL', '/cart/add-cart-item', {
        'user_id': 1,
        'product_id': product_id,
    }) # need to make this (1) dynamic from user_id
    return render_template('cart/nav-cart.html', cart=response, cartItems=response['cart_items'])

@cart_router.route('/remove-in-cart/<product_id>', methods=['GET'])
def remove_in_cart(product_id):
    response, status_success = post('PRODUCT_URL', '/cart/remove-cart-item', {
        'user_id': 1,
        'product_id': product_id,
    }) # need to make this (1) dynamic from user_id
    return render_template('cart/nav-cart.html', cart=response, cartItems=response['cart_items'])

@cart_router.route('/checkout', methods=['GET', 'POST'])
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
            flash("Your order has been saved", "info")
            return redirect("/")
        else:
            print(response)
            return response
            # return render_template('auth/signup.html', payload={
            #     "username": request.form['username'],
            #     "name": request.form['name'],
            #     "email": request.form['email'],
            #     "phone_number": request.form['phone_number'],
            #     "auth_error_message": response['detail']
            # })
    if request.method == 'GET':
        response, status_success = get('PRODUCT_URL', '/cart/1') # need to make this (1) dynamic from user_id
        if status_success:
            
            return render_template('cart/checkout.html', cart=response, cartItems=response['cart_items'])
        else:
            flash("No cart to checkout", "danger")
            return redirect("/")

    
