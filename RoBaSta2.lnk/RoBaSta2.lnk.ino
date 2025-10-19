/*  Servopositionen einstellen 
 *  von Andreas Wolter 
 *  fuer AZ-Delivery.de 
 *   
 *  Version: 1.0 
 *   
 *  Funktion: 
 *  Mit einem Potentiometer die Achsen der Servos einstellen. 
 *  Dabei die Positionswerte aus dem seriellen Monitor ablesen. 
 *  Mit einem Taster durch die Servos schalten. 
 *   
 *  Verwendete Hardware: 
 *    - Arduino Nano V3 
 *    - SG90 Mikroservos (4x) 
 *    - PCA9685 16 Kanal 12 Bit PWM Servotreiber 
 *    - Taster 
 *    - Potentiometer (hier 10KOhm) 
 *    - externe Spannungsversorgung 5V 
 *   
 *  Verwendete Bibliotheken: 
 *    - wire 
 *    - Adafruit PWM Servo Driver Library 
 *   
 *  Beispielquelle aus der Adafruit PWM Servo Driver Library: servo 
 *   
 ***************************************************  
  This is an example for our Adafruit 16-channel PWM & Servo driver 
  Servo test - this will drive 8 servos, one after the other on the 
  first 8 pins of the PCA9685 
 
  Pick one up today in the adafruit shop! 
  ------> http://www.adafruit.com/products/815 
   
  These drivers use I2C to communicate, 2 pins are required to   
  interface. 
 
  Adafruit invests time and resources providing this open source code,  
  please support Adafruit and open-source hardware by purchasing  
  products from Adafruit! 
 
  Written by Limor Fried/Ladyada for Adafruit Industries.   
  BSD license, all text above must be included in any redistribution 
 **************************************************** 
 *   
 *  Pinout: 
 *   
 *  Arduino Nano  |   Servo Treiber   |   Externe Spannungsquelle       
 *  ------------------------------------------------------------- 
 *      GND       |         GND       | 
 *      5V        |         VCC       | 
 *      A4        |         SDA       | 
 *      A5        |         SCL       | 
 *                |     Connector V+  |      +5V 
 *                |     Connector GND |      GND 
 *   
 *  Arduino Nano  |   Input 
 *  ------------------------------------------------------------- 
 *      D8        |   Taster Pin 1 
 *      A0        |   Potentiometer Mitte (Schleifer Pin) 
 *      5V        |   Potentiometer Außen 1 
 *      GND       |   Potentiometer Außen 2 
 *      GND       |   Taster Pin 2 
 */ 
 
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
  if (((steps % 10) < 1) && (delay_time >3)){
    delay_time -= 1;
  }
  delay(delay_time);                              // waits 15ms for the servo to reach the position
  }
  delay(50);   
}

void loop() { 
  //Servo positionieren 
  int start_pos = 190;
  int end_pos = 220;

  for (int i=3; i <= 7; i++){
    input = digitalRead(i);
    if (input == LOW) {
      Treffer_Array[7-i] = 11;
    }
    else{
      Treffer_Array[7-i] = 10;
    }
  }
 


  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    signal_received = true;
  }
  Serial.flush();
  
  if (signal_received) {
    for (int tt=0; tt <= 5; tt++){
      if (incomingByte==tt) {
        vorwarts_langsam(tt, Start_Array[tt], End_Array[tt]);
        delay(250);
        pwm.setPWM(tt, 0, Start_Array[tt]);
      }
    }
    
//  if (signal_received) {
//    if (incomingByte==9){
//       for (int j=0; j <= 2; j++){
//        vorwarts_langsam(j, Start_Array[j], End_Array[j]);
//        delay(250);
//        pwm.setPWM(j, 0, Start_Array[j]);
//      }
//    }
//    else{
//      for (int j=0; j <= 2; j++){
//        if (incomingByte==j) {
//          vorwarts_langsam(j, Start_Array[j], End_Array[j]);
//          delay(250);
//          pwm.setPWM(j, 0, Start_Array[j]);
//        }
//      }
//    }
    signal_received = false;
  }
  
 if (memcmp(Treffer_Array, Treffer_Array_alt, sizeof(Treffer_Array)) != 0) {
    Serial.write((uint8_t*)Treffer_Array, sizeof(Treffer_Array) );
    memcpy(Treffer_Array_alt, Treffer_Array, sizeof(Treffer_Array));
  }
}
