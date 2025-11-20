# 🎨 Guía de Diseño - Proyecto ML

## Sistema de Diseño Basado en Google Cloud / Material Design

Este proyecto utiliza el sistema de diseño de Google Cloud para crear una experiencia visual limpia, profesional y moderna.

---

## 🎯 Principios de Diseño

1. **Minimalismo**: Enfoque en contenido, reducción de elementos decorativos
2. **Claridad**: Jerarquía tipográfica clara y espaciado generoso
3. **Consistencia**: Componentes reutilizables con patrones coherentes
4. **Accesibilidad**: Contraste adecuado y tamaños de fuente legibles

---

## 🎨 Paleta de Colores

### Colores Principales
```css
--primary: #1a73e8          /* Google Blue - Botones, enlaces, elementos interactivos */
--primary-hover: #1765cc    /* Estado hover del azul primario */
--text-primary: #202124     /* Texto principal (títulos, contenido) */
--text-secondary: #5f6368   /* Texto secundario (descripciones, etiquetas) */
```

### Colores de Superficie
```css
--surface: #ffffff          /* Fondo de tarjetas y componentes */
--background: #f8f9fa       /* Fondo general de la página */
--border: #dadce0          /* Bordes sutiles */
```

### Colores Semánticos
```css
--success: #1e8e3e         /* Estados de éxito */
--warning: #f9ab00         /* Advertencias */
--danger: #d93025          /* Errores o acciones destructivas */
```

---

## 📝 Tipografía

### Fuentes
- **Google Sans**: Títulos y encabezados (400, 500, 700)
- **Roboto**: Texto de cuerpo (300, 400, 500)

### Escala Tipográfica
```css
h1: 36px / font-weight: 400    /* Títulos principales */
h2: 28px / font-weight: 400    /* Títulos de sección */
h3: 20px / font-weight: 500    /* Subtítulos */
body: 14px / font-weight: 400  /* Texto general */
```

### Características
- **Line-height**: 1.6 (mayor legibilidad)
- **Letter-spacing**: 0 (diseño limpio)
- **Antialiasing**: Activado para renderizado suave

---

## 🧩 Componentes

### Tarjetas (Cards)
```css
- Border-radius: 8px
- Border: 1px solid var(--border)
- Padding: 24px
- Shadow: Material Design elevation (multi-capa)
- Hover: Elevación aumentada + border azul sutil
```

### Botones
```css
Primary:
  - Background: #1a73e8
  - Padding: 10px 24px
  - Border-radius: 4px
  - Font-weight: 500
  - Letter-spacing: 0.25px
  - Shadow: Material Design elevation
  - Hover: Lift effect (translateY(-1px))

Outline:
  - Border: var(--border)
  - Hover: Background rgba(26, 115, 232, 0.04)
```

### Navegación
```css
- Background: white
- Border-bottom: 1px solid var(--border)
- Active state: 3px bottom border en primary
- Hover: Background light blue (rgba(26, 115, 232, 0.04))
- Logo: 28x28px con spacing de 8px
```

### Icon Boxes
```css
- Size: 48px x 48px (círculo)
- Background: rgba(26, 115, 232, 0.08)
- Color: var(--primary)
- Border-radius: 50%
```

---

## 🌊 Sombras (Material Design Elevation)

### Nivel 1 (Cards en reposo)
```css
box-shadow: 
  0 1px 2px 0 rgba(60, 64, 67, 0.3),
  0 1px 3px 1px rgba(60, 64, 67, 0.15);
```

### Nivel 2 (Cards hover / Botones)
```css
box-shadow: 
  0 1px 2px 0 rgba(60, 64, 67, 0.3),
  0 2px 6px 2px rgba(60, 64, 67, 0.15);
```

### Nivel 3 (Elevación máxima)
```css
box-shadow: 
  0 1px 3px 0 rgba(60, 64, 67, 0.3),
  0 4px 8px 3px rgba(60, 64, 67, 0.15);
```

---

## 📐 Espaciado

### Sistema de Espaciado
```
8px   → Espaciado mínimo (gaps pequeños)
12px  → Espaciado entre elementos relacionados
16px  → Espaciado estándar (margins, padding)
24px  → Espaciado entre secciones
32px  → Espaciado grande (separación de bloques)
48px  → Espaciado extra grande (secciones principales)
64px  → Espaciado de página (padding-bottom)
```

### Border-Radius
```
4px  → Botones, inputs
8px  → Cards, contenedores
12px → Mensajes destacados
```

---

## ⚡ Animaciones y Transiciones

### Timing Function
```css
cubic-bezier(0.4, 0, 0.2, 1)  /* Material Design standard easing */
```

### Duración
```css
0.2s → Transiciones rápidas (hover, focus)
0.3s → Transiciones estándar (cards, modales)
0.6s → Animaciones de entrada (fade-in)
```

### Efectos Comunes
- **Hover**: translateY(-2px) + shadow increase
- **Active**: translateY(0) + shadow decrease
- **Focus**: Border color change + glow effect

---

## 🖼️ Iconografía

### Logo/Favicon
- **Archivo**: `static/favicon.svg`
- **Diseño**: Cerebro estilizado con nodos de red neuronal
- **Colores**: Gradiente azul (#1a73e8 → #1765cc)
- **Tamaño**: 100x100px (SVG escalable)

### Font Awesome
- Se mantienen íconos mínimos y funcionales
- Tamaño estándar: 20px en icon-box
- Color: var(--primary) o heredado

---

## 📱 Responsividad

### Breakpoints Bootstrap
```
sm: 576px   → Móviles grandes
md: 768px   → Tablets
lg: 992px   → Laptops
xl: 1200px  → Desktops
```

### Consideraciones
- Navbar colapsable en móvil
- Padding reducido en pantallas pequeñas
- Grid de 12 columnas (Bootstrap)
- Max-width container: 1200px

---

## ✅ Checklist de Implementación

Cuando agregues nuevas páginas o componentes:

- [ ] Usar variables CSS (--primary, --text-primary, etc.)
- [ ] Aplicar Google Sans para títulos, Roboto para cuerpo
- [ ] Usar border-radius: 8px para cards, 4px para botones
- [ ] Implementar Material Design shadows
- [ ] Añadir transiciones con cubic-bezier(0.4, 0, 0.2, 1)
- [ ] Mantener espaciado consistente (múltiplos de 8px)
- [ ] Incluir favicon en <head>
- [ ] Probar hover states y focus states
- [ ] Validar contraste de colores (WCAG AA)
- [ ] Verificar responsividad en móvil

---

## 📚 Referencias

- [Google Material Design](https://material.io/design)
- [Google Cloud Design](https://cloud.google.com)
- [Material Design Color System](https://material.io/design/color)
- [Material Design Typography](https://material.io/design/typography)
- [Material Design Elevation](https://material.io/design/environment/elevation.html)

---

## 🔄 Historial de Versiones

### v2.0 (Actual) - Octubre 2025
- ✅ Sistema completo de Google Cloud / Material Design
- ✅ Paleta de colores actualizada (#1a73e8 primary)
- ✅ Tipografía Google Sans + Roboto
- ✅ Material Design elevation shadows
- ✅ Favicon SVG personalizado
- ✅ Navbar con logo y active indicators
- ✅ Botones y componentes refinados
- ✅ Espaciado y padding mejorados

### v1.0 - Diseño Inicial
- Sistema básico con Inter + Source Serif
- Paleta muted personalizada
- Iconografía abundante
- Gradientes decorativos

---

**Diseñado y implementado siguiendo las guías de Google Cloud**  
Para preguntas o sugerencias, consulta este documento.
