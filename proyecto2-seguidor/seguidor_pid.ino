// Seguidor de línea — versión con control PID
//
// En vez de lógica on/off, calcula un error continuo entre ambos sensores
// y corrige proporcionalmente la velocidad de cada motor.

const int SENSOR_IZQ = A0;
const int SENSOR_DER = A1;

const int LED_MOTOR_IZQ = 5;
const int LED_MOTOR_DER = 6;

// Velocidad base (cuando va perfectamente centrado)
const int VELOCIDAD_BASE = 150;
const int VELOCIDAD_MAX = 255;

// Constantes PID — ajustar empíricamente
const float Kp = 0.15;
const float Ki = 0.0;
const float Kd = 0.05;

float error_previo = 0;
float integral = 0;
unsigned long tiempo_previo = 0;

int saturar(int valor, int minimo, int maximo) {
    if (valor < minimo) return minimo;
    if (valor > maximo) return maximo;
    return valor;
}

void setup() {
    Serial.begin(9600);
    pinMode(LED_MOTOR_IZQ, OUTPUT);
    pinMode(LED_MOTOR_DER, OUTPUT);
    tiempo_previo = millis();
}

void loop() {
    int izq = analogRead(SENSOR_IZQ);
    int der = analogRead(SENSOR_DER);

    // El error: positivo si la línea está a la izquierda, negativo si a la derecha
    float error = izq - der;

    // Tiempo transcurrido en segundos
    unsigned long ahora = millis();
    float dt = (ahora - tiempo_previo) / 1000.0;
    tiempo_previo = ahora;

    // Términos PID
    float P = Kp * error;
    integral += error * dt;
    float I = Ki * integral;
    float D = (dt > 0) ? Kd * (error - error_previo) / dt : 0;

    float correccion = P + I + D;
    error_previo = error;

    // Aplicar a los motores
    int vel_izq = saturar(VELOCIDAD_BASE - correccion, 0, VELOCIDAD_MAX);
    int vel_der = saturar(VELOCIDAD_BASE + correccion, 0, VELOCIDAD_MAX);

    analogWrite(LED_MOTOR_IZQ, vel_izq);
    analogWrite(LED_MOTOR_DER, vel_der);

    Serial.print("Err: "); Serial.print(error);
    Serial.print(" | Corr: "); Serial.print(correccion);
    Serial.print(" | IZQ: "); Serial.print(vel_izq);
    Serial.print(" | DER: "); Serial.println(vel_der);

    delay(20);
}
