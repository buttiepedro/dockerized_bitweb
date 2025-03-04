from flask import Flask, render_template
from flask_mail import Mail

import locale

mail = Mail()

def create_app():

    app = Flask(__name__)

    app.config.from_object('config.Config')

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
    
    return app