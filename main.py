from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    """Maneja las solicitudes a la URL principal y renderiza la plantilla index.html."""
    return render_template('index.html')

@app.route('/usuario/<nombre>')
def usuario(nombre):
    """Maneja las solicitudes a la URL /usuario/<nombre> y renderiza una plantilla con el nombre."""
    return render_template('index.html', nombre=nombre)

@app.route('/acerca')
def acerca():
    """Maneja las solicitudes a la URL /acerca y renderiza la plantilla about.html."""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)