# Proyecto ML - Deducción de Imágenes mediante Redes Neuronales

Sistema de Machine Learning que utiliza redes neuronales convolucionales (CNN) para analizar imágenes y generar comandos automáticos.

## 📋 Descripción del Proyecto

Este proyecto implementa un sistema completo de visión artificial basado en Deep Learning que:
- Analiza imágenes mediante una red neuronal convolucional
- Identifica patrones visuales específicos
- Genera comandos ejecutables basados en el análisis
- Proporciona una interfaz web intuitiva para usuarios

## 🎯 Objetivos

1. Desarrollar un modelo CNN capaz de clasificar imágenes en 20 categorías de comandos
2. Lograr una precisión mínima del 85% en predicciones
3. Procesar imágenes en tiempo real (< 3 segundos)
4. Proporcionar una interfaz amigable para usuarios no técnicos

## 🏗️ Estructura del Proyecto

```
Proyecto Deduccion de imagen/
├── Login_python/
│   ├── app.py                          # Aplicación Flask principal
│   ├── database.sql                    # Script de base de datos
│   ├── requirements.txt                # Dependencias del proyecto
│   ├── README_VISTAS.md               # Esta documentación
│   └── templates/
│       ├── login.html                  # Página de inicio de sesión
│       ├── register.html               # Página de registro
│       ├── home.html                   # Página principal con navegación
│       ├── entendimiento_negocio.html  # Vista de entendimiento del negocio
│       ├── ingenieria_datos.html       # Vista de ingeniería de datos
│       └── modelo_neural.html          # Vista del modelo y predicciones
```

## 📊 Vistas del Sistema

### 1. Home (Página Principal)
**Ruta:** `/home`

Página de inicio que presenta:
- Mensaje de bienvenida personalizado
- Tarjetas de navegación a las 3 secciones principales
- Estadísticas generales del proyecto
- Barra de navegación consistente

**Características:**
- Navegación visual con iconos
- Tarjetas interactivas con efectos hover
- Información resumida del proyecto

### 2. Entendimiento del Negocio
**Ruta:** `/entendimiento-negocio`

Sección dedicada a la definición del proyecto:

**Contenido:**
- **Objetivos del Proyecto:** Metas y alcance del sistema
- **Requerimientos Funcionales:** Funcionalidades esperadas
- **Requerimientos Técnicos:** Especificaciones técnicas mínimas
- **Casos de Uso:** Escenarios de aplicación del sistema
- **Métricas de Éxito:** KPIs y objetivos cuantificables

**Métricas destacadas:**
- Precisión del modelo: 85%+
- Tiempo de respuesta: < 3s
- Usuarios concurrentes: 100+
- Satisfacción del usuario: 95%+

### 3. Entendimiento de Datos e Ingeniería de Datos
**Ruta:** `/ingenieria-datos`

Sección enfocada en el procesamiento de datos:

**Contenido:**
- **Fuentes de Datos:**
  - Imágenes propias
  - Datasets públicos (ImageNet, COCO)
  - Contribuciones de usuarios
  - Data Augmentation

- **Características del Dataset:**
  - Total: 50,000+ imágenes
  - Categorías: 20 comandos
  - Resolución: 224x224 px
  - Tamaño: 15 GB

- **Pipeline de Procesamiento:**
  1. Carga de datos
  2. Limpieza de datos
  3. Preprocesamiento
  4. Aumento de datos
  5. Etiquetado
  6. División del dataset (70/15/15)

- **Calidad de Datos:**
  - Completitud: 95%
  - Consistencia: 92%
  - Precisión: 88%
  - Unicidad: 97%

- **Técnicas de Ingeniería:**
  - Normalización de píxeles
  - Feature Extraction
  - Balanceo de clases

### 4. Modelo de Redes Neuronales
**Ruta:** `/modelo-neural`

Sección dedicada al modelo y predicciones:

**Contenido:**
- **Arquitectura del Modelo (CNN):**
  - Input Layer: 224x224x3
  - 3 Capas Convolucionales (32, 64, 128 filtros)
  - 2 Capas MaxPooling
  - GlobalAveragePooling2D
  - 2 Capas Dense (256, 128 neuronas)
  - Output Layer: 20 neuronas (Softmax)
  - Total de parámetros: ~2.5M

- **Hiperparámetros:**
  - Batch Size: 32
  - Épocas: 100
  - Learning Rate: 0.001
  - Dropout: 0.5 / 0.3

- **Métricas de Rendimiento:**
  - Accuracy: 89.5%
  - Precision: 87.2%
  - Recall: 88.7%
  - F1-Score: 87.9%

