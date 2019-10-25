import tkinter as tk
import serial

Arduino_Serial = serial.Serial('/dev/ttyACM0',9600) 

class speaker:
    def __init__(self, master):
        self.master = master 
        self.button = tk.Button(master, 
                           text="QUIT", 
                           fg="red",
                           font=('Helvetica', 36, 'bold'),
                           command=master.quit)
        self.button.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

        self.power = tk.Button(master,
                           text="Power",
                           font=('Helvetica', 36, 'bold'),
                           command=self.power)
        self.power.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.volUp = tk.Button(master,
                           text="Volume+",
                           font=('Helvetica', 36, 'bold'),
                           command=self.volUp)
        self.volUp.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.volDown = tk.Button(master,
                           text="Volume-",
                           font=('Helvetica', 36, 'bold'),
                           command=self.volDown)
        self.volDown.pack(side=tk.TOP, expand=True, fill=tk.BOTH)


    def power(self):
        Arduino_Serial.write('5'.encode())

    def volUp(self):
        Arduino_Serial.write('6'.encode())

    def volDown(self):
        Arduino_Serial.write('7'.encode())
    


