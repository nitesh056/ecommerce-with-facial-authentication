from flask import Blueprint, request, render_template, redirect, flash, g
from werkzeug.utils import secure_filename
from random import random

from middlewares.auth import get_user_info_middleware, check_auth_middleware
from services.requests import get, post


invoice_router = Blueprint('invoice-admin', __name__, url_prefix='/admin/invoice')


@invoice_router.route('/p', methods=["GET"])
def readAllPurchase():
    response, status_success = get('TRANSACTION_URL', '/invoice/p')
    print(response)
    return render_template('admin/transaction/list.html', invoices=response['invoices'])


@invoice_router.route('/s', methods=["GET"])
def readAllSales():
    response, status_success = get('TRANSACTION_URL', '/invoice/s')
    return render_template('admin/transaction/list.html', invoices=response['invoices'])


@invoice_router.route('/create', methods=["GET", "POST"])
@get_user_info_middleware
def createInvoice():
    if request.method == 'POST':
        product_ids = request.form.getlist('product_id')
        quantities = request.form.getlist('quantity')
        rates = request.form.getlist('rate')
        
        invoice_items_keys = ('product_id', 'quantity', 'rate')
        
        invoice_items = [dict(zip(invoice_items_keys, item_info)) for item_info in zip(product_ids, quantities, rates)]

        response, status_success = post('TRANSACTION_URL', '/invoice/create', {
            'invoice' : {
                'invoice_date': request.form['invoice_date'],
                'created_by': g.user['id'],
                'transaction_type': request.form['transaction_type'],
                'grand_total': request.form['grand_total'],
                'invoice_items': invoice_items
            }
        })

        print(response)
        return redirect('/admin/invoice/create')

    if request.method == 'GET':
        response, status_success = get('PRODUCT_URL', '/product/all')
        print(response, status_success)
        return render_template('admin/transaction/create.html', products=response['products'])

    response, status_success = get('TRANSACTION_URL', '/invoice/s')


@invoice_router.route('/add-item/', methods=["GET"])
def addItem():
    response, status_success = get('PRODUCT_URL', '/product/all')
    return render_template('admin/transaction/invoice-details.html', products=response['products'], randomId=int(random() * 100000))
