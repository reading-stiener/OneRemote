#include <IRremote.h>
const int RECV_PIN = 4;
IRrecv irrecv(RECV_PIN);
decode_results results;
IRsend irsend;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  irrecv.enableIRIn();
  irrecv.blink13(true);

}
void rSignal(){ 
  unsigned long starttime = millis();
  unsigned long endtime = starttime;
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
    irrecv.resume();
    Serial.println(results.value);
    }   
  //loopcount = loopcount+1;
  endtime = millis();
  }
  //serial.print (loopcount,DEC);
}
void loop(){
  // sending beacon signal
  for (int i = 0; i < 3; i++){
    irsend.sendNEC(0x9B286897, 32);
    delay(40);   
  }   
  
  //delay(1000); 
  irrecv.enableIRIn();
  irrecv.resume();
  rSignal(); 
}
