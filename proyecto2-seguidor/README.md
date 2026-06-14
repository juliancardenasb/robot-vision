# Proyecto 2 — Seguidor de línea (Arduino + Wokwi)

Robot que sigue una línea negra sobre fondo blanco usando 2 sensores IR y 2 motores DC.
Se simula completo en [Wokwi](https://wokwi.com) — no hace falta hardware físico.

## Cómo correrlo

1. Crear cuenta en https://wokwi.com
2. **New Project → Arduino Uno**
3. Pegar el contenido de `seguidor_linea.ino` en el panel `sketch.ino`
4. Agregar los componentes (click derecho → Add Part):
   - 2 IR Line Tracking Sensors
   - 1 L298N Motor Driver
   - 2 DC Motors

## Conexiones

| Componente | Pin Arduino |
|------------|-------------|
| Sensor izquierdo (OUT) | A0 |
| Sensor derecho (OUT)   | A1 |
| L298N IN1 (motor izq)  | 5  |
| L298N IN2 (motor izq)  | 6  |
| L298N IN3 (motor der)  | 9  |
| L298N IN4 (motor der)  | 10 |
| VCC sensores y lógica  | 5V |
| GND                    | GND |

## Lógica

El robot lee los dos sensores IR. Sobre línea negra dan valor BAJO (<500),
sobre blanco dan valor ALTO. Según qué sensor ve la línea:

| Sensor IZQ | Sensor DER | Acción |
|------------|------------|--------|
| Negro | Negro | Avanzar derecho |
| Negro | Blanco | Girar izquierda |
| Blanco | Negro | Girar derecha |
| Blanco | Blanco | Detenerse |

## Próximas mejoras

- [ ] Versión con control PID (movimiento suave en lugar de on/off)
- [ ] Agregar tercer sensor central para más precisión
- [ ] Memoria de última dirección para recuperar línea perdida
