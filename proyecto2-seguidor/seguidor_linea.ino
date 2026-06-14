// Seguidor de línea — versión Wokwi (motores simulados con LEDs)
//
// Sensores IR simulados con potenciómetros (A0, A1).
// Motores simulados con LEDs en pines PWM (5, 6).
// Brillo del LED = velocidad del motor correspondiente.

const int SENSOR_IZQ = A0;
const int SENSOR_DER = A1;

const int LED_MOTOR_IZQ = 5;
const int LED_MOTOR_DER = 6;

const int UMBRAL = 500;
const int VELOCIDAD = 180;  // 0-255

void setup() {
    Serial.begin(9600);
    pinMode(LED_MOTOR_IZQ, OUTPUT);
    pinMode(LED_MOTOR_DER, OUTPUT);
}

void motores(int vel_izq, int vel_der) {
    analogWrite(LED_MOTOR_IZQ, vel_izq);
    analogWrite(LED_MOTOR_DER, vel_der);
}

void loop() {
    int izq = analogRead(SENSOR_IZQ);
    int der = analogRead(SENSOR_DER);

    bool izq_en_linea = izq < UMBRAL;
    bool der_en_linea = der < UMBRAL;

    Serial.print("IZQ: "); Serial.print(izq);
    Serial.print(" | DER: "); Serial.print(der);
    Serial.print(" | Accion: ");

    if (izq_en_linea && der_en_linea) {
        Serial.println("AVANZAR");
        motores(VELOCIDAD, VELOCIDAD);
    } else if (izq_en_linea && !der_en_linea) {
        Serial.println("GIRAR IZQUIERDA");
        motores(0, VELOCIDAD);
    } else if (!izq_en_linea && der_en_linea) {
        Serial.println("GIRAR DERECHA");
        motores(VELOCIDAD, 0);
    } else {
        Serial.println("DETENER");
        motores(0, 0);
    }

    delay(50);
}
