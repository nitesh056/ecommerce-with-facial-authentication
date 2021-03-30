from flask import Blueprint, request, render_template, redirect, flash
from werkzeug.utils import secure_filename

from services.requests import get, post, put, delete


product_router = Blueprint('product-admin', __name__, url_prefix='/admin/products')


@product_router.route('/', methods=["GET"])
def read():
    if request.method == 'GET':
        response, status_success = get('PRODUCT_URL', '/product/all')
        return render_template('admin/product/list.html', products=response['products'])


@product_router.route('/create', methods=["GET", "POST"])
def create():
    if request.method == 'POST':
        is_gaming_laptop = 1 if request.form.get('is_gaming_laptop') is not None else 0
        is_desktop = 1 if request.form.get('is_desktop') is not None else 0
        is_new_arrival = 1 if request.form.get('is_new_arrival') is not None else 0

        image = request.files['image']

        image_name = "no-image.png"
        if image:
            image_name = secure_filename(image.filename)
            image.save('app/static/images/products/' + image_name)

        response, status_success = post('PRODUCT_URL', '/product/create', {
            'product': {
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
            return redirect('/admin/products')
        else:
            return response

    if request.method == 'GET':
        response, status_success = get('PRODUCT_URL', '/brand/')
        return render_template('admin/product/create.html', brands=response['brands'])


@product_router.route('/edit/<product_id>', methods=["GET", "POST"])
def edit(product_id):
    p_response, p_status_success = get('PRODUCT_URL', '/product/' + str(product_id))
    editing_error = False

    if request.method == 'POST':
        is_gaming_laptop = 1 if request.form.get('is_gaming_laptop') is not None else 0
        is_desktop = 1 if request.form.get('is_desktop') is not None else 0
        is_new_arrival = 1 if request.form.get('is_new_arrival') is not None else 0

        image = request.files['image']

        image_name = p_response['image']
        if image:
            image_name = secure_filename(image.filename)
            image.save('app/static/images/products/' + image_name)

        response, status_success = put('PRODUCT_URL', '/product/' + str(product_id), {
            'product': {
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
            flash("Product Saved Succesfully", "success")
            return redirect('/admin/products/')

        flash("Error while saving Product", "danger")
        editing_error = True

    if request.method == 'GET' or editing_error:
        b_response, b_status_success = get('PRODUCT_URL', '/brand/')
        if p_status_success & b_status_success:
            return render_template('admin/product/edit.html', product=p_response, brands=b_response['brands'])
        return redirect('/admin/products')


@product_router.route('/delete/<product_id>', methods=["GET"])
def remove(product_id):
    if request.method == 'GET':
        response, status_success = delete('PRODUCT_URL', '/product/' + str(product_id))
        return redirect('/admin/products')
