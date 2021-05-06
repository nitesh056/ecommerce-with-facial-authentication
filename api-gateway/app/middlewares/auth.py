from functools import wraps
from flask import Response, request, g, redirect, flash

from services.requests import post


def get_user_info_middleware(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('token')

        response, status_success = post('AUTH_URL', '/u/token', {
            'token': token
        })

        g.user = None
        if status_success:
            g.user = response['user']
        
        return func(*args, **kwargs)


    return decorated_function


def check_auth_middleware(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('token')

        response, status_success = post('AUTH_URL', '/u/token', {
            'token': token
        })

        if status_success:
            g.user = response['user']
            return func(*args, **kwargs)

        flash("Access Denied!!", "danger")
        return redirect('/u/login')


    return decorated_function


def no_auth_middleware(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('token')

        response, status_success = post('AUTH_URL', '/u/token', {
            'token': token
        })

        if status_success:
            return redirect('/')

        return func(*args, **kwargs)

    return decorated_function


def admin_only_middleware(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('token')

        response, status_success = post('AUTH_URL', '/u/token', {
            'token': token
        })

        if status_success:
            if response.user.role == 'admin':
                g.user = response['user']
                return func(*args, **kwargs)
            else:
                flash("Access denied", "danger")
                return redirect('/')
        else:
            flash("Access denied", "danger")
            return redirect('/u/login')


    return decorated_function
