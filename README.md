# Lengua de Señas con MediaPipe

Guía corta para capturar, entrenar y predecir señas usando MediaPipe Holistic y un modelo LSTM.

## Requisitos rápidos
- Python 3.11 (recomendado)
- Webcam activa
- Entorno virtual con las dependencias de `requirements.txt`

### Instalación básica
```powershell
python -m venv .venv
.\.venv\Scripts\pip install --upgrade pip
.\.venv\Scripts\pip install -r requirements.txt
```

## Flujo de trabajo
1. **Capturar datos** – `python capturar_secuencias.py`
	- Ingresá el nombre de la seña.
	- Presioná `C` para capturar o `Q` para salir.
2. **Entrenar modelo** – `python entrenar_modelo.py`
	- Genera `models/modelo_lstm.h5` y `models/etiquetas.pkl`.
3. **Predecir en vivo** – `python predecir_secuencias.py`
	- Mantén la seña un instante; si la confianza es baja se reporta como desconocida.

## Consejos de uso
- Capturá varias secuencias limpias por clase para reducir ambigüedades (ej. `a` vs `e`).
- Reentrená el modelo cada vez que incorpores nuevas muestras.
- En predicción, `Q` cierra todas las ventanas.

## Autores
- Harold Samuel Moreno Ramírez – samipe28@gmail.com
- Diego Martínez Benites

Proyecto con licencia MIT.