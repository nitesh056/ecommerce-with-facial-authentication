from flask import Blueprint, request, render_template
import requests

index_router = Blueprint('index', __name__, url_prefix='/')

@index_router.route('/')
def showHomePage():
    return render_template('index.html')