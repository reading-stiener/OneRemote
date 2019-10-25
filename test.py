import serial# add Serial library for Serial communication
import tkinter as tk
from sonyRem import sony
from speakerRem import speaker

Arduino_Serial = serial.Serial('/dev/ttyACM0',9600)  #Create Serial port object called arduinoSerialData              
print ('Point to your desired device')
root =  tk.Tk()
LOOP_ACTIVE = True
while LOOP_ACTIVE:
    print (Arduino_Serial.readline().decode('utf-8').lower())
    if ('sony' in  Arduino_Serial.readline().decode('utf-8').lower()):
        sonyRem =  sony(root)
        root.after(5000, root.destroy) 
        root.mainloop()
    elif ('nec' in Arduino_Serial.readline().decode('utf-8').lower()):
        speakerRem = speaker(root)
        #root.after(5000, root.destroy)
        root.mainloop()



    