from flask import request, jsonify
from app import db
from app.models import Usuario
from app.auth import generar_token
from werkzeug.security import generate_password_hash, check_password_hash
import re

def register():
    print("Ruta de registro llamada")
    datos = request.json
    nombre = datos.get('nombre')
    correo = datos.get('correo')
    contraseña = datos.get('contraseña')

    if not correo or not contraseña:
        return jsonify({'mensaje': 'Datos faltantes'}), 400
    if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
        return jsonify({'mensaje': 'Formato de correo inválido'}), 400
    if len(contraseña) < 8:
        return jsonify({'mensaje': 'La contraseña debe tener al menos 8 caracteres'}), 400

    usuario_existente = Usuario.query.filter_by(correo=correo).first()
    if usuario_existente:
        return jsonify({'mensaje': 'El usuario ya existe'}), 400

    contraseña_hash = generate_password_hash(contraseña)
    nuevo_usuario = Usuario(nombre=nombre, correo=correo, contraseña_hash=contraseña_hash)
    db.session.add(nuevo_usuario)
    db.session.commit()

    token = generar_token(nuevo_usuario)
    return jsonify({'mensaje': 'Usuario registrado exitosamente', 'token': token}), 201

def login():
    print("Ruta de login llamada")
    datos = request.json
    correo = datos.get('correo')
    contraseña = datos.get('contraseña')

    usuario = Usuario.query.filter_by(correo=correo).first()
    
    if usuario and check_password_hash(usuario.contraseña_hash, contraseña):
        token = generar_token(usuario)
        return jsonify({'mensaje': 'Inicio de sesión exitoso', 'token': token}), 200
    else:
        return jsonify({'mensaje': 'Credenciales inválidas'}), 401

def public_route():
    print("Ruta pública llamada")
    return jsonify({'mensaje': 'Esta es una ruta pública'})

def protected_route(usuario_actual):
    print("Ruta protegida llamada")
    return jsonify({'mensaje': 'Esta es una ruta protegida', 'usuario': usuario_actual.nombre})
