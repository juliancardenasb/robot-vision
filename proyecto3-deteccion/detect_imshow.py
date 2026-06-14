import os
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "xcb")

import cv2
from ultralytics import YOLO

MODEL_PATH = Path(__file__).parent / "yolov8n.pt"
WINDOW_NAME = "Deteccion de objetos — presiona Q para salir"


def cargar_modelo() -> YOLO:
    return YOLO(str(MODEL_PATH))


def abrir_camara() -> cv2.VideoCapture:
    for indice in range(3):
        cap = cv2.VideoCapture(indice, cv2.CAP_V4L2)
        if not cap.isOpened():
            cap.release()
            continue

        for _ in range(30):
            cap.read()

        ret, frame = cap.read()
        if ret and frame is not None and frame.mean() > 1:
            print(f"Cámara encontrada en índice {indice}")
            return cap

        cap.release()

    raise RuntimeError("No se encontró ninguna cámara funcional")


def procesar_frame(frame, modelo: YOLO):
    resultados = modelo(frame, verbose=False)
    return resultados[0].plot()


def main():
    print("Cargando modelo...")
    modelo = cargar_modelo()
    print("Modelo cargado. Iniciando cámara...")

    cap = abrir_camara()

    print("Corriendo. Presioná Q en la ventana para salir.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("No se pudo leer el frame. Saliendo.")
            break

        frame_anotado = procesar_frame(frame, modelo)
        cv2.imshow(WINDOW_NAME, frame_anotado)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Cerrado correctamente.")


if __name__ == "__main__":
    main()
