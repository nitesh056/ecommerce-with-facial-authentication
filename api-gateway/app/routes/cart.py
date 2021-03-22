from flask import Blueprint, request, render_template
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

@cart_router.route('/checkout')
def showCheckout():
    response, status_success = get('PRODUCT_URL', '/cart/1') # need to make this (1) dynamic from user_id
    return render_template('cart/checkout.html', cart=response, cartItems=response['cart_items'])