import tkinter as tk
import serial
import time

Arduino_Serial = serial.Serial('/dev/ttyACM0',9600)

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Options)
        self.currentStatus = ""
        self.lastTime = time.time()

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
    
    def sense(self, msg):
        print(msg)
        if ('nothing' not in msg):
            if 'sony' in msg:
                if self.currentStatus != 'sony':
                    print('sony')
                    self.currentStatus = 'sony'
                    self.lastTime = time.time()
                    self.switch_frame(SonyTV)
                else:
                    self.lastTime = time.time()
            elif 'nec' in msg:
                if self.currentStatus != 'nec':
                    print('nec') 
                    self.currentStatus = 'nec'
                    self.lastTime = time.time()
                    self.switch_frame(Speaker)
                else:
                    self.lastTime = time.time()
            msg = Arduino_Serial.readline().decode('utf-8').lower()
            print(msg)
            self.after(200, lambda: self.sense(msg))
        else:
            if time.time() - self.lastTime >= 10 and self.currentStatus != "":
                self.currentStatus = ""
                self.switch_frame(Options)
            msg = Arduino_Serial.readline().decode('utf-8').lower()
            print(msg)
            self.after(200, lambda: self.sense(msg))
    
    def remCom(self, code):
        Arduino_Serial.write(code.encode())

class Options(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Point at your desired device or choose your remote").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Sony Remote",
                  command=lambda: master.switch_frame(SonyTV)).pack()
        tk.Button(self, text="Speaker Remote",
                  command=lambda: master.switch_frame(Speaker)).pack()

class SonyTV(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="SONY remote").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to options",
                  command=lambda: master.switch_frame(Options)).pack()
        self.quitb = tk.Button(self, 
                       text="QUIT", 
                       fg="red",
                       font=('Helvetica', 36, 'bold'),
                       command=master.quit)
        self.quitb.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

        self.power = tk.Button(self,
                          text="Power",
                          font=('Helvetica', 36, 'bold'),
                          command=lambda: master.remCom('0'))
        self.power.pack(side=tk.TOP, expand=True, fill=tk.BOTH)  

        
        self.vol_Up = tk.Button(self,
                           text="Volume+",
                           font=('Helvetica', 36, 'bold'),
                           command=lambda: master.remCom('1'))
        self.vol_Up.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.vol_Down = tk.Button(self,
                           text="Volume-",
                           font=('Helvetica', 36, 'bold'),
                           command=lambda: master.remCom('2'))
        self.vol_Down.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.channel_up = tk.Button(self,
                           text="Channel+",
                           font=('Helvetica', 36, 'bold'),
                           command=lambda: master.remCom('3'))
        self.channel_up.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.channel_down = tk.Button(self,
                           text="Channel-",
                           font=('Helvetica', 36, 'bold'),
                           command=lambda: master.remCom('4'))
        self.channel_down.pack(side=tk.TOP, expand=True, fill=tk.BOTH)        
    
  
          
class Speaker(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Speaker remote").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to options",
                  command=lambda: master.switch_frame(Options)).pack()
        self.button = tk.Button(self, 
                           text="QUIT", 
                           fg="red",
                           font=('Helvetica', 36, 'bold'),
                           command=master.quit)
        self.button.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

        self.power = tk.Button(self,
                           text="Power",
                           font=('Helvetica', 36, 'bold'),
                           command=lambda: master.remCom('5'))
        
        self.power.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.volUp = tk.Button(self,
                           text="Volume+",
                           font=('Helvetica', 36, 'bold'),
                           command=lambda: master.remCom('6'))
        self.volUp.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.volDown = tk.Button(self,
                           text="Volume-",
                           font=('Helvetica', 36, 'bold'),
                           command=master.remCom('7'))
        self.volDown.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        
        
   
    
        
if __name__ == "__main__":
    app = SampleApp()
    msg = Arduino_Serial.readline().decode('utf-8').lower()
    print(msg) 
    app.sense(msg)
    app.mainloop()
