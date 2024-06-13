import os
from dotenv import load_dotenv

load_dotenv()

# Clase de configuración de la aplicación
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'tu_clave_secreta')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'aquí pones la url a tu base de datos, el format es: mysql+pymysql://usuario:contraseña@host:puerto/nombre_de_base_de_datos (yo usé railway porque olvidé mi contraseña de usuario para bases de datos locales de mysql, pero puedes usar cualquier base de datos que quieras, como sqlite, postgresql, etc.)')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
