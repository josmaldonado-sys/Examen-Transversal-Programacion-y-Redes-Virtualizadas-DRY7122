from flask import Flask, request
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

DB = "usuarios.db"


# Crear la base de datos
def crear_bd():

    conexion = sqlite3.connect(DB)
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            password TEXT NOT NULL

        )
    """)

    conexion.commit()
    conexion.close()


# Agregar usuarios
def agregar_usuario(usuario, password):

    conexion = sqlite3.connect(DB)
    cursor = conexion.cursor()

    hash_password = generate_password_hash(password)

    cursor.execute(
        "INSERT INTO usuarios(usuario,password) VALUES(?,?)",
        (usuario, hash_password)
    )

    conexion.commit()
    conexion.close()


# Crear BD
crear_bd()


# Integrantes
usuarios = [("Jose Maldonado", "Cisco123")]


conexion = sqlite3.connect(DB)
cursor = conexion.cursor()

cursor.execute("SELECT COUNT(*) FROM usuarios")

if cursor.fetchone()[0] == 0:

    for u in usuarios:
        agregar_usuario(u[0], u[1])

conexion.close()


@app.route("/")

def inicio():

    return """

<h2>Login DRY7122</h2>

<form method="POST" action="/login">

Usuario:<br>

<input name="usuario"><br><br>

Contraseña:<br>

<input type="password" name="password"><br><br>

<input type="submit">

</form>

"""


@app.route("/login", methods=["POST"])

def login():

    usuario = request.form["usuario"]
    password = request.form["password"]

    conexion = sqlite3.connect(DB)
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT password FROM usuarios WHERE usuario=?",
        (usuario,)
    )

    dato = cursor.fetchone()

    conexion.close()

    if dato and check_password_hash(dato[0], password):

        return f"<h2>Bienvenido {usuario}</h2>"

    else:

        return "<h2>Usuario o contraseña incorrecta</h2>"


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=7500,
        debug=True
    )
