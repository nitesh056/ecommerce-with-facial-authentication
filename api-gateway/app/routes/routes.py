from routes.auth import auth_router
from routes.index import index_router
from routes.cart import cart_router
from routes.admin.admin import admin_router
from routes.admin.product import product_router
from routes.admin.product import product_router


def register_blueprints(app):
    app.register_blueprint(index_router)
    app.register_blueprint(auth_router)
    app.register_blueprint(cart_router)
    app.register_blueprint(admin_router)
    app.register_blueprint(product_router)
