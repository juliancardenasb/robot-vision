// Seguidor de línea — versión básica (lógica binaria)
//
// Sensores IR: leen el piso. En línea negra → valor BAJO. En blanco → valor ALTO.
// Umbral típico: 500 (mitad del rango 0-1023 del ADC).

const int SENSOR_IZQ = A0;
const int SENSOR_DER = A1;

const int MOTOR_IZQ_A = 5;
const int MOTOR_IZQ_B = 6;
const int MOTOR_DER_A = 9;
const int MOTOR_DER_B = 10;

const int UMBRAL = 500;
const int VELOCIDAD = 180;  // 0-255

void setup() {
    Serial.begin(9600);

    pinMode(MOTOR_IZQ_A, OUTPUT);
    pinMode(MOTOR_IZQ_B, OUTPUT);
    pinMode(MOTOR_DER_A, OUTPUT);
    pinMode(MOTOR_DER_B, OUTPUT);
}

void motor_izq(int velocidad) {
    if (velocidad >= 0) {
        analogWrite(MOTOR_IZQ_A, velocidad);
        analogWrite(MOTOR_IZQ_B, 0);
    } else {
        analogWrite(MOTOR_IZQ_A, 0);
        analogWrite(MOTOR_IZQ_B, -velocidad);
    }
}

void motor_der(int velocidad) {
    if (velocidad >= 0) {
        analogWrite(MOTOR_DER_A, velocidad);
        analogWrite(MOTOR_DER_B, 0);
    } else {
        analogWrite(MOTOR_DER_A, 0);
        analogWrite(MOTOR_DER_B, -velocidad);
    }
}

void loop() {
    int izq = analogRead(SENSOR_IZQ);
    int der = analogRead(SENSOR_DER);

    bool izq_en_linea = izq < UMBRAL;
    bool der_en_linea = der < UMBRAL;

    Serial.print("IZQ: "); Serial.print(izq);
    Serial.print(" | DER: "); Serial.println(der);

    if (izq_en_linea && der_en_linea) {
        // ambos sobre la línea → avanzar derecho
        motor_izq(VELOCIDAD);
        motor_der(VELOCIDAD);
    } else if (izq_en_linea && !der_en_linea) {
        // solo el izquierdo ve la línea → girar a la izquierda
        motor_izq(0);
        motor_der(VELOCIDAD);
    } else if (!izq_en_linea && der_en_linea) {
        // solo el derecho ve la línea → girar a la derecha
        motor_izq(VELOCIDAD);
        motor_der(0);
    } else {
        // ninguno ve la línea → detenerse (o buscar)
        motor_izq(0);
        motor_der(0);
    }

    delay(20);
}
