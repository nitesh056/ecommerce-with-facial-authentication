from flask import Flask
import os

from routes.auth import auth_router
from routes.index import index_router
from routes.admin import admin_router
from routes.cart import cart_router

def get_application():
    application = Flask(__name__)

    application.secret_key = os.environ.get("SECRET_KEY", "hh&H*hf7&#(3usudo#*isduf")

    application.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
    
    application.register_blueprint(index_router)
    application.register_blueprint(auth_router)
    application.register_blueprint(admin_router)
    application.register_blueprint(cart_router)

    return application

app = get_application()

if __name__ == '__main__':
    app.run(
        host=os.environ.get("HOST", "127.0.0.1"),
        port=os.environ.get("PORT", 5000),
        debug=os.environ.get("DEBUG", True)
        )
