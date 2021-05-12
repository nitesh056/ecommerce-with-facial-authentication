from flask import Blueprint, Response
import requests
import cv2

from services.capture import Capture
from services.authenticate import FacialAuth


index_router = Blueprint('index', __name__, url_prefix='/')



@index_router.route('/')
def index():
    return """<img id="myImg" src='http://127.0.0.1:8004/video-feed/capture-face/second'>"""
    # <div id="demo">check here</div>
    # <script>
    # (function() {
    #     setInterval(function(){
    #         console.log("jaksdjfk");
    #         var x = document.getElementById("myImg").width;
            
    #         document.getElementById("demo").innerHTML = x;
    #     }, 500);
    # })();
    # </script>
    # """

@index_router.route('/auth')
def auth():
    return "<img src='http://127.0.0.1:8004/video-feed/auth/seconad'>"


@index_router.route('/video-feed/capture-face/<username>')
def captureFace(username):
    capture = Capture(username)
    return Response(capture.capture_face(), mimetype='multipart/x-mixed-replace; boundary=frame')


@index_router.route('/video-feed/auth/<username>')
def authenticate(username):
    capture = FacialAuth(username)
    return Response(capture.auth(), mimetype='multipart/x-mixed-replace; boundary=frame')