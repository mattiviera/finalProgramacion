# Gestión de Tareas y Usuarios

## Descripción

Este proyecto consiste en una web para gestionar **tareas** y  **usuarios** . La API permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre tareas y usuarios en una base de datos.

* **Usuarios** : Registro, consulta y actualización de usuarios.
* **Tareas** : Gestión de tareas asignadas a usuarios, con filtros por estado y usuario.

Está construida utilizando **FastAPI** para la gestión de las rutas y la lógica de negocio, y la base de datos se maneja con **SQLAlchemy** para interactuar con un sistema de base de datos (SQLite).

## Funcionalidades

1. **Usuarios** :

* Crear un nuevo usuario.
* Consultar todos los usuarios.
* Consultar un usuario por ID.
* Actualizar un usuario existente.
* Eliminar un usuario

1. **Tareas** :

* Crear una nueva tarea.
* Consultar todas las tareas.
* Consultar tareas por estado o usuario asignado.
* Consultar una tarea por ID.
* Actualizar y eliminar tareas.

## Tecnologías utilizadas

* **Python** : Lenguaje de programación principal del proyecto.
* **FastAPI** : Framework web para crear la API.
* **SQLAlchemy** : ORM para interactuar con la base de datos.
* **SQLite** (configurable en la conexión a la base de datos).
* **Flask** : Framework web para la interfaz de usuario frontend, proporcionando vistas dinámicas y formularios de interacción.
* **HTML** : Lenguaje de marcado utilizado para la creación de las vistas.
* **CSS** : Para estilizar las vistas de la interfaz de usuario y hacerlas visualmente atractivas.

## Requisitos

* **Python**
* Dependencias en `requirements.txt`.

## Instalación

1. Clona este repositorio:
   ```
   git clone <url_del_repositorio>
   cd <directorio_del_repositorio>

   ```
2. Crea un entorno virtual y actívalo:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate

   ```
3. Instala las dependencias necesarias:
   ```
   pip install -r requirements.txt

   ```

## Ejecutar la API con FastAPI

1. Inicia el servidor de FastAPI:
   ```
    uvicorn main:app --reload
   ```
2. Accede a la documentación interactiva de la API en:

* **Swagger UI** : `http://localhost:8000/docs`

## Ejecutar la Interfaz Web con Flask

1. Inicia el servidor de Flask:

   ```
   python app.py
   ```

   1. El servidor de Flask se ejecutará en `http://localhost:5000`.
   2. En la interfaz web podrás crear, editar y eliminar usuarios y tareas, además de ver todas las tareas y usuarios registrados en la base de datos.
