import tkinter as tk
from customWidgets import *

class Application(tk.Frame):

    width = 200

    def __init__(self, master=None):
        super().__init__(master, bg='black')
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.title = tk.Label(self, text="Roku")
        self.title.config(font=("Verdana", 18))
        self.title.place(x=self.width/2-(32), y=5)

        self.buttonL = RemoteButton(self, imgPath="./images/home.png")
        self.buttonL.place(x=5, y=5)

        self.buttonR = RemoteButton(self, imgPath="./images/power.png")
        self.buttonR.place(x=self.width-35, y=6)

        self.track = Trackpad(self, 190, 180)
        self.track.place(x=5, y=40)

        self.slider1 = Slider(self, 190, 120, labels=["MENU", "GUIDE", "INFO"])
        self.slider1.place(x=5, y=230)

        self.slider2 = Slider(self, 190, 120, labels=["DOWN", "VOL", "UP"])
        self.slider2.place(x=5, y=360)


root = tk.Tk()
root.geometry("200x500")
root.tk_setPalette(background='black', foreground='white',
               activeBackground='black', activeForeground='gray')
root.resizable(0, 0)
app = Application(master=root)
app.pack_propagate(0)
app.pack(fill=tk.BOTH, expand=1)
app.mainloop()