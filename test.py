import serial# add Serial library for Serial communication
import tkinter as tk
#import tkFont
#helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD) 
def power():
    Arduino_Serial.write('0'.encode())             #send 1 to arduino
  
def volUp():
    Arduino_Serial.write('1'.encode())
def volDown():
    Arduino_Serial.write('2'.encode())
def channelUp():
    Arduino_Serial.write('3'.encode())
def channelDown():
    Arduino_Serial.write('4'.encode()) 

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   font=('Helvetica', 36, 'bold'),
                   command=quit)
button.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

power = tk.Button(frame,
                  text="Power",
                  font=('Helvetica', 36, 'bold'),
                  command=power)
power.pack(side=tk.TOP, expand=True, fill=tk.BOTH)  

vol_Up = tk.Button(frame,
                   text="Volume+",
                   font=('Helvetica', 36, 'bold'),
                   command=volUp)
vol_Up.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

vol_Down = tk.Button(frame,
                   text="Volume-",
                   font=('Helvetica', 36, 'bold'),
                   command=volDown)
vol_Down.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

channel_up = tk.Button(frame,
                   text="Channel+",
                   font=('Helvetica', 36, 'bold'),
                   command=channelUp)
channel_up.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

channel_down = tk.Button(frame,
                   text="Channel-",
                   font=('Helvetica', 36, 'bold'),
                   command=channelDown)
channel_down.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

Arduino_Serial = serial.Serial('/dev/ttyACM0',9600)  #Create Serial port object called arduinoSerialData
#print (Arduino_Serial.readline())               #read the serial data and print it as line
print ('Point to your desired device')

while True:
    #infinite loop
    #a  = input() 
    print (type(Arduino_Serial.readline()))
    print (Arduino_Serial.readline())
    #print ('sony' in Arduino_Serial.readline().decode('utf-8').lower())
    
    if ('sony' in  Arduino_Serial.readline().decode('utf-8').lower()):
        #print('enter 1 or 0') 
        #input_data = input()                  #waits until user enters data
        #print ('you entered', input_data)          #prints the data for confirmation
        root.mainloop()
        #if (input_data == '1'):                   #if the entered data is 1 
            #Arduino_Serial.write('1'.encode())             #send 1 to arduino
            #print ('LED ON')
            #pass 
               
            
        #elif (input_data == '0'):                   #if the entered data is 0
        #    Arduino_Serial.write('0'.encode())             #send 0 to arduino 
        #    print ('LED OFF')