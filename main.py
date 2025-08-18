# Importa la clase Flask de la biblioteca flask
from flask import Flask

# Crea una instancia de la clase Flask
app = Flask(__name__)

# Define una ruta para la URL principal ('/')
@app.route('/')
def inicio():
    """ Maneja las solicitudes a la URL principal y devuelve un mensaje de bienvenida. """
    return '¡Hola! Esta es mi aplicación Flask.'

# Define la ruta para un usuario con un nombre personalizado
@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'¡Bienvenido, {nombre}!'

# Este bloque asegura que la aplicación se ejecute solo si el script se ejecuta directamente
if __name__ == '__main__':
    # Inicia el servidor de desarrollo en modo de depuración
    app.run(debug=True)