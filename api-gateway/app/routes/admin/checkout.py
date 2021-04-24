from flask import Blueprint, request, render_template, redirect, flash
from werkzeug.utils import secure_filename

from services.requests import get, post, put, delete


checkout_router = Blueprint('checkout-admin', __name__, url_prefix='/admin/checkout')


@checkout_router.route('/', methods=["GET"])
def read():
    response, status_success = get('PRODUCT_URL', '/cart/checkout')
    return render_template('admin/checkout/list.html', checkouts=response['checkouts'])


@checkout_router.route('/accept/<checkout_id>', methods=['GET'])
def accept(checkout_id):
    response, status_success = put('PRODUCT_URL', '/cart/checkout/' + str(checkout_id), {
        "checkout": {
            "status": "approved"
        }
    })

    if(status_success):
        response, status_success = post('NOTIFICATION_URL', '/notification/n/create', {
            "notification": {
                "message": f"Your checkout Request has been Accepted",
                "redirect_to": "",
                "recipient": response['cart']['user_id']
            }
        })

    return redirect('/admin/checkout/')

@checkout_router.route('/reject/<checkout_id>', methods=['GET'])
def reject(checkout_id):
    response, status_success = put('PRODUCT_URL', '/cart/checkout/' + str(checkout_id), {
        "checkout": {
            "status": "canceled"
        }
    })

    if(status_success):
        response, status_success = post('NOTIFICATION_URL', '/notification/n/create', {
            "notification": {
                "message": f"Your checkout Request has been Accepted",
                "redirect_to": "",
                "recipient": response['cart']['user_id']
            }
        })
    
    return redirect('/admin/checkout/')
