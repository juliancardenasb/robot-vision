from pathlib import Path

import cv2
from flask import Flask, Response, render_template_string
from ultralytics import YOLO

MODEL_PATH = Path(__file__).parent / "yolov8n.pt"
HOST = "127.0.0.1"
PORT = 5000

app = Flask(__name__)
modelo = YOLO(str(MODEL_PATH))


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


def generar_frames():
    cap = abrir_camara()
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            resultados = modelo(frame, verbose=False)
            anotado = resultados[0].plot()

            ok, buffer = cv2.imencode(".jpg", anotado, [cv2.IMWRITE_JPEG_QUALITY, 80])
            if not ok:
                continue

            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n"
            )
    finally:
        cap.release()


PAGINA = """
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>Detección de objetos</title>
    <style>
        body { background: #111; color: #eee; font-family: sans-serif; text-align: center; margin: 0; padding: 20px; }
        h1 { font-weight: 300; }
        img { max-width: 100%; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
    </style>
</head>
<body>
    <h1>Detección de objetos en tiempo real — YOLOv8</h1>
    <img src="/video" alt="stream">
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(PAGINA)


@app.route("/video")
def video():
    return Response(generar_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    print(f"Abrí http://{HOST}:{PORT} en tu navegador")
    app.run(host=HOST, port=PORT, threaded=True)
