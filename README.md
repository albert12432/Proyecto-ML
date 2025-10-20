# Proyecto ML - Reconocimiento de Lenguaje de Señas

Sistema de Machine Learning basado en Redes Neuronales Convolucionales para el reconocimiento y traducción de lenguaje de señas a texto mediante análisis de imágenes.

## Descripción

Este proyecto implementa un sistema de visión artificial que utiliza Deep Learning para:
- Analizar imágenes de gestos de lenguaje de señas mediante CNN (Convolutional Neural Networks)
- Reconocer y clasificar señas correspondientes a letras del alfabeto
- Predecir letras en tiempo real desde cámara web o imágenes subidas
- Proporcionar una interfaz web intuitiva para interactuar con el modelo

## Características

- Sistema de autenticación con login y registro de usuarios
- Dashboard interactivo con navegación entre módulos del proyecto
- Carga de imágenes estáticas o captura en tiempo real desde webcam
- Arquitectura CNN con 2.3M parámetros optimizada para reconocimiento de gestos
- Alta precisión de clasificación (objetivo: >94%)
- Pipeline completo de Machine Learning desde datos hasta despliegue

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
- Objetivos: Sistema de traducción de lenguaje de señas a texto
- Público objetivo: Personas con discapacidad auditiva y sus interlocutores
- Casos de uso: Comunicación inclusiva, educación, accesibilidad
- Análisis de viabilidad técnica y social

### Fase 2: Entendimiento e Ingeniería de Datos
- Dataset de imágenes de señas del alfabeto (letras A-Z)
- Recolección mediante cámara web y datasets públicos
- Pipeline de procesamiento: normalización, redimensionamiento, augmentation
- Técnicas de Data Augmentation: rotación, zoom, flip horizontal
- División del dataset (70% entrenamiento, 15% validación, 15% prueba)

### Fase 3: Modelo de Redes Neuronales
- Arquitectura CNN especializada en reconocimiento de gestos
- Capas convolucionales para extracción de características de manos
- Clasificación de 26 letras del alfabeto (A-Z) o más según el alcance
- Predicción en tiempo real desde webcam
- Carga de imágenes estáticas para predicción
- Visualización de resultados con probabilidades por letra

## Tecnologías

**Backend:**
- Python 3.8+
- Flask 2.3.3
- MySQL
- Flask-MySQLdb
- Flask-Bcrypt
- TensorFlow/Keras (para el modelo CNN)
- OpenCV (procesamiento de imágenes)
- NumPy, Pandas (manipulación de datos)

**Frontend:**
- HTML5, CSS3, JavaScript
- Bootstrap 5.3.0
- Font Awesome 6.0.0
- Webcam.js (captura de video en tiempo real)

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

## Funcionalidades del Sistema

### Reconocimiento de Señas
El sistema puede reconocer gestos de lenguaje de señas y traducirlos a letras:

**Modos de entrada:**
- Carga de imagen estática (formatos: JPG, PNG)
- Captura en tiempo real desde webcam

**Proceso de predicción:**
1. El usuario sube una imagen o activa la webcam
2. La imagen se procesa y normaliza
3. El modelo CNN analiza el gesto
4. Se muestra la letra predicha con su nivel de confianza
5. Historial de predicciones disponible

**Alfabeto reconocible:**
Letras A-Z del lenguaje de señas (26 clases o más según configuración)

## Estado del Proyecto

- Fase 1: Diseño de vistas y arquitectura web (Completado)
- Fase 2: Recolección y preparación del dataset de señas (En progreso)
- Fase 3: Desarrollo y entrenamiento del modelo CNN (Pendiente)
- Fase 4: Integración del modelo con la interfaz web (Pendiente)
- Fase 5: Optimización y despliegue (Pendiente)

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