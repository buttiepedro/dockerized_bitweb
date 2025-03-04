from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

import locale

db = SQLAlchemy()
mail = Mail()

def create_app():

    app = Flask(__name__)

    app.config.from_object('config.Config')
    
    db.init_app(app)

    mail = Mail(app)

    locale.setlocale(locale.LC_ALL, 'es_ES')

    #Pagina principal
    @app.route('/')
    def index():
        return render_template('index.html')
    
    from bitr import contacto
    app.register_blueprint(contacto.bp)

    from bitr import servicios
    app.register_blueprint(servicios.bp)

    from bitr import nosotros
    app.register_blueprint(nosotros.bp)

    with app.app_context():
        db.create_all()
    
    return app