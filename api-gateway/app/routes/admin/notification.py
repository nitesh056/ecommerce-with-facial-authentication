from jinja2 import TemplateNotFound
from flask import Blueprint, request, render_template, redirect, flash
from werkzeug.utils import secure_filename

from services.requests import get, post
from middlewares.auth import admin_only_middleware

notification_router = Blueprint('notification', __name__, url_prefix='/admin/notification')


@notification_router.route('/create', methods=["GET", "POST"])
@admin_only_middleware
def create():
    if request.method == 'POST':
        response, status_success = post('NOTIFICATION_URL', '/notification/g/create', {
            'notification': {
                'message': request.form['message'],
                'redirect_to': "",
                'group_type': request.form['group_type']
            }
        })

        if status_success:
            flash("Notification Created Succesfully", "success")
        else:
            flash("Error while creating notification", "danger")

        return redirect('/admin/notification/create')

    if request.method == 'GET':
        return render_template('admin/notification/create.html')
