from pathlib import Path

import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO

MODEL_PATH = Path(__file__).parent / "yolov8n.pt"


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

    print("Corriendo. Cerrá la ventana de matplotlib para salir.")

    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.axis("off")
    img_plot = None

    try:
        while plt.fignum_exists(fig.number):
            ret, frame = cap.read()
            if not ret:
                break

            frame_anotado = procesar_frame(frame, modelo)
            frame_rgb = cv2.cvtColor(frame_anotado, cv2.COLOR_BGR2RGB)

            if img_plot is None:
                img_plot = ax.imshow(frame_rgb)
            else:
                img_plot.set_data(frame_rgb)

            plt.pause(0.001)
    except KeyboardInterrupt:
        print("Interrumpido por usuario.")
    finally:
        cap.release()
        plt.close("all")
        print("Cerrado correctamente.")


if __name__ == "__main__":
    main()
