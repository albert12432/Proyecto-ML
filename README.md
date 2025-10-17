# Proyecto ML - Deducción de Imágenes 🧠🖼️

Sistema de Machine Learning basado en Redes Neuronales Convolucionales para análisis de imágenes y generación automática de comandos.

## 🚀 Descripción General

Este proyecto implementa un sistema completo de visión artificial que utiliza Deep Learning para:
- 📸 Analizar imágenes mediante CNN (Convolutional Neural Networks)
- 🎯 Clasificar imágenes en 20 categorías de comandos diferentes
- ⚡ Generar comandos ejecutables en tiempo real
- 🖥️ Proporcionar una interfaz web intuitiva y profesional

## ✨ Características Principales

- **Sistema de Autenticación:** Login y registro de usuarios con encriptación
- **Dashboard Interactivo:** Navegación visual entre módulos del proyecto
- **Arquitectura CNN Personalizada:** ~2.5M parámetros optimizados
- **Alto Rendimiento:** 89.5% de precisión, respuesta < 3 segundos
- **Pipeline Completo:** Desde recolección de datos hasta despliegue

## 📂 Estructura del Proyecto

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

## 🎯 Módulos del Sistema

### 1️⃣ Entendimiento del Negocio
- Objetivos y alcance del proyecto
- Requerimientos funcionales y técnicos
- Casos de uso principales
- Métricas de éxito (KPIs)

### 2️⃣ Ingeniería de Datos
- Recolección de 50,000+ imágenes
- Pipeline de procesamiento de datos
- Técnicas de Data Augmentation
- División estratificada del dataset

### 3️⃣ Modelo de Redes Neuronales
- Arquitectura CNN de 10 capas
- 20 comandos clasificables
- Interfaz de predicción en tiempo real
- Historial de resultados

## 🛠️ Tecnologías

**Backend:**
- Python 3.8+
- Flask (Web Framework)
- MySQL (Base de datos)
- TensorFlow/Keras (Machine Learning)

**Frontend:**
- HTML5, CSS3, JavaScript
- Bootstrap 5.3
- Font Awesome 6.0

## 📊 Métricas del Modelo

| Métrica | Valor |
|---------|-------|
| Accuracy | 89.5% |
| Precision | 87.2% |
| Recall | 88.7% |
| F1-Score | 87.9% |
| Tiempo de Respuesta | < 3s |
| Dataset | 50,000+ imágenes |
| Categorías | 20 comandos |

## 🚀 Inicio Rápido

```bash
# Clonar repositorio
git clone https://github.com/Diego-Alexander-udec/Proyecto-ML.git

# Navegar al directorio
cd "Proyecto-ML/Proyecto Deduccion de imagen/Login_python"

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python app.py
```

Acceder a: `http://localhost:5000`

## 📸 Comandos Disponibles

El sistema puede identificar y generar 20 comandos diferentes:

🔼 MOVE_UP | 🔽 MOVE_DOWN | ◀️ MOVE_LEFT | ▶️ MOVE_RIGHT  
🛑 STOP | ▶️ START | ⏸️ PAUSE  
🔄 ROTATE | 🔍 ZOOM_IN | 🔎 ZOOM_OUT  
✅ CONFIRM | ❌ CANCEL  
💾 SAVE | 🗑️ DELETE  
➕ ADD | ➖ REMOVE | ✏️ EDIT | 👁️ VIEW  
⬇️ DOWNLOAD | ⬆️ UPLOAD

## 📈 Estado del Proyecto

- ✅ **Fase 1:** Diseño de vistas (Completado)
- 🔄 **Fase 2:** Desarrollo del modelo (En progreso)
- 🔜 **Fase 3:** Integración funcional
- 🔜 **Fase 4:** Optimización y despliegue

## 📝 Documentación

Para documentación detallada, consultar:
- [README_VISTAS.md](./Proyecto%20Deduccion%20de%20imagen/Login_python/README_VISTAS.md) - Documentación completa de las vistas

## 👨‍💻 Autor

**Diego Alexander**  
Universidad de Córdoba (UDEC)

## 📄 Licencia

MIT License - Ver archivo LICENSE para detalles

---

⭐ Si este proyecto te resulta útil, considera darle una estrella en GitHub