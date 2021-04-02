from flask import Blueprint, request, render_template, redirect, flash
from werkzeug.utils import secure_filename

from services.requests import get, post, put, delete


invoice_router = Blueprint('invoice-admin', __name__, url_prefix='/admin/invoice')


@invoice_router.route('/', methods=["GET"])
def read():
    response, status_success = get('TRANSACTION_URL', '/cart/invoice')
    return render_template('admin/transaction/list.html', invoices=response['invoices'])


