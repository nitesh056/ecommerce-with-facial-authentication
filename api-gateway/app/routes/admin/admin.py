from jinja2 import TemplateNotFound
from flask import Blueprint, request, render_template, redirect
from werkzeug.utils import secure_filename

from services.requests import get, post
from middlewares.auth import admin_only_middleware

admin_router = Blueprint('admin', __name__, url_prefix='/admin')


@admin_router.route('/', methods=["GET", "POST"])
@admin_only_middleware
def getDashboard():
    return render_template('admin/index.html', user_num=2, product_num=13, checkout_num=3, sale_num=1)
