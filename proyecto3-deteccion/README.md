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
