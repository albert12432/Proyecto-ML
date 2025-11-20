# 🚀 Guía Rápida de Instalación y Ejecución

## ⚡ Inicio Rápido (5 minutos)

### 1️⃣ Prerrequisitos

Antes de comenzar, asegúrate de tener instalado:

- ✅ **Python 3.8 o superior** → [Descargar Python](https://www.python.org/downloads/)
- ✅ **MySQL Server** → [Descargar MySQL](https://dev.mysql.com/downloads/)
- ✅ **Git** (opcional) → [Descargar Git](https://git-scm.com/downloads/)

### 2️⃣ Clonar el Repositorio

```bash
# Opción 1: Con Git
git clone https://github.com/Diego-Alexander-udec/Proyecto-ML.git
cd Proyecto-ML/Proyecto\ Deduccion\ de\ imagen/Login_python

# Opción 2: Descargar ZIP
# Descargar desde GitHub y extraer
cd ruta/al/proyecto/Login_python
```

### 3️⃣ Crear Entorno Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 4️⃣ Instalar Dependencias

```bash
pip install -r requirements.txt
```

**Dependencias instaladas:**
- Flask
- Flask-MySQLdb
- Flask-Bcrypt
- mysqlclient

### 5️⃣ Configurar Base de Datos

#### Opción A: Línea de Comandos MySQL

```bash
# Conectar a MySQL
mysql -u root -p

# En la consola MySQL:
CREATE DATABASE flask_login;
USE flask_login;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

EXIT;
```

#### Opción B: Ejecutar Script SQL

```bash
mysql -u root -p < database.sql
```

### 6️⃣ Configurar Credenciales (Opcional)

Si tus credenciales de MySQL son diferentes:

Editar `app.py`:
```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'          # ← Cambiar aquí
app.config['MYSQL_PASSWORD'] = ''          # ← Cambiar aquí
app.config['MYSQL_DB'] = 'flask_login'
```

### 7️⃣ Ejecutar la Aplicación

```bash
python app.py
```

**Salida esperada:**
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### 8️⃣ Acceder al Sistema

Abrir navegador en: **http://localhost:5000**

---

## 🔐 Primer Uso

### Crear una Cuenta

1. Hacer clic en "Registro" o ir a `/register`
2. Ingresar:
   - **Usuario:** tu_usuario
   - **Contraseña:** tu_contraseña_segura
3. Hacer clic en "Registrarse"

### Iniciar Sesión

1. En `/login` ingresar:
   - **Usuario:** tu_usuario
   - **Contraseña:** tu_contraseña
2. Hacer clic en "Iniciar sesión"

### Explorar las Vistas

Una vez autenticado, navegar por:
- 🏠 **Home** - Dashboard principal
- 💼 **Negocio** - Objetivos y requerimientos
- 💾 **Datos** - Ingeniería de datos
- 🧠 **Modelo** - Redes neuronales

---

## 🛠️ Solución de Problemas

### Error: "No module named 'flask'"

```bash
# Asegurarse de que el entorno virtual está activado
# Windows:
venv\Scripts\activate

# Instalar dependencias nuevamente
pip install -r requirements.txt
```

### Error: "Access denied for user 'root'@'localhost'"

**Solución 1: Verificar credenciales**
```python
# En app.py, verificar:
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'tu_password_real'
```

**Solución 2: Crear usuario MySQL específico**
```sql
CREATE USER 'flask_user'@'localhost' IDENTIFIED BY 'flask_password';
GRANT ALL PRIVILEGES ON flask_login.* TO 'flask_user'@'localhost';
FLUSH PRIVILEGES;
```

### Error: "mysqlclient installation error"

**Windows:**
```bash
pip install wheel
pip install mysqlclient
```

Si persiste el error, instalar:
1. Visual C++ Build Tools: https://visualstudio.microsoft.com/downloads/
2. MySQL Connector C: https://dev.mysql.com/downloads/connector/c/

**Linux:**
```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
pip install mysqlclient
```

**Mac:**
```bash
brew install mysql
pip install mysqlclient
```

### Error: "Port 5000 is already in use"

```bash
# Cambiar puerto en app.py:
if __name__ == '__main__':
    app.run(debug=True, port=5001)
```

### Base de Datos no se Crea

```bash
# Verificar que MySQL está corriendo
# Windows:
services.msc  # Buscar "MySQL" y verificar que está "Running"

# Linux:
sudo systemctl status mysql

# Mac:
mysql.server status
```

---

## 📦 Contenido de requirements.txt

```txt
Flask==2.3.3
Flask-MySQLdb==1.0.1
Flask-Bcrypt==1.0.1
mysqlclient==2.2.0
```

---

## 🎯 Comandos Útiles

### Activar/Desactivar Entorno Virtual

```bash
# Activar
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Desactivar
deactivate
```

### Verificar Instalaciones

```bash
# Verificar Python
python --version

# Verificar pip
pip --version

# Verificar MySQL
mysql --version

# Listar paquetes instalados
pip list
```

### Detener la Aplicación

```bash
# En la terminal donde está corriendo Flask:
Ctrl + C
```

---

## 🔄 Actualizar el Proyecto

```bash
# Si hay cambios en el repositorio
git pull origin main

# Actualizar dependencias
pip install -r requirements.txt --upgrade
```

---

## 🗂️ Estructura de Archivos

```
Login_python/
│
├── app.py                  ← Aplicación Flask principal
├── database.sql            ← Script de base de datos
├── requirements.txt        ← Dependencias Python
├── INICIO_RAPIDO.md       ← Esta guía
│
├── templates/              ← Plantillas HTML
│   ├── login.html
│   ├── register.html
│   ├── home.html
│   ├── entendimiento_negocio.html
│   ├── ingenieria_datos.html
│   └── modelo_neural.html
│
└── venv/                   ← Entorno virtual (crear)
```

---

## 📊 Verificar que Todo Funciona

### Checklist de Verificación

- [ ] MySQL está corriendo
- [ ] Base de datos `flask_login` creada
- [ ] Tabla `users` existe
- [ ] Entorno virtual activado
- [ ] Dependencias instaladas
- [ ] `python app.py` ejecuta sin errores
- [ ] Navegador abre en `localhost:5000`
- [ ] Página de login se muestra correctamente
- [ ] Registro de usuario funciona
- [ ] Login con usuario registrado funciona
- [ ] Dashboard se muestra correctamente
- [ ] Navegación entre vistas funciona
- [ ] Logout funciona

---

## 🆘 Soporte Adicional

### Recursos
- 📘 [Documentación Flask](https://flask.palletsprojects.com/)
- 📘 [Documentación MySQL](https://dev.mysql.com/doc/)
- 📘 [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/)

### Reportar Problemas
Si encuentras un problema que no está cubierto aquí:
1. Verificar la documentación en `README_VISTAS.md`
2. Revisar los logs en la terminal
3. Abrir un issue en GitHub

---

## 🎉 ¡Listo para Usar!

Una vez completados todos los pasos, deberías ver:

```
✅ Python instalado
✅ MySQL configurado
✅ Entorno virtual activo
✅ Dependencias instaladas
✅ Base de datos creada
✅ Aplicación corriendo
✅ Navegador mostrando login
```

**¡Ahora puedes explorar todas las vistas del proyecto!** 🚀

---

## 🔥 Comandos de un Solo Paso (Para Expertos)

### Windows (PowerShell)

```powershell
# Configuración completa
python -m venv venv; .\venv\Scripts\Activate.ps1; pip install -r requirements.txt; python app.py
```

### Linux/Mac (Bash)

```bash
# Configuración completa
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python app.py
```

**Nota:** Debes haber creado la base de datos MySQL previamente.

---

**Tiempo estimado de configuración:** 5-10 minutos  
**Dificultad:** ⭐⭐☆☆☆ (Fácil)  
**Última actualización:** 15 de Octubre, 2025
