# Robot Vision — IA + Robótica + Electrónica

Proyecto personal para aprender robótica, electrónica e inteligencia artificial
combinando Arduino con modelos de visión por computadora.

## Proyectos

| Proyecto | Estado | Tecnologías |
|----------|--------|-------------|
| [Detección de objetos](./proyecto3-deteccion/) | 🔧 en progreso | Python, YOLOv8, OpenCV |
| [Seguidor de línea](./proyecto2-seguidor/) | ⏳ pendiente | Arduino, Wokwi |

## Requisitos

- Python 3.10 o 3.11
- Arduino IDE 2.x (para proyecto 2)

## Instalación

```bash
git clone https://github.com/tu-usuario/robot-vision.git
cd robot-vision

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Estructura

```
robot-vision/
├── proyecto3-deteccion/   ← detección de objetos con YOLOv8
└── proyecto2-seguidor/    ← robot seguidor de línea con Arduino
```
