from routes.auth import auth_router
from routes.index import index_router
from routes.cart import cart_router
from routes.admin.admin import admin_router
from routes.admin.user import user_router
from routes.admin.product import product_router
from routes.admin.checkout import checkout_router
from routes.admin.invoice import invoice_router
from routes.admin.notification import notification_router


def register_blueprints(app):
    app.register_blueprint(index_router)
    app.register_blueprint(auth_router)
    app.register_blueprint(cart_router)
    app.register_blueprint(admin_router)
    app.register_blueprint(user_router)
    app.register_blueprint(product_router)
    app.register_blueprint(checkout_router)
    app.register_blueprint(invoice_router)
    app.register_blueprint(notification_router)
