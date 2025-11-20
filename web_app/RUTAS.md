# 🗺️ Mapa de Rutas del Sistema

## Rutas Disponibles

### 🔐 Autenticación

| Ruta | Método | Descripción | Requiere Auth |
|------|--------|-------------|---------------|
| `/` | GET | Redirige a home o login según estado | No |
| `/login` | GET, POST | Página de inicio de sesión | No |
| `/register` | GET, POST | Página de registro de usuario | No |
| `/logout` | GET | Cierra sesión del usuario | Sí |

### 📊 Páginas Principales

| Ruta | Método | Descripción | Requiere Auth |
|------|--------|-------------|---------------|
| `/home` | GET | Dashboard principal con navegación | Sí |
| `/entendimiento-negocio` | GET | Vista de objetivos y requerimientos | Sí |
| `/ingenieria-datos` | GET | Vista de procesamiento de datos | Sí |
| `/modelo-neural` | GET | Vista del modelo y predicciones | Sí |

## 🎨 Componentes de las Vistas

### Home (`/home`)
```
┌─────────────────────────────────────────┐
│  🧠 Proyecto ML - Deducción de Imágenes│
├─────────────────────────────────────────┤
│                                         │
│  Bienvenido, [Usuario]!                │
│  Sistema de Deducción de Imágenes      │
│                                         │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐  │
│  │ 💼      │ │ 💾      │ │ 🧠      │  │
│  │Negocio  │ │ Datos   │ │ Modelo  │  │
│  └─────────┘ └─────────┘ └─────────┘  │
│                                         │
│  Estadísticas: 50K+ | 20 | 89.5% | <3s│
└─────────────────────────────────────────┘
```

### Entendimiento del Negocio (`/entendimiento-negocio`)
```
┌─────────────────────────────────────────┐
│  💼 Entendimiento del Negocio          │
├─────────────────────────────────────────┤
│                                         │
│  🎯 Objetivos del Proyecto             │
│  ├─ Identificar patrones visuales      │
│  ├─ Generar comandos automáticos       │
│  └─ Optimizar procesos                 │
│                                         │
│  📋 Requerimientos                     │
│  ├─ Funcionales: Carga, proceso, UI    │
│  └─ Técnicos: 85%, <3s, escalable     │
│                                         │
│  👥 Casos de Uso                       │
│  ├─ Análisis de imágenes               │
│  ├─ Generación de comandos             │
│  └─ Monitoreo de resultados            │
│                                         │
│  🏆 Métricas: 85%+ | <3s | 100+ | 95%+ │
└─────────────────────────────────────────┘
```

### Ingeniería de Datos (`/ingenieria-datos`)
```
┌─────────────────────────────────────────┐
│  💾 Ingeniería de Datos                │
├─────────────────────────────────────────┤
│                                         │
│  📥 Fuentes de Datos                   │
│  ├─ Imágenes propias                   │
│  ├─ Datasets públicos (ImageNet, COCO) │
│  ├─ Contribuciones usuarios            │
│  └─ Data Augmentation                  │
│                                         │
│  📊 Dataset                            │
│  ├─ Total: 50,000+ imágenes            │
│  ├─ Categorías: 20 comandos            │
│  ├─ Resolución: 224x224 px             │
│  └─ Tamaño: 15 GB                      │
│                                         │
│  🔄 Pipeline                           │
│  1. Carga de datos                     │
│  2. Limpieza                           │
│  3. Preprocesamiento                   │
│  4. Data Augmentation                  │
│  5. Etiquetado                         │
│  6. División (70/15/15)                │
│                                         │
│  ✅ Calidad: 95% | 92% | 88% | 97%    │
└─────────────────────────────────────────┘
```

