# 🤟 Documentación Educativa: Reconocimiento de Lengua de Señas

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Conceptos Fundamentales](#conceptos-fundamentales)
3. [Arquitectura General del Sistema](#arquitectura-general-del-sistema)
4. [Paso 1: Captura de Datos](#paso-1-captura-de-datos)
5. [Paso 2: Entrenamiento del Modelo](#paso-2-entrenamiento-del-modelo)
6. [Paso 3: Predicción en Tiempo Real](#paso-3-predicción-en-tiempo-real)
7. [Tecnologías Utilizadas](#tecnologías-utilizadas)

---

## Introducción

Este proyecto es un **sistema de reconocimiento de lengua de señas** en tiempo real. Combina dos tecnologías poderosas:

- **MediaPipe Holistic:** Detecta puntos de referencia en las manos, rostro y cuerpo.
- **Redes Neuronales LSTM:** Aprende patrones de movimiento y postura a partir de esos puntos.

El objetivo es que la computadora pueda "entender" y clasificar diferentes señas (letras, números, palabras) capturadas en video.

---

## Conceptos Fundamentales

### 1. ¿Qué es MediaPipe Holistic?

MediaPipe es una biblioteca de visión por computadora desarrollada por Google que puede detectar:

- **33 puntos de referencia en el rostro** (nariz, ojos, boca, etc.)
- **21 puntos en cada mano** (dedos, palma, articulaciones)
- **17 puntos en el cuerpo** (hombros, caderas, rodillas, etc.)

Estos puntos se representan con coordenadas (x, y, z) que indican posición en el espacio.

```
Ejemplo de un punto: (0.45, 0.32, -0.12)
- x: posición horizontal (0 a 1, siendo 0 izquierda y 1 derecha)
- y: posición vertical (0 a 1, siendo 0 arriba y 1 abajo)
- z: profundidad relativa a la cámara (valores negativos = más cerca)
```

### 2. ¿Qué son los Landmarks?

Un "landmark" es un punto detectado. En este proyecto:
- Recolectamos **147 valores** por frame (características):
  - 63 valores de la mano izquierda (21 puntos × 3 coordenadas)
  - 63 valores de la mano derecha (21 puntos × 3 coordenadas)
  - 6 valores de los hombros (2 puntos × 3 coordenadas)
  - 15 valores del rostro (5 puntos × 3 coordenadas)

### 3. ¿Qué es una Secuencia?

Una **secuencia** es una colección de frames consecutivos:
- **30 frames** por secuencia (aproximadamente 1 segundo a 30 FPS)
- Cada frame contiene 147 valores de landmarks
- Forma: **(30, 147)**

Esto permite que el modelo capture **tanto postura como movimiento**.

### 4. Normalización de Landmarks

Antes de usar los landmarks, los normalizamos para hacerlos **independientes de posición y tamaño**:

1. **Centrar:** Restamos el promedio de todos los puntos, centrando la seña en el origen.
2. **Escalar:** Dividimos por la distancia máxima, haciendo que todas las señas tengan un "tamaño" similar.

Esto permite que el modelo reconozca la seña aunque la persona esté más o menos cerca de la cámara.

---

## Arquitectura General del Sistema

```
┌─────────────────┐
│  1. CAPTURA     │
│  (Cámara Web)   │
└────────┬────────┘
         │ Video en vivo
         ▼
┌─────────────────────────────┐
│  2. DETECCIÓN MediaPipe     │
│  (33 puntos cara,           │
│   21 puntos por mano,       │
│   17 puntos cuerpo)         │
└────────┬────────────────────┘
         │ 147 valores (landmarks)
         ▼
┌─────────────────────────────┐
│  3. NORMALIZACIÓN           │
│  (Centrar, escalar)         │
└────────┬────────────────────┘
         │ Secuencia (30, 147)
         ▼
    ┌────────────────┐
    │  ¿Entrenando?  │
    └────┬────────┬──┘
         │        │
         SI      NO
         │        │
         ▼        ▼
    ┌────────┐  ┌────────────────────────┐
    │ GUARDAR│  │ 4. MODELO LSTM         │
    │ .npy   │  │ (Predicción)           │
    └────────┘  │ Clase predicha         │
               └────────────────────────┘
```

---

## Paso 1: Captura de Datos

### ¿Por qué necesitamos capturar datos?

Las redes neuronales aprenden **observando ejemplos**. Necesitamos múltiples grabaciones de cada seña para que el modelo aprenda sus características.

### ¿Cómo funciona la captura?

**Script:** `capturar_secuencias.py`

1. **Usuario ingresa el nombre de la seña** (ej: "hola")
2. **El programa abre la cámara** y muestra vista previa
3. **Usuario presiona 'C'** para comenzar a grabar
4. **Se capturan 30 frames** (1 segundo) de landmarks
5. **Se repite 30 veces** para la misma seña (30 secuencias)
6. **Se genera un GIF** mostrando la seña capturada

### Archivo de salida

Cada secuencia se guarda como:
```
data/secuencias/hola/hola_0.npy    (Secuencia 1)
data/secuencias/hola/hola_1.npy    (Secuencia 2)
...
data/secuencias/hola/hola_29.npy   (Secuencia 30)
```

Formato: Array NumPy con forma **(30, 147)**

### Código clave

```python
# En capturar_secuencias.py
for i in range(Config.SEQUENCES_PER_CLASS):  # 30 secuencias
    while len(secuencia) < Config.FRAMES_PER_SEQUENCE:  # 30 frames
        ret, frame = cap.read()
        results = holistic.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        landmarks = extract_holistic_landmarks(results)  # 147 valores
        landmarks = normalize_landmarks(landmarks)
        
        if validate_landmarks(landmarks):  # Validar que sean buenos
            secuencia.append(landmarks)
    
    np.save(f"data/secuencias/hola/hola_{i}.npy", secuencia)
```

---

## Paso 2: Entrenamiento del Modelo

### ¿Qué es el entrenamiento?

El entrenamiento es el proceso donde la red neuronal **aprende a reconocer patrones** a partir de los datos capturados.

**Script:** `entrenar_modelo.py`

### Fases del entrenamiento

#### 2.1 Carga de Datos

```python
def cargar_datos(augment=False):
    X, y = [], []
    # X: lista de secuencias (datos de entrada)
    # y: lista de etiquetas (qué seña es cada una)
    
    for clase in ['hola', 'adios', 'gracias']:
        for archivo in os.listdir(f'data/secuencias/{clase}'):
            secuencia = np.load(archivo)  # Forma: (30, 147)
            X.append(secuencia)
            y.append(indice_clase)
```

#### 2.2 Aumento de Datos

Para mejorar la precisión, generamos **variaciones de cada secuencia**:
- Rotación aleatoria (±5 grados)
- Ruido gaussiano (pequeñas perturbaciones)

Esto multiplica el dataset sin necesidad de grabar más.

```python
def augment_sequence(sequence):
    # Aplica rotación 3D
    angle = random.uniform(-5, 5)
    rotation_matrix = crear_matriz_rotacion(angle)
    
    # Aplica ruido
    noise = np.random.normal(0, 0.005, secuencia.shape)
    
    return secuencia_rotada + noise
```

**Resultado:** De 300 secuencias → 900 secuencias (triplicamos el dataset)

#### 2.3 División Train/Validation

```python
X_train, X_val, y_train, y_val = train_test_split(
    X, y,
    test_size=0.2,  # 80% entrenamiento, 20% validación
    random_state=42,
    stratify=y  # Mantener proporción de clases
)
```

#### 2.4 Modelo LSTM

**¿Qué es LSTM?**

LSTM = **Long Short-Term Memory** (Memoria a Largo y Corto Plazo)

Es una red neuronal recurrente especial que:
- Procesa **secuencias** de datos (perfecta para video)
- Recuerda información importante del pasado
- Olvida información irrelevante
- Realiza buenas predicciones basándose en patrones temporales

**Arquitectura del modelo:**

```
┌─────────────────────────────────────────┐
│ Entrada: Secuencia (30, 147)            │
└────────────────┬────────────────────────┘
                 │
                 ▼
        ┌────────────────────┐
        │ LSTM (128 neuronas)│ ← Lee la secuencia
        │ return_sequences   │   completa
        └────────┬───────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ BatchNormalization│ ← Normaliza salida
        └────────┬────────┘
                 │
                 ▼
        ┌────────────────────┐
        │ Dropout (30%)      │ ← Regularización
        └────────┬───────────┘
                 │
                 ▼
        ┌────────────────────┐
        │ LSTM (64 neuronas) │ ← Extrae características
        │ return_sequences   │
        └────────┬───────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ BatchNormalization│
        └────────┬────────┘
                 │
                 ▼
        ┌────────────────────┐
        │ Dropout (30%)      │
        └────────┬───────────┘
                 │
                 ▼
        ┌────────────────────┐
        │ LSTM (32 neuronas) │ ← Síntesis final
        └────────┬───────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ BatchNormalization│
        └────────┬────────┘
                 │
                 ▼
        ┌────────────────────────┐
        │ Dense (64, ReLU)       │ ← Procesamiento denso
        └────────┬───────────────┘
                 │
                 ▼
        ┌────────────────────────────┐
        │ Dense (N_clases, Softmax)  │ ← Probabilidades
        └────────┬───────────────────┘
                 │
                 ▼
        ┌──────────────────────────┐
        │ Salida: Predicción       │
        │ Ej: [0.02, 0.95, 0.03]  │
        │ Clase predicha: HOLA     │
        └──────────────────────────┘
```

**¿Por qué 3 capas LSTM?**
- **Capa 1 (128):** Aprende patrones básicos
- **Capa 2 (64):** Combina patrones en conceptos más complejos
- **Capa 3 (32):** Síntesis final para clasificación

#### 2.5 Compilación y Entrenamiento

```python
modelo.compile(
    loss='sparse_categorical_crossentropy',  # Función de pérdida
    optimizer='adam',                        # Optimizador
    metrics=['accuracy']                     # Métrica
)

modelo.fit(
    X_train, y_train,
    epochs=150,              # Máximo 150 iteraciones
    validation_data=(X_val, y_val),
    callbacks=[early_stop, reduce_lr],
    batch_size=32
)
```

**¿Qué es cada componente?**

- **Loss (Pérdida):** Mide qué tan mal predice el modelo. Objetivo: reducirlo.
- **Optimizer (Adam):** Algoritmo que ajusta los pesos del modelo para reducir la pérdida.
- **Accuracy:** Porcentaje de predicciones correctas.
- **Epochs:** Número de veces que el modelo ve todo el dataset.
- **Batch Size:** Cuántas secuencias procesa antes de actualizar pesos.

**Callbacks (Funciones especiales):**
- **EarlyStopping:** Detiene el entrenamiento si no mejora (evita sobreentrenamiento).
- **ReduceLROnPlateau:** Reduce la velocidad de aprendizaje si se estanca.

#### 2.6 Guardar Modelo

```python
modelo.save(Config.MODEL_PATH)  # Guarda en models/modelo_lstm.h5
pickle.dump(etiquetas, open(Config.LABELS_PATH, 'wb'))  # Guarda las clases
```

---

## Paso 3: Predicción en Tiempo Real

### ¿Cómo funciona la predicción?

**Script:** `predecir_secuencias.py`

Una vez que tenemos el modelo entrenado, lo usamos para **clasificar señas nuevas** en tiempo real.

### Flujo de Predicción

```
1. Capturar frame actual
         │
         ▼
2. Detectar landmarks (MediaPipe)
         │
         ▼
3. Normalizar landmarks
         │
         ▼
4. Agregar a buffer de 30 frames
         │
         ▼
5. Buffer lleno (30 frames) →
         │
         ▼
6. Pasar a modelo LSTM
         │
         ▼
7. Obtener predicción (vector de probabilidades)
         │
         ▼
8. Verificar confianza y consistencia
         │
         ├─ Confianza < 80% → Descartar
         │
         ├─ Brecha entre clases < 15% → Descartar (ambiguo)
         │
         └─ Todo bien → Mostrar resultado
```

### Código clave

```python
# Buffer para almacenar 30 frames consecutivos
buffer = deque(maxlen=30)

while True:
    ret, frame = cap.read()
    results = holistic.process(frame)
    landmarks = extract_holistic_landmarks(results)
    landmarks = normalize_landmarks(landmarks)
    
    if validate_landmarks(landmarks):
        buffer.append(landmarks)
    
    # Cuando tenemos 30 frames
    if len(buffer) == 30:
        secuencia = np.array(buffer).reshape(1, 30, 147)
        pred = model.predict(secuencia)[0]
        
        # Obtener top 2 predicciones
        idx_mejor = np.argmax(pred)
        confianza = pred[idx_mejor]
        idx_segundo = np.argmax(pred[pred < confianza])
        confianza_segundo = pred[idx_segundo]
        
        brecha = confianza - confianza_segundo
        
        # Verificar calidad de predicción
        if (confianza >= 0.80 and
            brecha >= 0.15 and
            predicciones_consistentes >= 3):
            
            clase_predicha = etiquetas[idx_mejor]
            print(f"🎯 {clase_predicha.upper()}")
            
            # Mostrar GIF de referencia
            mostrar_gif(clase_predicha)
        
        buffer.clear()
```

### Métricas de Confianza

Para evitar falsos positivos, verificamos:

1. **MIN_CONFIDENCE = 0.80** (80%)
   - El modelo debe estar al menos 80% seguro de su predicción

2. **MIN_CONFIDENCE_GAP = 0.15** (15%)
   - Diferencia entre la clase más probable y la segunda más probable
   - Evita confusiones entre clases similares (ej: A y E)

3. **CONSISTENT_PREDICTIONS = 3**
   - Debe repetir la misma predicción al menos 3 veces
   - Evita falsos positivos de un solo frame

**Ejemplo:**

```
Predicción: [0.05, 0.82, 0.13]
    ↓
Clase mejor: "HOLA" (82%)
Clase segundo: "A" (13%)
Brecha: 82% - 13% = 69% ✓ (> 15%)
Confianza: 82% ✓ (> 80%)
Consistencia: 3/3 veces ✓

✅ PREDICCIÓN VÁLIDA: HOLA
```

---

## Tecnologías Utilizadas

### 1. **MediaPipe**
- Detecta puntos de referencia en tiempo real
- Modelo preentrenado en millones de imágenes
- Precisión: ~95%

### 2. **TensorFlow/Keras**
- Framework para redes neuronales
- Proporciona capas LSTM, Dense, BatchNormalization
- Optimizadores (Adam)

### 3. **OpenCV (cv2)**
- Captura de video desde cámara web
- Manipulación de imágenes
- Visualización en tiempo real

### 4. **NumPy**
- Operaciones numéricas eficientes
- Manejo de arrays multidimensionales
- Transformaciones matemáticas (rotación, escala)

### 5. **Scikit-learn**
- División train/test
- Preprocesamiento de datos

### 6. **Pillow (PIL)**
- Generación de GIFs
- Procesamiento de imágenes

---

## Resumen de Flujo Completo

```
┌──────────────────────────────────────────────────────────┐
│                     INICIO                               │
└──────────────────────────────────────────────────────────┘
                         │
                         ▼
        ┌────────────────────────────────────┐
        │ 1. CAPTURAR DATOS                  │
        │    (capturar_secuencias.py)        │
        │    Crea: data/secuencias/*/        │
        │    Genera: gifs/*.gif              │
        └────────────────┬───────────────────┘
                         │
                         ▼
        ┌────────────────────────────────────┐
        │ 2. ENTRENAR MODELO                 │
        │    (entrenar_modelo.py)            │
        │    Lee: data/secuencias/*/         │
        │    Crea: models/modelo_lstm.h5     │
        │    Crea: models/etiquetas.pkl      │
        └────────────────┬───────────────────┘
                         │
                         ▼
        ┌────────────────────────────────────┐
        │ 3. PREDECIR EN TIEMPO REAL         │
        │    (predecir_secuencias.py)        │
        │    Lee: models/modelo_lstm.h5      │
        │    Lee: gifs/*.gif                 │
        │    Salida: Predicciones en pantalla│
        └────────────────┬───────────────────┘
                         │
                         ▼
        ┌──────────────────────────────────────┐
        │           RESULTADO FINAL            │
        │  Reconocimiento de Lengua de Señas  │
        └──────────────────────────────────────┘
```

---

## Mejoras y Extensiones Futuras

1. **Aumentar Dataset:** Capturar más secuencias por clase
2. **Agregar más clases:** Palabras complejas, frases completas
3. **Transfer Learning:** Usar modelos preentrenados
4. **Interfaz Gráfica:** Crear GUI amigable
5. **Exportar a Mobile:** Llevar el modelo a dispositivos móviles
6. **Reconocimiento de Contexto:** Secuencias de múltiples palabras

---

**Autores:** Harold Samuel Moreno Ramírez | Diego Martínez Benites

**Última actualización:** Noviembre 2025
