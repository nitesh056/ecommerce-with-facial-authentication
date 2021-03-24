from flask import Blueprint, request, render_template
import requests

from services.requests import get, post


index_router = Blueprint('index', __name__, url_prefix='/')

@index_router.route('/')
def showHomePage():
    response, status_success = get('PRODUCT_URL', '/product')
    return render_template('index.html', products=response['products'])

@index_router.route('/gaming-laptop')
def showGamingLaptop():
    response, status_success = get('PRODUCT_URL', '/product/gaming-laptop')
    return render_template('product/products-list.html', products=response['products'])

@index_router.route('/desktop')
def showDesktop():
    response, status_success = get('PRODUCT_URL', '/product/desktop')
    return render_template('product/products-list.html', products=response['products'])

@index_router.route('/new-arrival')
def showNewArrival():
    response, status_success = get('PRODUCT_URL', '/product/new-arrival')
    return render_template('product/products-list.html', products=response['products'])

@index_router.route('/list-brand')
def showBrand():
    response, status_success = get('PRODUCT_URL', '/brand')
    return render_template('product/brand-list.html', brands=response['brands'])

@index_router.route('/search-by-brand/<brand_name>')
def showProductsByBrand(brand_name):
    response, status_success = get('PRODUCT_URL', '/brand/'+brand_name)
    return render_template('product/products-list.html', products=response['brand']['products'])
