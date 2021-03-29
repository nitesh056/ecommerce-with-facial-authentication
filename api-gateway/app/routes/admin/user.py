from jinja2 import TemplateNotFound
from flask import Blueprint, request, render_template, redirect, flash
from werkzeug.utils import secure_filename

from services.requests import get, post, put, delete


user_router = Blueprint('user-admin', __name__, url_prefix='/admin/users')


@user_router.route('/', methods=["GET"])
def read():
    if request.method == 'GET':
        response, status_success = get('AUTH_URL', '/u/')
        return render_template('admin/user/list.html', users=response['users'])


@user_router.route('/edit/<user_id>', methods=["GET", "POST"])
def edit(user_id):
    p_response, p_status_success = get('AUTH_URL', '/user/' + str(user_id))
    editing_error = False

    if request.method == 'POST':
        is_gaming_laptop = 1 if request.form.get('is_gaming_laptop') is not None else 0
        is_desktop = 1 if request.form.get('is_desktop') is not None else 0
        is_new_arrival = 1 if request.form.get('is_new_arrival') is not None else 0

        image = request.files['image']

        image_name = p_response['image']
        if image:
            image_name = secure_filename(image.filename)
            image.save('app/static/images/users/' + image_name)

        response, status_success = put('AUTH_URL', '/user/' + str(user_id), {
            'user': {
                'name': request.form['name'],
                'old_price': request.form['old_price'],
                'current_price': request.form['current_price'],
                'qty': request.form['qty'],
                'image': image_name,
                'short_description': request.form['short_description'],
                'description': request.form['long_description'],
                'features': request.form['features'],
                'is_gaming_laptop': is_gaming_laptop,
                'is_desktop': is_desktop,
                'is_new_arrival': is_new_arrival,
                'status': 'active',
                'brand_id': request.form['brand_id']
            }
        })

        if status_success:
            flash("User Saved Succesfully", "success")
            return redirect('/admin/users/')

        flash("Error while saving User", "danger")
        editing_error = True

    if request.method == 'GET' or editing_error:
        b_response, b_status_success = get('AUTH_URL', '/brand/')
        if p_status_success & b_status_success:
            return render_template('admin/user/edit.html', user=p_response, brands=b_response['brands'])
        return redirect('/admin/users')


# @user_router.route('/delete/<user_id>', methods=["GET"])
# def remove(user_id):
#     if request.method == 'GET':
#         response, status_success = delete('AUTH_URL', '/user/' + str(user_id))
#         return redirect('/admin/users')
