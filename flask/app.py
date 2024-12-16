from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests

app = Flask(__name__)

API_BASE_URL = "http://127.0.0.1:8000"  # URL de la API FastAPI

@app.route('/')
def index():
    return render_template('base.html')


@app.route('/usuarios')
def listar_usuarios():
    response = requests.get(f"{API_BASE_URL}/usuario/")
    usuarios = response.json() if response.status_code == 200 else []
    return render_template('usuarios/listar_usuarios.html', usuarios=usuarios)

@app.route('/usuarios/crear', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        data = {
            "nombre": request.form['nombre'],
            "edad": int(request.form['edad']),
            "correo": request.form['correo']
        }
        requests.post(f"{API_BASE_URL}/usuario/", json=data)
        return redirect(url_for('listar_usuarios'))
    return render_template('usuarios/crear_usuario.html')

@app.route('/usuarios/editar/<id>', methods=['GET', 'POST'])
def editar_usuario(id):
    if request.method == 'POST':
        data = {
            "nombre": request.form['nombre'],
            "edad": int(request.form['edad']),
            "correo": request.form['correo']
        }
        requests.put(f"{API_BASE_URL}/usuario/{id}", json=data)
        return redirect(url_for('listar_usuarios'))

    response = requests.get(f"{API_BASE_URL}/usuario/{id}")
    usuario = response.json()
    return render_template('usuarios/editar_usuario.html', usuario=usuario)

@app.route('/usuarios/eliminar/<id>', methods=['POST'])
def eliminar_usuario(id):
    requests.delete(f"{API_BASE_URL}/usuario/{id}")
    return redirect(url_for('listar_usuarios'))


@app.route('/tareas')
def listar_tareas():
    response = requests.get(f"{API_BASE_URL}/tarea/")
    tareas = response.json() if response.status_code == 200 else []
    return render_template('tareas/listar_tareas.html', tareas=tareas)

@app.route('/tareas/asignar', methods=['GET', 'POST'])
def asignar_tarea():
    if request.method == 'POST':
        data = {
            "usuario_id": request.form['usuario_id'],
            "tarea": request.form['tarea'],
            "fecha": request.form['fecha'],
            "id_estado": int(request.form['id_estado'])
        }
        requests.post(f"{API_BASE_URL}/tarea/", json=data)
        return redirect(url_for('listar_tareas'))

    usuarios = requests.get(f"{API_BASE_URL}/usuario/").json()
    estados = requests.get(f"{API_BASE_URL}/estado/").json()
    return render_template('tareas/asignar_tarea.html', usuarios=usuarios, estados=estados)

@app.route('/tareas/usuario/<id>')
def tareas_usuario(id):
    response = requests.get(f"{API_BASE_URL}/tarea/")
    tareas = response.json()
    tareas_filtradas = [t for t in tareas if t['usuario_id'] == id and t['id_estado'] != 3]
    return render_template('tareas/tareas_usuario.html', tareas=tareas_filtradas)

@app.errorhandler(404)
def error_404(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
