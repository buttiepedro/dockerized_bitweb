
class Config:
    DEBUG = True
    SECRET_KEY = 'dev'

    #Database config
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:P3drobutt1e$@localhost:5432/bit_videoanalisis"

    #CKEditor para ingresar texto
    CKEDITOR_PKG_TYPE = 'standard'

    #Configuracion del mail

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'buttiepedro.bit@gmail.com'  # Reemplaza con tu email
    MAIL_PASSWORD = 'nqxz qssp dqdm mwqw'  # Reemplaza con tu contraseña
    
    