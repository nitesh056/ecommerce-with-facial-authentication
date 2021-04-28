from jinja2 import TemplateNotFound

from flask import Blueprint, request, render_template, redirect
from werkzeug.utils import secure_filename
from services.requests import get, post


admin_router = Blueprint('admin', __name__, url_prefix='/admin')


@admin_router.route('/', methods=["GET", "POST"])
def getDashboard():
    return render_template('admin/index.html')
