from flask import current_app as app
from app.controllers import register, login, public_route, protected_route
from app.auth import token_requerido

@app.route('/register', methods=['POST'])
def register_route():
    return register()

@app.route('/login', methods=['POST'])
def login_route():
    return login()

@app.route('/public')
def public_route_handler():
    return public_route()

@app.route('/protected')
@token_requerido
def protected_route_handler(usuario_actual):
    return protected_route(usuario_actual)
