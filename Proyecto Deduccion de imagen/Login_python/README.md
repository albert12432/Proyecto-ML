# Sistema de Login con Python y Flask

Este es un sistema de autenticación de usuarios con Flask, MySQL y Bootstrap.

## 📋 Requisitos previos

- Python 3.8 o superior
- MySQL Server instalado y ejecutándose
- pip (gestor de paquetes de Python)

## 🚀 Instalación y configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/BrayamDev/Login_python.git
cd Login_python
```

### 2. Instalar dependencias de Python
```bash
pip install -r requirements.txt
```

### 3. Configurar la base de datos MySQL

#### Opción A: Usando la línea de comandos de MySQL
```bash
# Acceder a MySQL
mysql -u root -p

# Ejecutar el archivo SQL
source database.sql
```

#### Opción B: Usando MySQL Workbench
1. Abrir MySQL Workbench
2. Conectarse a tu servidor local
3. Abrir el archivo `database.sql`
4. Ejecutar el script (botón de rayo ⚡)

#### Opción C: Manualmente
Ejecuta estos comandos en MySQL:
```sql
CREATE DATABASE IF NOT EXISTS flask_login;
USE flask_login;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 4. Configurar las credenciales de MySQL

Edita el archivo `app.py` y actualiza estas líneas con tus credenciales:
```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'        # Tu usuario de MySQL
app.config['MYSQL_PASSWORD'] = ''        # Tu contraseña de MySQL
app.config['MYSQL_DB'] = 'flask_login'
```

### 5. Ejecutar la aplicación
```bash
python app.py
```

La aplicación estará disponible en: **http://127.0.0.1:5000**

## 📁 Estructura del proyecto

```
Login_python/
│
├── app.py                 # Aplicación principal Flask
├── database.sql           # Script de creación de base de datos
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Este archivo
│
└── templates/            # Plantillas HTML
    ├── home.html        # Página principal (después del login)
    ├── login.html       # Página de inicio de sesión
    └── register.html    # Página de registro
```

## 🔧 Funcionalidades

- ✅ Registro de nuevos usuarios
- ✅ Inicio de sesión con validación
- ✅ Contraseñas encriptadas con bcrypt
- ✅ Sesiones de usuario
- ✅ Protección de rutas
- ✅ Cierre de sesión
- ✅ Interfaz responsiva con Bootstrap 5

## 🛠️ Tecnologías utilizadas

- **Backend:** Flask (Python)
- **Base de datos:** MySQL
- **Frontend:** HTML, Bootstrap 5
- **Seguridad:** Flask-Bcrypt para hash de contraseñas
- **ORM:** Flask-MySQLdb

## 📝 Uso

1. **Registro:** Accede a `/register` o haz clic en "Regístrate"
2. **Login:** Usa tus credenciales en `/login`
3. **Home:** Después del login, serás redirigido a la página principal
4. **Logout:** Haz clic en "Cerrar sesión" para salir

## ⚠️ Notas importantes

- Asegúrate de que MySQL esté ejecutándose antes de iniciar la aplicación
- La contraseña de MySQL debe estar correctamente configurada en `app.py`
- Para producción, cambia `app.secret_key` por una clave más segura
- No uses `debug=True` en producción

## 🐛 Solución de problemas

### Error: "Can't connect to MySQL server"
- Verifica que MySQL esté ejecutándose
- Verifica las credenciales en `app.py`

### Error: "No module named 'MySQLdb'"
```bash
pip install mysqlclient
```

### Error en Windows con mysqlclient
Puede que necesites instalar Visual C++ Build Tools o usar una versión precompilada:
```bash
pip install mysqlclient‑2.2.0‑cp311‑cp311‑win_amd64.whl
```

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

## 👤 Autor

**BrayamDev**
- GitHub: [@BrayamDev](https://github.com/BrayamDev)
