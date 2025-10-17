# 🎨 Guía de Diseño Visual del Sistema

## 🎨 Paleta de Colores

### Colores Principales
```css
/* Azul Primario (Barra de navegación) */
--primary-blue: #007bff;

/* Gradientes por Sección */
--gradient-negocio: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
--gradient-datos: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
--gradient-modelo: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
```

### Colores Semánticos
```css
--success: #28a745;  /* Verde - Éxito */
--warning: #ffc107;  /* Amarillo - Advertencia */
--danger: #dc3545;   /* Rojo - Error */
--info: #17a2b8;     /* Cian - Información */
--secondary: #6c757d; /* Gris - Secundario */
--dark: #343a40;     /* Negro - Oscuro */
```

### Colores de Fondo
```css
--bg-light: #f8f9fa;     /* Fondo claro */
--bg-white: #ffffff;     /* Blanco */
--bg-dark: #1e1e1e;      /* Terminal/Código */
--bg-terminal: #1e1e1e;  /* Terminal */
--text-terminal: #00ff00; /* Texto terminal */
```

## 📐 Espaciado y Dimensiones

### Contenedores
```css
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 15px;
}

.section-header {
    padding: 30px;
    margin-bottom: 30px;
    border-radius: 10px;
}

.card-custom {
    padding: 20px;
    border-radius: 10px;
}
```

### Iconos
```css
.icon-box {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    font-size: 24px;
}

.icon-circle {
    width: 100px;
    height: 100px;
    border-radius: 50%;
}

.fa-3x { font-size: 3rem; }
.fa-4x { font-size: 4rem; }
```

### Espaciado
```css
mt-3: 1rem (16px)
mt-4: 1.5rem (24px)
mb-3: 1rem (16px)
mb-4: 1.5rem (24px)
p-4: 1.5rem (24px) en todos los lados
```

## 🖼️ Componentes Visuales

### 1. Tarjetas (Cards)

#### Card Estándar
```html
<div class="card card-custom">
    <div class="card-body p-4">
        <div class="icon-box icon-box-[color]">
            <i class="fas fa-[icon]"></i>
        </div>
        <h3 class="card-title">Título</h3>
        <p class="card-text">Contenido...</p>
    </div>
</div>
```

#### Card con Hover Effect (Home)
```css
.hover-card {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.hover-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}
```

### 2. Sección Header

```html
<div class="section-header">
    <h1><i class="fas fa-[icon] me-3"></i>Título Principal</h1>
    <p class="mb-0">Descripción de la sección</p>
</div>
```

**Variantes por sección:**
- Negocio: `gradient-negocio` (Púrpura)
- Datos: `gradient-datos` (Verde-Cian)
- Modelo: `gradient-modelo` (Rosa-Rojo)

### 3. Icon Box

```html
<div class="icon-box icon-box-[color]">
    <i class="fas fa-[icon]"></i>
</div>
```

**Colores disponibles:**
- `icon-box-purple`: #e0d4f7 (fondo) / #667eea (icono)
- `icon-box-blue`: #d4e4f7 / #4a90e2
- `icon-box-green`: #d4f7e0 / #4ae290
- `icon-box-orange`: #f7e4d4 / #e2904a
- `icon-box-teal`: #d4f7f0 / #11998e
- `icon-box-cyan`: #d4eff7 / #1199e8
- `icon-box-lime`: #e8f7d4 / #7de811
- `icon-box-pink`: #ffe0f0 / #f093fb
- `icon-box-red`: #ffe0e0 / #f5576c

### 4. Barras de Progreso

```html
<div class="mb-3">
    <div class="d-flex justify-content-between mb-1">
        <span>Etiqueta</span>
        <span class="fw-bold">95%</span>
    </div>
    <div class="progress">
        <div class="data-quality-bar" style="width: 95%"></div>
    </div>
</div>
```

### 5. Pipeline Steps

```html
<div class="pipeline-step">
    <h5><i class="fas fa-[icon] text-[color] me-2"></i>Título</h5>
    <p class="mb-0 text-muted">Descripción del paso</p>
</div>
```

### 6. Badges de Comandos

```html
<span class="badge bg-[color] w-100 p-2">
    <i class="fas fa-[icon] me-2"></i>COMANDO
</span>
```

**Colores utilizados:**
- `bg-primary`, `bg-success`, `bg-warning`, `bg-danger`
- `bg-info`, `bg-secondary`, `bg-dark`

### 7. Terminal Output

```html
<div class="command-output">
    <div class="mb-2">
        <span class="text-info">$</span> Comando aquí...
    </div>
    <div class="mt-3">
        <span class="text-muted">// Comentario</span>
    </div>
</div>
```

```css
.command-output {
    background-color: #1e1e1e;
    color: #00ff00;
    padding: 20px;
    border-radius: 8px;
    font-family: 'Courier New', monospace;
    min-height: 150px;
}
```

### 8. Upload Area

```html
<div class="upload-area">
    <i class="fas fa-cloud-upload-alt fa-4x text-muted mb-3"></i>
    <h5>Arrastra o haz clic para cargar imagen</h5>
    <p class="text-muted mb-0">Formatos: JPG, PNG | Max: 10MB</p>
    <button class="btn btn-primary mt-3">
        <i class="fas fa-folder-open me-2"></i>Seleccionar Archivo
    </button>
</div>
```

```css
.upload-area {
    border: 3px dashed #dee2e6;
    border-radius: 10px;
    padding: 40px;
    text-align: center;
    transition: all 0.3s ease;
    cursor: pointer;
}

.upload-area:hover {
    border-color: #f093fb;
    background-color: #f8f9fa;
}
```

