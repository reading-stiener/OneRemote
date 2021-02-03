import tkinter as tk
from datetime import datetime
from PIL import Image
from PIL import ImageTk

defaultPad = 10
defaultFont = "Verdana 10"
MIN_SWIPE_SPEED = 80
SWIPE_TIME = 0.2

class RemoteWidget(tk.Canvas):

    def __init__(self, parent, width, height, cornerradius=15, padding=0, color="#4B4B4B", command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0, relief="flat", highlightthickness=0)
        self.command = command

        if cornerradius > 0.5*width:
            print("Error: cornerradius is greater than width.")
            return None

        if cornerradius > 0.5*height:
            print("Error: cornerradius is greater than height.")
            return None

        rad = 2*cornerradius
        def shape():
            self.create_polygon((padding,height-cornerradius-padding,padding,cornerradius+padding,padding+cornerradius,padding,width-padding-cornerradius,padding,width-padding,cornerradius+padding,width-padding,height-cornerradius-padding,width-padding-cornerradius,height-padding,padding+cornerradius,height-padding), fill=color, outline=color)
            self.create_arc((padding,padding+rad,padding+rad,padding), start=90, extent=90, fill=color, outline=color)
            self.create_arc((width-padding-rad,padding,width-padding,padding+rad), start=0, extent=90, fill=color, outline=color)
            self.create_arc((width-padding,height-rad-padding,width-padding-rad,height-padding), start=270, extent=90, fill=color, outline=color)
            self.create_arc((padding,height-padding-rad,padding+rad,height-padding), start=180, extent=90, fill=color, outline=color)

        id = shape()
        (x0, y0, x1, y1) = self.bbox("all")
        width = (x1-x0)
        height = (y1-y0)
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()



class Trackpad(RemoteWidget):

    lastx = None
    lasty = None
    startTime = None

    def __init__(self, parent, width, height):
        RemoteWidget.__init__(self, parent, width, height)
        self.bind("<Motion>", self.motion)
        self.bind("<Button-1>", self.clicked)

    def resetGesture(self):
        self.startTime = None
        self.lastx = None
        self.lasty = None

    def motion(self, event):
        x, y = event.x, event.y

        if self.startTime is None:
            self.startTime = datetime.now()
        if self.lastx is not None:
            deltax = x-self.lastx
            deltay = y-self.lasty
            deltat = (self.startTime-datetime.now()).total_seconds()*-1
            if deltax > MIN_SWIPE_SPEED and deltat > SWIPE_TIME:
                print("Trackpad Swiped Right")
                self.resetGesture()
            elif deltax < MIN_SWIPE_SPEED*-1 and deltat > SWIPE_TIME:
                print("Trackpad Swiped Left")
                self.resetGesture()
            if deltay > MIN_SWIPE_SPEED and deltat > SWIPE_TIME:
                print("Trackpad Swiped Down")
                self.resetGesture()
            elif deltay < MIN_SWIPE_SPEED*-1 and deltat > SWIPE_TIME:
                print("Trackpad Swiped Up")
                self.resetGesture()
        else:
            self.lastx = x
            self.lasty = y

    def clicked(self, event):
        print("Trackpad Tapped")



class Slider(RemoteWidget):

    lastx = None
    startTime = None

    def __init__(self, parent, width, height, labels=None, images=None):
        RemoteWidget.__init__(self, parent, width, height)
        self.bind("<Motion>", self.motion)
        self.bind("<Button-1>", self.clicked)

        if images is not None:
            pass
        elif labels is not None:
            self.create_text(defaultPad*3, defaultPad, fill="white", font=defaultFont,
                             text=labels[0])
            self.create_text(width / 2, defaultPad, fill="white", font=defaultFont,
                             text=labels[1])
            self.create_text(width-defaultPad*3, defaultPad, fill="white", font=defaultFont,
                             text=labels[2])

    def resetGesture(self):
        self.startTime = None
        self.lastx = None

    def motion(self, event):
        x = event.x

        if self.startTime is None:
            self.startTime = datetime.now()
        if self.lastx is not None:
            deltax = x - self.lastx
            deltat = (self.startTime - datetime.now()).total_seconds() * -1
            if deltax > MIN_SWIPE_SPEED and deltat > SWIPE_TIME:
                print("Slider Swiped Right")
                self.resetGesture()
            elif deltax < MIN_SWIPE_SPEED * -1 and deltat > SWIPE_TIME:
                print("Slider Swiped Left")
                self.resetGesture()
        else:
            self.lastx = x

    def clicked(self, event):
        print("Slider Tapped")

class RemoteButton(tk.Button):

    def __init__(self, master, imgPath=None, label=None, command=None):
        tk.Button.__init__(self, master=master)
        self.command = command
        if imgPath is not None:
            img = Image.open(imgPath)
            img = ImageTk.PhotoImage(img.resize((25, 25), Image.ANTIALIAS))
            self.image = img
            self.config(image=img, borderwidth=0)
        elif label is not None:
            self.text = label
