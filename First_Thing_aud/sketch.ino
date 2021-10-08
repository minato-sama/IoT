int state = -1;
int led_pin = 13;
int led_delay = 300;

int sensor1_val = 0;
int sensor2_val = 0;

bool send_sensor1 = false;
bool send_sensor2 = false;

void setup() {
    Serial.begin(9600);
    pinMode(led_pin, OUTPUT);
}

void loop() {
    while (Serial.available()>0) {
        int a = Serial.read();
        if (a == 'd')
            state = 0;
        else if (a == 'u')
            state = 1;
        else if (a == 'b')
            state = 2;
        else if (a == '1')
            send_sensor1 = true;
        else if (a == '2')
            send_sensor2 = true;
        else
            state = -1;
    }
    if (state == 0 or state == 1)
            digitalWrite(led_pin, state);
        else if (state == 2) {
            digitalWrite(led_pin, (millis()/led_delay) %2);
        if (send_sensor1) {
            sensor1_val = analogRead(A0);
            Serial.println(sensor1_val);
            send_sensor1 = false;
        if (send_sensor2) {
            sensor2_val = analogRead(A2);
            Serial.println(sensor2_val);
            send_sensor2 = false;
        }
      }
    }
}
