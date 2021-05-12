from routes.index import index_router


def register_blueprints(app):
    app.register_blueprint(index_router)
    