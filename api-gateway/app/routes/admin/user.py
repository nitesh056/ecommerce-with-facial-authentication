from jinja2 import TemplateNotFound
from flask import Blueprint, request, render_template, redirect, flash
from werkzeug.utils import secure_filename

from services.requests import get, post, put, delete
from middlewares.auth import admin_only_middleware

user_router = Blueprint('user-admin', __name__, url_prefix='/admin/users')


@user_router.route('/', methods=["GET"])
@admin_only_middleware
def read():
    if request.method == 'GET':
        response, status_success = get('AUTH_URL', '/u/')
        return render_template('admin/user/list.html', users=response['users'])


@user_router.route('/<user_id>/<role>', methods=["GET"])
@admin_only_middleware
def edit(user_id, role):
    response, status_success = put('AUTH_URL', '/u/role/' + str(user_id), {
        "user": {
            "role": role
        }
    })

    if not status_success:
        flash("Failed", 'danger')

    return redirect('/admin/users/')


# @user_router.route('/<user_id>/user', methods=["GET"])
# def edit(user_id):
#     response, status_success = put('AUTH_URL', '/u/role' + str(user_id), {
#         "user": {
#             "role": 'user'
#         }
#     })

#     if not status_success:
#         flash("Failed", 'danger')

#     return redirect('/admin/users/')
