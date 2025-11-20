# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np
from PIL import Image
from utils import (
    Config, create_directories, initialize_holistic,
    setup_camera, extract_holistic_landmarks, normalize_landmarks,
    validate_landmarks
)


# Dibuja los puntos y conexiones de manos, rostro y cuerpo en el frame con
# MediaPipe Holistic. Útil para que el usuario vea si sus gestos están
# siendo bien capturados.
def draw_holistic_landmarks(frame, results):
    import mediapipe as mp
    mp_drawing = mp.solutions.drawing_utils  # type: ignore
    if results.face_landmarks:
        mp_drawing.draw_landmarks(
            frame, results.face_landmarks,
            mp.solutions.holistic.FACEMESH_TESSELATION
        )
    if results.left_hand_landmarks:
        mp_drawing.draw_landmarks(
            frame, results.left_hand_landmarks,
            mp.solutions.hands.HAND_CONNECTIONS
        )
    if results.right_hand_landmarks:
        mp_drawing.draw_landmarks(
            frame, results.right_hand_landmarks,
            mp.solutions.hands.HAND_CONNECTIONS
        )
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            frame, results.pose_landmarks,
            mp.solutions.holistic.POSE_CONNECTIONS
        )


# Genera un archivo GIF animado desde una lista de frames (usado para mostrar
# la seña capturada)
def generar_gif(frames, ruta_salida):
    imagenes = [
        Image.fromarray(cv2.cvtColor(f, cv2.COLOR_BGR2RGB)).resize((300, 300))
        for f in frames
    ]
    imagenes[0].save(
        ruta_salida, save_all=True, append_images=imagenes[1:],
        duration=100, loop=0
    )


# Espera que el usuario presione 'c' para comenzar la captura
# Muestra mensaje en pantalla y dibuja los landmarks para que el usuario
# pueda posicionarse
def esperar_confirmacion_inicio(cap, holistic):
    print("\n🕒 Esperando que presiones 'C' para comenzar...")
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        frame = cv2.flip(frame, 1)
        results = holistic.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw_holistic_landmarks(frame, results)

        h, w = frame.shape[:2]
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, h - 40), (w, h), (0, 0, 0), -1)
        cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)
        texto = "POSICIONESE - 'C' PARA COMENZAR, 'Q' PARA SALIR"
        cv2.putText(frame, texto, (10, h - 12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.imshow("Captura Secuencia", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            return False
        elif key == ord('c') or key == ord('C'):
            return True


# Captura una secuencia de 30 frames (por Config), guarda los landmarks y los
# frames sin dibujos para el gif
def capturar_secuencia(holistic, cap, clase, secuencia_id):
    secuencia = []
    gif_frames = []

    # Cuenta regresiva antes de cada secuencia para dar tiempo al usuario
    for i in range(3, 0, -1):
        ret, frame = cap.read()
        if not ret:
            return None, None
        frame = cv2.flip(frame, 1)

        # Dibujar landmarks durante la cuenta regresiva para referencia
        results = holistic.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw_holistic_landmarks(frame, results)

        cv2.putText(frame, f"Comenzando en {i}...",
                    (int(frame.shape[1]/2)-150, int(frame.shape[0]/2)),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
        texto_sec = f"Sec. {secuencia_id + 1}/{Config.SEQUENCES_PER_CLASS}"
        cv2.putText(frame, texto_sec,
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        cv2.imshow("Captura Secuencia", frame)
        if cv2.waitKey(1000) & 0xFF == ord('q'):
            return None, None

    while len(secuencia) < Config.FRAMES_PER_SEQUENCE:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        results = holistic.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Copiamos el frame sin dibujos para guardar el gif limpio
        frame_limpio = frame.copy()

        draw_holistic_landmarks(frame, results)

        landmarks = extract_holistic_landmarks(results)
        landmarks = normalize_landmarks(landmarks)

        if validate_landmarks(landmarks):
            secuencia.append(landmarks)
            gif_frames.append(frame_limpio)  # sin landmarks dibujados

        # Visualización del progreso
        texto_cap = (f"Capturando '{clase.upper()}' - "
                     f"{len(secuencia)}/{Config.FRAMES_PER_SEQUENCE}")
        cv2.putText(frame, texto_cap, (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        texto_sec = f"Sec. {secuencia_id + 1}/{Config.SEQUENCES_PER_CLASS}"
        cv2.putText(frame, texto_sec, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

        cv2.imshow("Captura Secuencia", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return None, None

    return np.array(secuencia), gif_frames


# Función principal del script de captura
def main():
    print("\n🟢 CAPTURA DE SECUENCIAS - HOLISTIC UNIFICADO")
    clase_input = input(
        "▶ Ingresá letra, número o frase (sin espacios): "
    ).lower().strip()

    # Elimina caracteres no válidos para nombres de archivo/carpeta
    clase = ''.join(
        c for c in clase_input if c.isalnum() or c in (' ', '_')
    ).replace(' ', '_')

    if not clase:
        print("❌ Nombre de clase no válido. Usa solo letras y números.")
        return

    carpeta_clase = os.path.join(Config.SEQUENCES_DIR, clase)
    create_directories([Config.SEQUENCES_DIR, Config.GIFS_DIR, carpeta_clase])

    # Inicialización de cámara y Holistic
    cap = setup_camera(width=1280, height=720)
    holistic = initialize_holistic()

    # Eliminamos secuencias anteriores si existen (sobreescribe clase)
    existentes = [f for f in os.listdir(carpeta_clase) if f.endswith('.npy')]
    for f in existentes:
        os.remove(os.path.join(carpeta_clase, f))
    print(f"🗑️ Borradas {len(existentes)} secuencias para '{clase}'")

    print(f"\n🎯 Clase: '{clase}'")
    print(f"🆕 Capturando {Config.SEQUENCES_PER_CLASS} nuevas secuencias...")

    # Esperamos la confirmación del usuario antes de iniciar todas las capturas
    if not esperar_confirmacion_inicio(cap, holistic):
        print("❌ Captura cancelada por el usuario.")
        cap.release()
        cv2.destroyAllWindows()
        holistic.close()
        return

    # Capturamos múltiples secuencias (cada una de 30 frames)
    for i in range(Config.SEQUENCES_PER_CLASS):
        print(f"\n⏳ Capturando sec. {i+1}/{Config.SEQUENCES_PER_CLASS}...")

        secuencia, frames = capturar_secuencia(holistic, cap, clase, i)

        if secuencia is None:
            print("❌ Captura interrumpida.")
            break

        # Guardamos la secuencia como archivo .npy
        ruta_npy = os.path.join(carpeta_clase, f"{clase}_{i}.npy")
        np.save(ruta_npy, secuencia)
        print(f"✅ Secuencia guardada: {ruta_npy}")

        # Solo se genera un gif (de la primera muestra)
        if i == 0:
            ruta_gif = os.path.join(Config.GIFS_DIR, f"{clase}.gif")
            generar_gif(frames, ruta_gif)
            print(f"🎞️ GIF generado: {ruta_gif}")

    cap.release()
    cv2.destroyAllWindows()
    holistic.close()
    print("\n📦 Captura finalizada.")


# Punto de entrada principal del script
if __name__ == "__main__":
    main()
