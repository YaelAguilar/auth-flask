from app import create_app

#Archivo principal de la aplicación
app = create_app()

if __name__ == '__main__':
    print("Ejecutando la aplicación")
    app.run(debug=True)
