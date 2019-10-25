import tkinter as tk
import serial

Arduino_Serial = serial.Serial('/dev/ttyACM0',9600) 

class sony:
    def __init__(self, master):
        self.master = master
        self.quitb = tk.Button(master, 
                       text="QUIT", 
                       fg="red",
                       font=('Helvetica', 36, 'bold'),
                       command=master.quit)
        self.quitb.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

        self.power = tk.Button(master,
                          text="Power",
                          font=('Helvetica', 36, 'bold'),
                          command=self.power)
        self.power.pack(side=tk.TOP, expand=True, fill=tk.BOTH)  

        self.vol_Up = tk.Button(master,
                           text="Volume+",
                           font=('Helvetica', 36, 'bold'),
                           command=self.volUp)
        self.vol_Up.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.vol_Down = tk.Button(master,
                           text="Volume-",
                           font=('Helvetica', 36, 'bold'),
                           command=self.volDown)
        self.vol_Down.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.channel_up = tk.Button(master,
                           text="Channel+",
                           font=('Helvetica', 36, 'bold'),
                           command=self.channelUp)
        self.channel_up.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.channel_down = tk.Button(master,
                           text="Channel-",
                           font=('Helvetica', 36, 'bold'),
                           command=self.channelDown)
        self.channel_down.pack(side=tk.TOP, expand=True, fill=tk.BOTH)


    
    def power(self):
        Arduino_Serial.write('0'.encode())             #send 1 to arduino

    def volUp(self):
        Arduino_Serial.write('1'.encode())
    def volDown(self):
        Arduino_Serial.write('2'.encode())
    def channelUp(self):
        Arduino_Serial.write('3'.encode())
    def channelDown(self):
        Arduino_Serial.write('4'.encode())
    