- **Interfaz de Predicción:**
  - Carga de imágenes (drag & drop)
  - Vista previa de imagen
  - Análisis en tiempo real
  - Comando generado con nivel de confianza

- **20 Comandos Disponibles:**
  - MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT
  - STOP, START, PAUSE
  - ROTATE, ZOOM_IN, ZOOM_OUT
  - CONFIRM, CANCEL
  - SAVE, DELETE
  - ADD, REMOVE, EDIT, VIEW
  - DOWNLOAD, UPLOAD

- **Historial de Predicciones:**
  - Registro de todas las predicciones
  - Niveles de confianza
  - Estado de ejecución

## 🚀 Instalación y Ejecución

### Prerrequisitos
- Python 3.8+
- MySQL Server
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/Diego-Alexander-udec/Proyecto-ML.git
cd Proyecto-ML/Proyecto\ Deduccion\ de\ imagen/Login_python
```

2. **Crear entorno virtual:**
```bash
python -m venv venv
```

3. **Activar entorno virtual:**
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

5. **Configurar base de datos:**
- Crear base de datos MySQL
- Ejecutar el script `database.sql`
- Actualizar credenciales en `app.py` si es necesario

6. **Ejecutar la aplicación:**
```bash
python app.py
```

7. **Acceder a la aplicación:**
Abrir navegador en: `http://localhost:5000`

## 🔐 Autenticación

El sistema requiere registro e inicio de sesión:
- **Registro:** `/register` - Crear nueva cuenta
- **Login:** `/login` - Iniciar sesión
- **Logout:** Botón en barra de navegación

## 🎨 Tecnologías Utilizadas

### Backend
- **Flask:** Framework web Python
- **Flask-MySQLdb:** Conexión con MySQL
- **Flask-Bcrypt:** Encriptación de contraseñas
- **Python 3.8+**

### Frontend
- **HTML5**
- **CSS3**
- **Bootstrap 5.3:** Framework CSS
- **Font Awesome 6.0:** Iconos
- **JavaScript (vanilla)**

### Machine Learning (Futuro)
- **TensorFlow / Keras:** Construcción del modelo CNN
- **NumPy:** Procesamiento numérico
- **Pandas:** Manipulación de datos
- **OpenCV:** Procesamiento de imágenes
- **Pillow:** Manejo de imágenes

## 📈 Metodología

El proyecto sigue la metodología **CRISP-DM** (Cross Industry Standard Process for Data Mining):

1. ✅ **Entendimiento del Negocio:** Definición de objetivos
2. ✅ **Entendimiento de los Datos:** Análisis exploratorio
3. ✅ **Preparación de Datos:** Limpieza y transformación
4. 🔄 **Modelado:** Construcción del modelo CNN
5. 🔄 **Evaluación:** Validación del modelo
6. 🔄 **Despliegue:** Implementación en producción

## 🎯 Roadmap

### Fase 1: ✅ Diseño de Vistas (Actual)
- [x] Vista de entendimiento del negocio
- [x] Vista de ingeniería de datos
- [x] Vista del modelo neural
- [x] Sistema de navegación
- [x] Sistema de autenticación

### Fase 2: 🔄 Desarrollo del Modelo
- [ ] Recolección de datos
- [ ] Preprocesamiento de imágenes
- [ ] Entrenamiento del modelo CNN
- [ ] Optimización de hiperparámetros
- [ ] Validación y testing

### Fase 3: 🔜 Integración
- [ ] API para predicciones
- [ ] Carga de imágenes funcional
- [ ] Procesamiento en tiempo real
- [ ] Almacenamiento de resultados
- [ ] Historial de predicciones funcional

### Fase 4: 🔜 Mejoras
- [ ] Optimización de rendimiento
- [ ] Transfer Learning
- [ ] Despliegue en la nube
- [ ] API REST documentada
- [ ] Testing automatizado

## 👥 Equipo de Desarrollo

- **Desarrollador Principal:** Diego Alexander
- **Institución:** UDEC

## 📝 Notas Importantes

- Las vistas actuales son prototipos de visualización
- Los datos mostrados son ejemplos ilustrativos
- El modelo CNN está en fase de diseño
- La funcionalidad de predicción será implementada en futuras fases

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

## 📧 Contacto

Para preguntas o sugerencias, contactar a través del repositorio de GitHub.

---

**Fecha de última actualización:** 15 de Octubre, 2025
**Versión:** 1.0.0 - Diseño de Vistas
