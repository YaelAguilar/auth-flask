from flask import request, jsonify, current_app as app
from functools import wraps
import jwt
import datetime
from app.models import Usuario

def token_requerido(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]  # Bearer <token>
        
        if not token:
            return jsonify({'mensaje': 'Token es requerido'}), 401
        
        try:
            datos = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            usuario_actual = Usuario.query.filter_by(correo=datos['correo']).first()
        except Exception as e:
            return jsonify({'mensaje': 'Token es inválido', 'error': str(e)}), 401
        
        return f(usuario_actual, *args, **kwargs)
    
    return decorador

def generar_token(usuario):
    payload = {
        'correo': usuario.correo,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token
