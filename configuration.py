from routes.home import home_route
from routes.estoque import estoque_route
from routes.previsao import previsao_route
from database.database import db
from database.models.remedios import Remedio

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(estoque_route, url_prefix='/estoque')
    app.register_blueprint(previsao_route, url_prefix='/previsao')


def configure_db():
    db.connect()
    db.create_tables([Remedio])