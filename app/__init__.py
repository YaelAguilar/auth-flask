from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import pymysql

# Configurar pymysql como MySQLdb
pymysql.install_as_MySQLdb()

db = SQLAlchemy()

def create_app():
    load_dotenv()  # Carga las variables de entorno

    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    with app.app_context():
        from app import routes, models  # Importar modelos y rutas aquí para evitar importaciones circulares
        db.create_all()
        print("Base de datos inicializada")

    print("Aplicación creada")
    return app
