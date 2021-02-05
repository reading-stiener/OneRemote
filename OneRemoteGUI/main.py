import tkinter as tk
from frames import *
import time

class ORApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("200x500")
        self.tk_setPalette(background='black', foreground='white',
                           activeBackground='black', activeForeground='gray')
        self.resizable(0, 0)
        self._frame = None
        self.switch_frame(Options)
        self.currentStatus = ""
        self.lastTime = time.time()

    def switch_frame(self, new_frame, remoteName=None):
        """Destroys current frame and replaces it with a new one."""
        if remoteName is not None:
            new_frame = new_frame(master=self, name=remoteName)
        else:
            new_frame = new_frame(master=self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def remCom(self, code):
        print("outputting ", code)


app = ORApp()
app.mainloop()