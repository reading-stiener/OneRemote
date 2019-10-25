#include <IRremote.h>
const int RECV_PIN = 11;
IRrecv irrecv(RECV_PIN);
decode_results results;
IRsend irsend;
int value=0;
const int led=13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  irrecv.enableIRIn();
  irrecv.blink13(true);
  pinMode(led, OUTPUT);
  digitalWrite (led, LOW);
  Serial.println("Connection established...");

}

boolean rSignal(){ 
  unsigned long starttime = millis();
  unsigned long endtime = starttime;
  boolean signal = false; 
  while ((endtime - starttime)<=1000){
    if (irrecv.decode(&results)){
        if (results.decode_type == NEC) {
          Serial.print("NEC: ");
        } 
        else if (results.decode_type == SONY) {
          Serial.print("SONY: ");
        } 
        else if (results.decode_type == RC5) {
          Serial.print("RC5: ");
        } 
        else if (results.decode_type == RC6) {
          Serial.print("RC6: ");
        } 
        else if (results.decode_type == UNKNOWN) {
          Serial.print("UNKNOWN: ");
        }
        Serial.println("detected!");
        signal = true; 
        irrecv.resume();
        Serial.println(results.value);   
   }
   endtime = millis();
  }
  return signal;
}

void loop(){
  // sending beacon signal 
  // should only do this if it receives input from remote 
   while (Serial.available())
      {
         value = Serial.read();
      }
   //power sony
   if (value == 48){ 
      //digitalWrite (led, HIGH);
      for (int i = 0; i < 3; i++){ 
        irsend.sendSony(0xa90, 12); 
        delay(40); 
      }
     
   }
   //volume up sony
   else if (value == 49){ 
      for (int i = 0; i < 3; i++){ 
        irsend.sendSony(0x490, 12); 
        delay(40); 
      }
   }
   // volume down sony 
   else if (value == 50){ 
      for (int i = 0; i < 3; i++){ 
        irsend.sendSony(0xC90, 12); 
        delay(40); 
      }
   }
   // channel up sony
   else if (value == 51){ 
      for (int i = 0; i < 3; i++){ 
        irsend.sendSony(0x90, 12); 
        delay(40); 
      }
   } 
   // channel down sony  
   else if (value == 52){ 
      for (int i = 0; i < 3; i++){ 
        irsend.sendSony(0x890, 12); 
        delay(40); 
      }
   }
   // speaker power 
   else if (value == 53){ 
     for (int i = 0; i < 3; i++){
      irsend.sendNEC(0x9B28B649, 32);
      delay;
     } 
   }
   // speaker vol up 
   else if (value == 54){ 
     for (int i = 0; i < 3; i++){
      irsend.sendNEC(0x9B28F20D, 32);
      delay;
     } 
   }  
   // speaker vol down 
   else if (value == 55){ 
     for (int i = 0; i < 3; i++){
      irsend.sendNEC(0x9B280AF5, 32);
      delay;
     } 
   }  
   // speaker next 
   else if (value == 56){ 
     for (int i = 0; i < 3; i++){
      irsend.sendNEC(0x9B28A857, 32);
      delay;
     } 
   }
   // speaker prev 
   else if (value == 57){ 
     for (int i = 0; i < 3; i++){
      irsend.sendNEC(0x9B286897, 32);
      delay;
     } 
   }   
   
  value = 0; 
  //delay(1000); 
  irrecv.enableIRIn();
  irrecv.resume();
  boolean signal_received =  rSignal(); 
  Serial.println(signal_received);   
  
}  
