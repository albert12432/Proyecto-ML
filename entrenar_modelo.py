# -*- coding: utf-8 -*-
# entrenar_modelo.py - Entrena el modelo LSTM para reconocer señas
# Este script recorre las carpetas de secuencias por clase, entrena una red
# LSTM y guarda el modelo y etiquetas

import os
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from utils import Config, create_directories, augment_sequence


# Carga todas las secuencias de datos y etiquetas desde la carpeta
# data/secuencias/
def cargar_datos(augment=False):
    X, y = [], []
    etiquetas = sorted(os.listdir(Config.SEQUENCES_DIR))
    omitidas = 0

    for idx, clase in enumerate(etiquetas):
        carpeta_clase = os.path.join(Config.SEQUENCES_DIR, clase)
        for archivo in os.listdir(carpeta_clase):
            if archivo.endswith('.npy'):
                ruta = os.path.join(carpeta_clase, archivo)
                try:
                    secuencia = np.load(ruta)
                    # Valida que la secuencia tenga la forma correcta
                    if secuencia.shape != (
                        Config.FRAMES_PER_SEQUENCE,
                        Config.FEATURES
                    ):
                        print(f"⚠️  Omitida (forma incorrecta): {ruta}")
                        omitidas += 1
                        continue
                    X.append(secuencia)
                    y.append(idx)

                    if augment:
                        # Genera 2 variantes aumentadas por cada secuencia
                        for _ in range(2):
                            augmented = augment_sequence(secuencia)
                            if augmented.shape == (
                                Config.FRAMES_PER_SEQUENCE,
                                Config.FEATURES
                            ):
                                X.append(augmented)
                                y.append(idx)
                except Exception as e:
                    print(f"⚠️  Error cargando {ruta}: {e}")
                    omitidas += 1
                    continue

    if omitidas > 0:
        print(f"\n⚠️  Se omitieron {omitidas} secuencias corruptas.")

    if len(X) == 0:
        print("❌ No se encontraron secuencias válidas.")
        return None, None, etiquetas

    return np.array(X), np.array(y), etiquetas


# Define y construye el modelo LSTM para secuencias de landmarks
def construir_modelo(input_shape, num_clases):
    modelo = Sequential()
    modelo.add(LSTM(128, return_sequences=True, input_shape=input_shape))
    modelo.add(BatchNormalization())
    modelo.add(Dropout(0.3))
    modelo.add(LSTM(64, return_sequences=True))
    modelo.add(BatchNormalization())
    modelo.add(Dropout(0.3))
    modelo.add(LSTM(32))
    modelo.add(BatchNormalization())
    modelo.add(Dense(64, activation='relu'))
    modelo.add(Dense(num_clases, activation='softmax'))
    modelo.compile(
        loss='sparse_categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )
    return modelo


def main():
    print("📥 Cargando y aumentando datos de entrenamiento...")
    X, y, etiquetas = cargar_datos(augment=True)
    print(f"🔤 Clases encontradas: {etiquetas}")
    print(f"📊 Total de muestras (con aumento): {len(X)}")

    # Divide los datos en entrenamiento y validación
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print("🧠 Construyendo modelo LSTM mejorado...")
    modelo = construir_modelo(
        (Config.FRAMES_PER_SEQUENCE, Config.FEATURES), len(etiquetas)
    )

    # Callbacks para detener el entrenamiento si no mejora o ajustar el
    # learning rate
    early_stop = EarlyStopping(
        monitor='val_loss', patience=15, restore_best_weights=True
    )
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=7)

    print("🚀 Entrenando modelo...")
    modelo.fit(X_train, y_train, epochs=150, validation_data=(X_val, y_val),
               callbacks=[early_stop, reduce_lr], batch_size=32)

    create_directories([Config.MODELS_DIR])

    # Guarda el modelo y las etiquetas
    modelo.save(Config.MODEL_PATH)
    with open(Config.LABELS_PATH, 'wb') as f:
        pickle.dump(etiquetas, f)

    print(f"✅ Modelo guardado en {Config.MODEL_PATH}")
    print(f"✅ Etiquetas guardadas en {Config.LABELS_PATH}")


if __name__ == "__main__":
    main()
