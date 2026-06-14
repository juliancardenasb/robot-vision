# Proyecto 3 — Detección de objetos en tiempo real

Detección de objetos usando YOLOv8 sobre la cámara de la laptop. Detecta 80 clases
(personas, sillas, botellas, autos, etc.) en tiempo real sin GPU.

## Cómo correr

```bash
# Desde la raíz del repositorio, con el venv activado:
cd proyecto3-deteccion
python detect.py
```

El modelo `yolov8n.pt` se descarga automáticamente la primera vez (~6 MB).

## Versiones disponibles

| Script | Display | Cuándo usarlo |
|--------|---------|---------------|
| `detect.py` | matplotlib | Wayland (default en GNOME moderno) — más lento (~10 fps) pero estable |
| `detect_imshow.py` | cv2.imshow + Qt | X11 / Xorg — fluido (~30 fps) pero requiere libs de xcb |
| `detect_web.py` | navegador (Flask + MJPEG) | Funciona en cualquier sistema, accesible desde el navegador |

Para usar `detect_imshow.py` en Wayland, instalá las libs de xcb:
```bash
sudo apt install libxcb-cursor0 libxcb-xinerama0 libxcb-icccm4 \
                 libxcb-image0 libxcb-keysyms1 libxcb-randr0 \
                 libxcb-render-util0 libxcb-shape0 libxkbcommon-x11-0
```

## Controles

| Tecla | Acción |
|-------|--------|
| `Q` | Salir |

## Estructura

```
proyecto3-deteccion/
├── detect.py       ← script principal
├── yolov8n.pt      ← modelo (se descarga automático, no se sube a git)
└── assets/         ← capturas y demos
```

## Aprendizajes

- YOLOv8n (nano) corre en tiempo real en CPU sin problema para demos
- OpenCV lee la cámara como arrays numpy en formato BGR, no RGB
- `results[0].plot()` devuelve el frame ya anotado con bounding boxes y etiquetas
