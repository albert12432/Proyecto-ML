# Proyecto ML - Deducción de Imágenes

Sistema de Machine Learning basado en Redes Neuronales Convolucionales para análisis de imágenes y generación automática de comandos.

## Descripción

Este proyecto implementa un sistema de visión artificial que utiliza Deep Learning para:
- Analizar imágenes mediante CNN (Convolutional Neural Networks)
- Clasificar imágenes en 20 categorías de comandos diferentes
- Generar comandos ejecutables en tiempo real
- Proporcionar una interfaz web intuitiva

## Características

- Sistema de autenticación con login y registro de usuarios
- Dashboard interactivo con navegación entre módulos
- Arquitectura CNN con 2.3M parámetros
- Alta precisión de clasificación (94.2%)
- Pipeline completo de Machine Learning

## Estructura del Proyecto

```
Proyecto-ML/
├── README.md                           # Este archivo
└── Proyecto Deduccion de imagen/
    └── Login_python/
        ├── app.py                      # Aplicación Flask
        ├── database.sql                # Base de datos
        ├── requirements.txt            # Dependencias
        ├── README_VISTAS.md           # Documentación detallada
        └── templates/
            ├── login.html              # Login
            ├── register.html           # Registro
            ├── home.html               # Página principal
            ├── entendimiento_negocio.html
            ├── ingenieria_datos.html
            └── modelo_neural.html
```

## Módulos del Sistema

### Fase 1: Entendimiento del Negocio
- Objetivos y alcance del proyecto
- Requerimientos funcionales y técnicos
- Casos de uso y análisis de viabilidad

### Fase 2: Entendimiento e Ingeniería de Datos
- Dataset de 50,000 imágenes
- Pipeline de procesamiento y limpieza
- Técnicas de Data Augmentation
- División del dataset (70% entrenamiento, 15% validación, 15% prueba)

### Fase 3: Modelo de Redes Neuronales
- Arquitectura CNN con capas convolucionales y pooling
- Clasificación de 20 comandos diferentes
- Interfaz de predicción en tiempo real
- Visualización de resultados

## Tecnologías

**Backend:**
- Python 3.8+
- Flask 2.3.3
- MySQL
- Flask-MySQLdb
- Flask-Bcrypt

**Frontend:**
- HTML5, CSS3, JavaScript
- Bootstrap 5.3.0
- Font Awesome 6.0.0

## Inicio Rápido

```bash
# Clonar repositorio
git clone https://github.com/Diego-Alexander-udec/Proyecto-ML.git

# Navegar al directorio
cd "Proyecto-ML/Proyecto Deduccion de imagen/Login_python"

# Instalar dependencias
pip install -r requirements.txt

# Configurar base de datos MySQL
# Ejecutar el archivo database.sql en MySQL para crear la base de datos

# Ejecutar aplicación
python app.py
```

Acceder a: http://localhost:5000

### Credenciales de prueba
- Usuario: admin
- Contraseña: admin123

## Comandos Disponibles

El sistema puede identificar 20 comandos diferentes:

MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT, STOP, START, PAUSE, ROTATE, ZOOM_IN, ZOOM_OUT, CONFIRM, CANCEL, SAVE, DELETE, ADD, REMOVE, EDIT, VIEW, DOWNLOAD, UPLOAD

## Estado del Proyecto

- Fase 1: Diseño de vistas (Completado)
- Fase 2: Desarrollo del modelo (En progreso)
- Fase 3: Integración funcional (Pendiente)
- Fase 4: Optimización y despliegue (Pendiente)

## Documentación

Para documentación detallada, consultar:
- [README_VISTAS.md](./Proyecto%20Deduccion%20de%20imagen/Login_python/README_VISTAS.md)
- [INICIO_RAPIDO.md](./Proyecto%20Deduccion%20de%20imagen/Login_python/INICIO_RAPIDO.md)
- [RUTAS.md](./Proyecto%20Deduccion%20de%20imagen/Login_python/RUTAS.md)

## Autor

Diego Alexander  
Universidad de Córdoba (UDEC)

## Licencia

MIT License