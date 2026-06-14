# Proyecto 2 — Seguidor de línea (Arduino + Wokwi)

Robot que sigue una línea negra sobre fondo blanco usando 2 sensores IR y 2 motores DC.
Se simula completo en [Wokwi](https://wokwi.com) — no hace falta hardware físico.

## Cómo correrlo en Wokwi

Wokwi no incluye motores DC ni el L298N, así que los sustituimos:
- **Sensores IR** → potenciómetros (girar = simular ver negro/blanco)
- **Motores** → LEDs (el brillo PWM = velocidad del motor)

1. Crear cuenta en https://wokwi.com
2. **New Project → Arduino Uno**
3. Pegar el contenido de `seguidor_linea.ino` en el panel `sketch.ino`
4. Agregar componentes (Add Part):
   - 2 × Potentiometer
   - 2 × LED
   - 2 × Resistor (220Ω)

## Conexiones

| Componente | Pin Arduino |
|------------|-------------|
| Potenciómetro izquierdo (SIG) | A0 |
| Potenciómetro derecho (SIG)   | A1 |
| LED izquierdo (ánodo + resistor) | 5 |
| LED derecho (ánodo + resistor)   | 6 |
| Extremos de pots y cátodos LEDs | 5V / GND |

## Lógica

El robot lee los dos sensores IR. Sobre línea negra dan valor BAJO (<500),
sobre blanco dan valor ALTO. Según qué sensor ve la línea:

| Sensor IZQ | Sensor DER | Acción |
|------------|------------|--------|
| Negro | Negro | Avanzar derecho |
| Negro | Blanco | Girar izquierda |
| Blanco | Negro | Girar derecha |
| Blanco | Blanco | Detenerse |

## Versiones

| Archivo | Estrategia |
|---------|-----------|
| `seguidor_linea.ino` | Lógica binaria on/off — fácil de entender |
| `seguidor_pid.ino` | Control PID — movimiento suave y proporcional |

## Próximas mejoras

- [ ] Tuning fino del PID (Kp, Ki, Kd)
- [ ] Agregar tercer sensor central para más precisión
- [ ] Memoria de última dirección para recuperar línea perdida
