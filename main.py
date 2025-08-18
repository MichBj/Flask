# Importa la clase Flask de la biblioteca flask
from flask import Flask

# Crea una instancia de la clase Flask
app = Flask(__name__)

# Define una ruta para la URL principal ('/')
@app.route('/')
def inicio():
    """
    Maneja las solicitudes a la URL principal y devuelve un mensaje de bienvenida.
    """
    return '¡Hola! Esta es mi aplicación Flask.'

# Este bloque asegura que la aplicación se ejecute solo si el script se ejecuta directamente
if __name__ == '__main__':
    # Inicia el servidor de desarrollo
    # debug=True activa el depurador y el auto-recargador
    app.run(debug=True)