## 🎯 Barra de Navegación

```html
<nav class="navbar navbar-expand-lg navbar-custom">
    <div class="container-fluid">
        <a class="navbar-brand" href="{{ url_for('home') }}">
            <i class="fas fa-brain me-2"></i>Proyecto ML - Deducción de Imágenes
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link" href="{{ url_for('home') }}">
                        <i class="fas fa-home me-1"></i>Inicio
                    </a>
                </li>
                <!-- Más items... -->
            </ul>
        </div>
    </div>
</nav>
```

### Iconos de Navegación
- 🏠 Inicio: `fas fa-home`
- 💼 Negocio: `fas fa-briefcase`
- 💾 Datos: `fas fa-database`
- 🧠 Modelo: `fas fa-project-diagram`
- 🚪 Logout: `fas fa-sign-out-alt`

## 📊 Tablas

```html
<div class="table-responsive">
    <table class="table table-hover">
        <thead class="table-light">
            <tr>
                <th>#</th>
                <th>Columna 1</th>
                <th>Columna 2</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>Dato 1</td>
                <td>Dato 2</td>
            </tr>
        </tbody>
    </table>
</div>
```

## 🎭 Animaciones y Transiciones

### Hover Effects
```css
/* Cards */
transition: transform 0.3s ease;
transform: translateY(-5px) on hover;

/* Hover Cards (Home) */
transition: transform 0.3s ease, box-shadow 0.3s ease;
transform: translateY(-10px) on hover;

/* Upload Area */
transition: all 0.3s ease;
```

### Sombras
```css
box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);  /* Normal */
box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* Hover */
box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  /* Sutil */
```

## 📱 Responsive Design

### Breakpoints (Bootstrap 5)
```css
/* Extra small devices (portrait phones) */
@media (max-width: 575.98px) { }

/* Small devices (landscape phones) */
@media (min-width: 576px) and (max-width: 767.98px) { }

/* Medium devices (tablets) */
@media (min-width: 768px) and (max-width: 991.98px) { }

/* Large devices (desktops) */
@media (min-width: 992px) and (max-width: 1199.98px) { }

/* Extra large devices (large desktops) */
@media (min-width: 1200px) { }
```

### Clases de Columnas
```html
<!-- 3 columnas en desktop, 1 en móvil -->
<div class="col-md-4 mb-3">...</div>

<!-- 2 columnas en desktop, 1 en móvil -->
<div class="col-md-6 mb-3">...</div>

<!-- Full width en todas las pantallas -->
<div class="col-12 mb-4">...</div>
```

## 🖋️ Tipografía

### Fuentes
```css
/* Por defecto (Bootstrap) */
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, ...;

/* Terminal/Código */
font-family: 'Courier New', monospace;
```

### Tamaños de Texto
```css
display-6: 4rem (64px)
h1: 2.5rem (40px)
h2: 2rem (32px)
h3: 1.75rem (28px)
h4: 1.5rem (24px)
h5: 1.25rem (20px)
lead: 1.25rem (20px)
text: 1rem (16px)
small: 0.875rem (14px)
```

## 🎨 Utilidades de Bootstrap

### Espaciado
```html
mt-{n}: margin-top
mb-{n}: margin-bottom
ms-{n}: margin-start (left)
me-{n}: margin-end (right)
p-{n}: padding (todos los lados)
```

Donde `{n}` = 0, 1, 2, 3, 4, 5

### Texto
```html
text-primary, text-success, text-warning, etc.
text-muted: color gris claro
text-center, text-start, text-end
fw-bold: font-weight bold
lead: párrafo destacado
```

### Fondos
```html
bg-primary, bg-success, bg-warning, etc.
bg-light: fondo claro (#f8f9fa)
bg-white: fondo blanco
bg-transparent: fondo transparente
```

### Display
```html
d-flex: display flex
d-none: ocultar elemento
justify-content-between: espacio entre items
align-items-center: alinear verticalmente
```

## 🎯 Iconos Font Awesome Utilizados

### Por Sección
**Home:**
- `fa-brain` - Logo principal
- `fa-home` - Inicio
- `fa-briefcase` - Negocio
- `fa-database` - Datos
- `fa-project-diagram` - Modelo

**Negocio:**
- `fa-bullseye` - Objetivos
- `fa-clipboard-list` - Requerimientos
- `fa-cogs` - Técnicos
- `fa-users` - Casos de uso
- `fa-trophy` - Métricas

**Datos:**
- `fa-download` - Recolección
- `fa-chart-pie` - Características
- `fa-check-double` - Calidad
- `fa-project-diagram` - Pipeline
- `fa-camera, fa-cloud, fa-robot` - Fuentes

**Modelo:**
- `fa-network-wired` - Arquitectura
- `fa-sliders-h` - Hiperparámetros
- `fa-chart-line` - Rendimiento
- `fa-upload` - Carga de imagen
- `fa-terminal` - Comandos
- `fa-history` - Historial

## 📝 Mejores Prácticas

1. **Consistencia:** Usar las mismas clases y estilos en todas las vistas
2. **Accesibilidad:** Incluir atributos `alt` en imágenes, usar etiquetas semánticas
3. **Responsive:** Probar en múltiples tamaños de pantalla
4. **Performance:** Minimizar CSS/JS, usar CDN para librerías
5. **UX:** Feedback visual en interacciones, tiempos de carga claros

---

**Última actualización:** 15 de Octubre, 2025  
**Framework:** Bootstrap 5.3.0  
**Iconos:** Font Awesome 6.0.0
