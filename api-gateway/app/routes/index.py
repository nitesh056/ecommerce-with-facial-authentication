from flask import Blueprint, request, render_template, g, Response
import requests

from middlewares.auth import get_user_info_middleware
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

@index_router.route('/product/<product_id>')
def showProduct(product_id):
    response, status_success = get('PRODUCT_URL', '/product/'+ str(product_id))
    return render_template('product/product.html', product=response)

@index_router.route('/search-by-brand/<brand_name>')
def showProductsByBrand(brand_name):
    response, status_success = get('PRODUCT_URL', '/brand/'+brand_name)
    return render_template('product/products-list.html', products=response['brand']['products'])

@index_router.route('/notification')
@get_user_info_middleware
def get_notifications():
    status_success = False
    if g.user is not None:
        if g.user['role'] == 'admin': 
            user_type = 'admin'
        if g.user['role'] == 'staff':
            user_type = 'admin'
        else:
            user_type = 'customer'
        response, status_success = get('NOTIFICATION_URL', '/notification/' + user_type + "/" +str(g.user['id']))
    
    if status_success:
        notifications = response
    else:
        notifications = []
    

    def convertdate(notification):
        notification_date, notification_time = notification['created_at'].split("T")
        notification_time = notification_time.split(".")[0]
        notification['created_at'] = f"{notification_date}, at {notification_time}"
        return notification

    notifications = list(map(convertdate, notifications))

    return render_template('include/nav-notification.html', notifications=notifications, number_of_notifications=len(notifications))
    


# def gen():
#     cap = cv2.VideoCapture(0)
#     while True:
#         try:        
#             video_frame = run_frame(cap)
#             yield (b'--frame\r\n'
#                 b'Content-Type: image/jpeg\r\n\r\n' + video_frame + b'\r\n\r\n')
#         except:
#             cap.release()
#             cap = cv2.VideoCapture(0)

@index_router.route('/video-feed/capture-face')
def captureFace():
    return "asdf"