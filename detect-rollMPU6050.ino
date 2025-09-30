#include <Wire.h>
#include <MPU6050.h>
MPU6050 mpu;
void setup() {
  pinMode(amberLED,OUTPUT);
  pinMode(blueLED,OUTPUT);
  pinMode(greenLED,OUTPUT);
  Serial.begin(9600);
  Serial.println("Initialize MPU6050");
  while(!mpu.begin(MPU6050_SCALE_2000DPS,MPU6050_RANGE_2G)){
    Serial.println("Could not find a valid MPU6050 sensor,check wiring!")
    delay(500);
  }
}
void loop() {
  Vector normAccel=mpu.readNormalizeAccel();
  float pitch=normalAccel.XAxis;
  float roll=normalAccel.YAxis;
  Serial.print("Pitch=");
  Serial.print(pitch);
  Serial.print("Roll=");
  Serial.print(roll);
  Serial.println();
  Serial.println("*********************************")
  if(pitch<0.00){
    Serial.println("Pitch front detected")
  }else if(pitch>0.90){
    Serial.println("Pitch back detected")
  }
  if(roll>0.60){
    Serial.println("Roll Right detected")
  }else if(roll<0.00){
    Serial.println("Roll Left detected")
  }
  if((pitch>0.00 && pitch<0.90) && (roll>0 && roll<0.60)){
    Serial.println("No pitch and No Roll");
  }
  delay(10);
}
