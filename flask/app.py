from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import os
import requests

app = Flask(__name__)

app.secret_key = os.urandom(24)  

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

    usuarios_response = requests.get(f"{API_BASE_URL}/usuario/")
    usuarios = usuarios_response.json() if usuarios_response.status_code == 200 else []

    estados_response = requests.get(f"{API_BASE_URL}/estado/")
    estados = estados_response.json() if estados_response.status_code == 200 else []

    # Filtrar por estado y/o usuario
    id_estado = request.args.get('id_estado')
    usuario_id = request.args.get('usuario_id')
    
    params = {}
    if id_estado:
        params['id_estado'] = id_estado
    if usuario_id:
        params['usuario_id'] = usuario_id
    
    # Realizo solicitud a la API con los parametros
    response = requests.get(f"{API_BASE_URL}/tarea/", params=params)
    
    tareas = response.json() if response.status_code == 200 else []
    
    # Filtro tareas no finalizadas asumeindo que id 3 es "Finalizada"
    tareas = [tarea for tarea in tareas if tarea['id_estado'] != 3]
    
    return render_template('tareas/listar_tareas.html', 
                           tareas=tareas, 
                           usuarios=usuarios, 
                           estados=estados)

@app.route('/tareas/usuario/<usuario_id>')
def tareas_usuario(usuario_id):
    response_usuario = requests.get(f"{API_BASE_URL}/usuario/{usuario_id}")
    usuario = response_usuario.json()

    estados_response = requests.get(f"{API_BASE_URL}/estado/")
    estados = estados_response.json() if estados_response.status_code == 200 else []

    response = requests.get(f"{API_BASE_URL}/tarea?usuario_id={usuario_id}")
    tareas = response.json() if response.status_code == 200 else []
    

    tareas = [tarea for tarea in tareas if tarea['id_estado'] != 3]
    
    return render_template('tareas/tareas_usuario.html', tareas=tareas, usuario=usuario, estados=estados)

@app.route('/tareas/crear', methods=['GET', 'POST'])
def crear_tarea():

    usuarios_response = requests.get(f"{API_BASE_URL}/usuario/")
    usuarios = usuarios_response.json() if usuarios_response.status_code == 200 else []
    
    estados_response = requests.get(f"{API_BASE_URL}/estado/")
    estados = estados_response.json() if estados_response.status_code == 200 else []

    if request.method == 'POST':
        data = {
            "usuario_id": request.form['usuario_id'],
            "tarea": request.form['tarea'],
            "fecha": request.form['fecha'],
            "id_estado": int(request.form['id_estado'])
        }
        requests.post(f"{API_BASE_URL}/tarea/", json=data)
        return redirect(url_for('listar_tareas'))
    
    return render_template('tareas/crear_tarea.html', usuarios=usuarios, estados=estados)

@app.route('/tareas/editar/<id>', methods=['GET', 'POST'])
def editar_tarea(id):

    usuarios_response = requests.get(f"{API_BASE_URL}/usuario/")
    usuarios = usuarios_response.json() if usuarios_response.status_code == 200 else []
    
    estados_response = requests.get(f"{API_BASE_URL}/estado/")
    estados = estados_response.json() if estados_response.status_code == 200 else []

    if request.method == 'POST':
        data = {
            "usuario_id": request.form['usuario_id'],
            "tarea": request.form['tarea'],
            "fecha": request.form['fecha'],
            "id_estado": int(request.form['id_estado'])
        }
        requests.put(f"{API_BASE_URL}/tarea/{id}", json=data)
        return redirect(url_for('listar_tareas'))

    response = requests.get(f"{API_BASE_URL}/tarea/{id}")
    tarea = response.json()
    return render_template('tareas/editar_tarea.html', tarea=tarea, usuarios=usuarios, estados=estados)

@app.route('/tareas/eliminar/<id>', methods=['POST'])
def eliminar_tarea(id):
    requests.delete(f"{API_BASE_URL}/tarea/{id}")
    return redirect(url_for('listar_tareas'))


@app.errorhandler(404)
def error_404(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
