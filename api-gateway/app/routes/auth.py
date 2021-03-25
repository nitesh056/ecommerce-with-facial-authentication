from flask import Blueprint, request, render_template, make_response, redirect, g
import requests

from middlewares.auth import no_auth_middleware, get_user_info_middleware
from services.requests import get, post


auth_router = Blueprint('auth', __name__, url_prefix='/u')


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
                'role_id': "user",
                'status': "active"
            }
        })

        if status_success:
            resp = make_response(render_template('index.html'))
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
    print(g.user)
    return render_template('auth/nav-auth.html', user=g.user)


@auth_router.route('/logout', methods=['GET'])
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie('token', '')
    return resp