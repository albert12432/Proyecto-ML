from flask import Flask, render_template, request, redirect, url_for, session, flash, make_response
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'lengua_senas_proyecto_ml_2025'

bcrypt = Bcrypt(app)

# Base de datos en memoria (simple para desarrollo)
# En producción, usar una base de datos real
users_db = {
    'admin': bcrypt.generate_password_hash('admin').decode('utf-8'),
    'usuario': bcrypt.generate_password_hash('1234').decode('utf-8')
}

# Función para agregar cabeceras de no caché
def add_no_cache_headers(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"  # Deshabilita la caché
    response.headers["Pragma"] = "no-cache"  # Compatibilidad con HTTP/1.0
    response.headers["Expires"] = "0"  # Fecha de expiración en el pasado
    return response

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('home'))  # Redirige a home si está autenticado
    return redirect(url_for('login'))  # Redirige a login si no está autenticado

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificar usuario en la base de datos en memoria
        if username in users_db:
            if bcrypt.check_password_hash(users_db[username], password):
                session['username'] = username
                return redirect(url_for('home'))
        
        flash('Usuario o contraseña incorrectos')
        return redirect(url_for('login'))

    response = make_response(render_template('login.html'))
    return add_no_cache_headers(response)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Registrar nuevo usuario
        if username in users_db:
            flash('El usuario ya existe')
            return redirect(url_for('register'))
        
        hashed = bcrypt.generate_password_hash(password).decode('utf-8')
        users_db[username] = hashed

        flash('Registro exitoso. Por favor, inicia sesión.')
        return redirect(url_for('login'))

    response = make_response(render_template('register.html'))
    return add_no_cache_headers(response)

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))  # Redirige a login si no está autenticado
    response = make_response(render_template('home.html'))
    return add_no_cache_headers(response)  # Aplica las cabeceras de no caché

@app.route('/entendimiento-negocio')
def entendimiento_negocio():
    if 'username' not in session:
        return redirect(url_for('login'))  # Redirige a login si no está autenticado
    response = make_response(render_template('entendimiento_negocio.html'))
    return add_no_cache_headers(response)  # Aplica las cabeceras de no caché

@app.route('/ingenieria-datos')
def ingenieria_datos():
    if 'username' not in session:
        return redirect(url_for('login'))  # Redirige a login si no está autenticado
    response = make_response(render_template('ingenieria_datos.html'))
    return add_no_cache_headers(response)  # Aplica las cabeceras de no caché

@app.route('/modelo-neural')
def modelo_neural():
    if 'username' not in session:
        return redirect(url_for('login'))  # Redirige a login si no está autenticado
    response = make_response(render_template('modelo_neural.html'))
    return add_no_cache_headers(response)  # Aplica las cabeceras de no caché

@app.route('/logout')
def logout():
    session.pop('username', None)
    response = make_response(redirect(url_for('login')))
    return add_no_cache_headers(response)  # Aplica las cabeceras de no caché

if __name__ == '__main__':
    app.run(debug=True)