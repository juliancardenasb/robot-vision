from pathlib import Path

import cv2
from ultralytics import YOLO

MODEL_PATH = Path(__file__).parent / "yolov8n.pt"
WINDOW_NAME = "Deteccion de objetos — presiona Q para salir"


def cargar_modelo() -> YOLO:
    return YOLO(str(MODEL_PATH))


def abrir_camara(indice: int = 0) -> cv2.VideoCapture:
    cap = cv2.VideoCapture(indice)
    if not cap.isOpened():
        raise RuntimeError(f"No se pudo abrir la cámara (índice {indice})")
    return cap


def procesar_frame(frame, modelo: YOLO):
    resultados = modelo(frame, verbose=False)
    return resultados[0].plot()


def main():
    print("Cargando modelo...")
    modelo = cargar_modelo()
    print("Modelo cargado. Iniciando cámara...")

    cap = abrir_camara()

    print(f"Corriendo. Presioná Q en la ventana para salir.")

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
