from flask import Flask

from routes.auth import auth_router
from routes.index import index_router

def get_application():
    application = Flask(__name__)

    application.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
    
    application.register_blueprint(index_router)
    application.register_blueprint(auth_router)

    return application

app = get_application()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