### Modelo Neural (`/modelo-neural`)
```
┌─────────────────────────────────────────┐
│  🧠 Modelo de Redes Neuronales         │
├─────────────────────────────────────────┤
│                                         │
│  🏗️ Arquitectura CNN                   │
│  ├─ Input Layer: 224x224x3             │
│  ├─ Conv2D (32) + MaxPooling           │
│  ├─ Conv2D (64) + MaxPooling           │
│  ├─ Conv2D (128) + GlobalAvgPooling    │
│  ├─ Dense (256) + Dropout(0.5)         │
│  ├─ Dense (128) + Dropout(0.3)         │
│  └─ Output (20) - Softmax              │
│                                         │
│  ⚙️ Hiperparámetros                    │
│  ├─ Batch Size: 32                     │
│  ├─ Épocas: 100                        │
│  ├─ Learning Rate: 0.001               │
│  └─ Parámetros: ~2.5M                  │
│                                         │
│  📈 Rendimiento                        │
│  ├─ Accuracy: 89.5%                    │
│  ├─ Precision: 87.2%                   │
│  ├─ Recall: 88.7%                      │
│  └─ F1-Score: 87.9%                    │
│                                         │
│  🎯 Interfaz de Predicción             │
│  ├─ Carga de imagen (drag & drop)      │
│  ├─ Análisis en tiempo real            │
│  ├─ Comando generado + confianza       │
│  └─ Historial de resultados            │
│                                         │
│  🎮 20 Comandos: ⬆️⬇️⬅️➡️🛑▶️⏸️🔄🔍...   │
└─────────────────────────────────────────┘
```

## 🔄 Flujo de Navegación

```
┌─────────┐
│ Login   │
│/login   │
└────┬────┘
     │
     ▼
┌─────────┐    ┌──────────────────┐
│Register │◄──►│ Home Dashboard   │
│/register│    │ /home            │
└─────────┘    └────────┬─────────┘
                        │
         ┌──────────────┼──────────────┐
         │              │              │
         ▼              ▼              ▼
┌────────────┐  ┌─────────────┐  ┌──────────┐
│ Negocio    │  │ Datos       │  │ Modelo   │
│ /ent-neg   │  │ /ing-datos  │  │ /modelo  │
└────────────┘  └─────────────┘  └──────────┘
         │              │              │
         └──────────────┼──────────────┘
                        │
                        ▼
                   ┌─────────┐
                   │ Logout  │
                   │ /logout │
                   └─────────┘
```

## 🎨 Elementos Comunes

### Barra de Navegación (Todas las páginas autenticadas)
```
┌──────────────────────────────────────────────────────┐
│ 🧠 Proyecto ML │ 🏠 Inicio │ 💼 Negocio │ 💾 Datos │
│                │ 🧠 Modelo │ 🚪 Cerrar sesión        │
└──────────────────────────────────────────────────────┘
```

### Características de Diseño
- ✅ Responsive (Bootstrap 5.3)
- ✅ Iconos intuitivos (Font Awesome 6.0)
- ✅ Colores consistentes
- ✅ Animaciones suaves
- ✅ Cards con hover effects
- ✅ Navegación clara y accesible

## 🔒 Seguridad

### Protección de Rutas
- Todas las rutas principales requieren autenticación
- Redirección automática a `/login` si no hay sesión
- Headers de no-cache en todas las respuestas
- Contraseñas encriptadas con Bcrypt

### Sesiones
```python
session['username']  # Usuario autenticado
```

## 📱 Responsividad

Todas las vistas son completamente responsive:
- 📱 Móvil: 320px - 767px
- 📱 Tablet: 768px - 1023px
- 💻 Desktop: 1024px+

## 🎯 Próximas Funcionalidades

### Rutas Futuras (Pendientes)
- `/api/predict` - POST - Predicción de imágenes
- `/api/upload` - POST - Carga de imágenes
- `/api/history` - GET - Historial de predicciones
- `/api/stats` - GET - Estadísticas del usuario
- `/profile` - GET - Perfil de usuario
- `/admin` - GET - Panel administrativo

---

**Última actualización:** 15 de Octubre, 2025  
**Versión:** 1.0.0
