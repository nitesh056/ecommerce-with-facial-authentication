from flask import Flask
import os

from routes.routes import register_blueprints

def get_application():
    application = Flask(__name__)

    application.secret_key = os.environ.get("SECRET_KEY", "hh&H*hf7&#(3usudo#*isduf")

    application.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
    
    register_blueprints(application)

    return application

app = get_application()

if __name__ == '__main__':
    app.run(
        host=os.environ.get("HOST", "127.0.0.1"),
        port=os.environ.get("PORT", 5000),
        debug=os.environ.get("DEBUG", True)
        )
