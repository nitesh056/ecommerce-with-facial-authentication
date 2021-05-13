from flask import Blueprint, request, render_template, make_response, redirect, g
import requests

from middlewares.auth import no_auth_middleware, get_user_info_middleware
from services.requests import get, post, put


auth_router = Blueprint('auth', __name__, url_prefix='/u')


@auth_router.route('/profile', methods=['POST', 'GET'])
@get_user_info_middleware
def showProfile():
    if request.method == 'GET':
        return render_template('auth/profile.html', user=g.user)
    
    if request.method == 'POST':
        
        if len(request.form.getlist('status')) == 0:
            userStatus = "inactive"
        else:
            userStatus = request.form.getlist('status')[0]
    
        response, status_success = put('AUTH_URL', '/u/edit/' + str(g.user['id']), {
            'user': {
                'name': request.form['name'],
                'email': request.form['email'],
                'phone_number': request.form['phone_number'],
                'password': request.form['password'],
                'status': userStatus
            }
        })

        return redirect('/u/profile')
    


@auth_router.route('/login', methods=['POST', 'GET'])
@no_auth_middleware
def login():
    if request.method == 'POST':

        response, status_success = post('AUTH_URL', '/u/login', {
            'user': {
                'email': request.form['email'],
                'password': request.form['password']
            }
        })
        
        if status_success:
            resp = make_response(redirect('/'))
            resp.set_cookie('token', response['token'])
            return resp
        else:
            return render_template('auth/login.html', payload={
                "email": request.form['email'],
                "auth_error_message": response['detail']
            })

    if request.method == 'GET':
        return render_template('auth/login.html')


@auth_router.route('/signup', methods=['POST', 'GET'])
@no_auth_middleware
def signup():
    if request.method == 'POST':

        response, status_success = post('AUTH_URL', '/u/register', {
            'user': {
                'username': request.form['username'],
                'name': request.form['name'],
                'email': request.form['email'],
                'password': request.form['password'],
                'phone_number': request.form['phone_number'],
                'role': "user",
                'status': "inactive",
                'upload_folder': ""
            }
        })

        if status_success:
            resp = make_response(redirect('/'))
            resp.set_cookie('token', response['token'])
            return resp
        else:
            return render_template('auth/signup.html', payload={
                "username": request.form['username'],
                "name": request.form['name'],
                "email": request.form['email'],
                "phone_number": request.form['phone_number'],
                "auth_error_message": response['detail']
            })

    if request.method == 'GET':
        return render_template('auth/signup.html')


@auth_router.route('/check_auth', methods=['GET'])
@get_user_info_middleware
def checkAuth():
    return render_template('auth/nav-auth.html', user=g.user)

@auth_router.route('/save-face/', methods=['GET'])
@get_user_info_middleware
def scanFace():
    return render_template('auth/camera.html', user=g.user)



@auth_router.route('/auth-with-face/<email>', methods=['POST'])
@no_auth_middleware
def authWithFace(email):
    response, status_success = put('AUTH_URL', '/u/check-email/', {
        'email': email
    })
    if status_success:
        return render_template('auth/authenticate-face.html', user=response)

    return response['detail']

@auth_router.route('/auth-with-face/confirm/<email>', methods=['GET'])
@no_auth_middleware
def confirmAuthWithFace(email):
    if request.method == 'GET':
        response, status_success = put('AUTH_URL', '/u/check-email/confirm', {
            'email': email
        })
        
        if status_success:
            resp = make_response(redirect('/'))
            resp.set_cookie('token', response['token'])
            return resp
        else:
            return render_template('auth/login.html', payload={
                "email": request.form['email'],
                "auth_error_message": response['detail']
            })

        return render_template('auth/login.html')

@auth_router.route('/logout', methods=['GET'])
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie('token', '')
    return resp
