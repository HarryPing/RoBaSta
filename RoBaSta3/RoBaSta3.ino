#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

#define SERVOMIN   68   // 0 bis 4096 - try and error
#define SERVOMAX   510  // 0 bis 4096 - try and error
#define SERVO_FREQ 50   // Analog servos run at ~50 Hz updates   
#define TOLERANZ   10   // Prozent vom Endanschlag 

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

// States       
int state = 0;

// Input 
bool input = HIGH; 
bool input_alt = HIGH;  
int input_analog = 0;

uint8_t Treffer_Array[6] = {10,10,10,10,10,255};
uint8_t Treffer_Array_alt[6] = {10,10,10,10,10,255};
uint8_t incomingByte = 0;

int Start_Array[5] = {200,200,200,200,200};
int End_Array[5] = {300,300,300,310,300};

bool signal_received = false;

// Servos 
// Berechne Min und Max mit Servotoleranz am Aussenanschlag 
const int MAXSERVOS = 5; 
int range = SERVOMAX - SERVOMIN; 
double temp = (range / 100) * (double)TOLERANZ; 
int NEWMIN = SERVOMIN + (int)temp; 
int NEWMAX = SERVOMAX - (int)temp; 
int i = 0; 
int SERVO_MIDDLE[MAXSERVOS] = {190,190,190,190,190}; 

void setup() { 
  Serial.begin(9600);
  pinMode(7, INPUT_PULLUP);
  pinMode(6, INPUT_PULLUP);
  pinMode(5, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);

  pwm.begin(); 
  pwm.setOscillatorFrequency(27000000);   // The int.osc. is closer to 27MHz   
  pwm.setPWMFreq(SERVO_FREQ);             // Analog servos run at ~50 Hz updates 
  delay(500);
}

void vorwarts_langsam(int state, int start_pos, int end_pos)
{
  int pos = start_pos;
  int delay_time = 5;
  int steps = 0;
  for (pos; pos <= end_pos; pos += 1) {    // goes from 180 degrees to 0 degrees
    pwm.setPWM(state, 0, pos);              // tell servo to go to position in variable 'pos'
    steps += 1;
    if (((steps % 10) < 1) && (delay_time > 3)){
      delay_time -= 1;
    }
    delay(delay_time);                              // waits 15ms for the servo to reach the position
  }
  delay(50);   
}

bool isUSBConnected() {
  // Prüfen, ob eine serielle Verbindung besteht. 
  return Serial.available() > 0;
}

bool areAllSwitchesClosed() {
  // Prüfen, ob alle Kippschalter (Pins 3-7) geschlossen sind (d.h. LOW).
  return (digitalRead(3) == LOW) && (digitalRead(4) == LOW) && (digitalRead(5) == LOW) && (digitalRead(6) == LOW) && (digitalRead(7) == LOW);
}

void resetTargets() {
  // Alle Targets zurücksetzen (setzt alle Servo-Positionen auf die Startwerte)
  for (int tt = 0; tt <= 4; tt++) {
    pwm.setPWM(tt, 0, Start_Array[tt]);
  }
}

void loop() { 
  // Servo positionieren 
  int start_pos = 190;
  int end_pos = 220;

  for (int i = 3; i <= 7; i++) {
    input = digitalRead(i);
    if (input == LOW) {
      Treffer_Array[7 - i] = 11;
    } else {
      Treffer_Array[7 - i] = 10;
    }
  }

  // Überprüfen, ob eine serielle Verbindung besteht
  if (isUSBConnected()) {
    if (Serial.available() > 0) {
      // lesen des eingehenden Bytes:
      incomingByte = Serial.read();
      signal_received = true;
    }
  }

  Serial.flush();
  
  // Reset Target
  if (signal_received) {
    for (int tt = 0; tt <= 5; tt++) {
      if (incomingByte == tt) {
        vorwarts_langsam(tt, Start_Array[tt], End_Array[tt]);
        delay(250);
        pwm.setPWM(tt, 0, Start_Array[tt]);
      }
    }
    signal_received = false;
  }

  // Überprüfen, ob alle Kippschalter geschlossen sind und keine USB-Verbindung besteht
  if (!isUSBConnected() && areAllSwitchesClosed()) {
    resetTargets(); // Targets zurücksetzen
    delay(500);     // Kurze Verzögerung, um das mehrfache Auslösen zu vermeiden
  }
  
  if (memcmp(Treffer_Array, Treffer_Array_alt, sizeof(Treffer_Array)) != 0) {
    Serial.write((uint8_t*)Treffer_Array, sizeof(Treffer_Array));
    memcpy(Treffer_Array_alt, Treffer_Array, sizeof(Treffer_Array));
  }
}
