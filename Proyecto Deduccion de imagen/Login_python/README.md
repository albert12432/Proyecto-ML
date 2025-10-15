# Sistema de Login con Python y Flask

Este proyecto implementa un sistema de autenticación de usuarios utilizando Flask, MySQL y Bootstrap.

## Requisitos previos

- Python 3.8 o superior
- MySQL Server en funcionamiento
- pip instalado

## Instalación y configuración

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

#### Opción A: Línea de comandos de MySQL
```bash
mysql -u root -p
source database.sql
```

#### Opción B: MySQL Workbench
1. Abrir MySQL Workbench
2. Conectarse al servidor local
3. Abrir `database.sql`
4. Ejecutar el script

#### Opción C: Manualmente
Ejecutar estos comandos en MySQL:
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

Editar el archivo `app.py` y actualizar las siguientes líneas con tus datos:
```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'        # Usuario de MySQL
app.config['MYSQL_PASSWORD'] = ''        # Contraseña de MySQL
app.config['MYSQL_DB'] = 'flask_login'
```

### 5. Ejecutar la aplicación
```bash
python app.py
```

La aplicación estará disponible en: http://127.0.0.1:5000

## Estructura del proyecto

```
Login_python/
│
├── app.py                 # Archivo principal de Flask
├── database.sql           # Script de base de datos
├── requirements.txt       # Dependencias
├── README.md              # Documentación
│
└── templates/             # Plantillas HTML
    ├── home.html
    ├── login.html
    └── register.html
```

## Funcionalidades

- Registro de usuarios nuevos
- Inicio de sesión con validación
- Contraseñas cifradas con bcrypt
- Manejo de sesiones
- Protección de rutas privadas
- Cierre de sesión
- Interfaz adaptativa con Bootstrap 5

## Tecnologías utilizadas

- Flask (Python)
- MySQL
- HTML y Bootstrap 5
- Flask-Bcrypt para seguridad de contraseñas
- Flask-MySQLdb como ORM

## Uso

1. Registro: Accede a `/register`
2. Inicio de sesión: Usa tus credenciales en `/login`
3. Página principal: Redirección tras iniciar sesión
4. Cerrar sesión: Opción disponible en la interfaz

## Notas importantes

- MySQL debe estar ejecutándose antes de iniciar la aplicación.
- La contraseña de MySQL debe coincidir con la configuración en `app.py`.
- Para ambientes de producción, se recomienda cambiar `app.secret_key` por una clave segura.
- No activar el modo debug en producción.

## Solución de problemas

### Error: "Can't connect to MySQL server"
- Verificar que MySQL esté iniciado
- Revisar credenciales en `app.py`

### Error: "No module named 'MySQLdb'"
```bash
pip install mysqlclient
```

### Error en Windows con mysqlclient
Puede requerir Visual C++ Build Tools o instalar una versión precompilada:
```bash
pip install mysqlclient‑2.2.0‑cp311‑cp311‑win_amd64.whl
```

## Licencia

Proyecto bajo Licencia MIT.

## Autor

BrayamDev  
GitHub: [@BrayamDev](https://github.com/BrayamDev)
