import tkinter as tk
import json
from customWidgets import *

class Remote(tk.Frame):

    width = 200

    def __init__(self, master=None, name=None):
        super().__init__(master, bg='black')
        self.master = master
        self.pack()
        self.create_remote(name)
        self.pack_propagate(0)
        self.pack(fill=tk.BOTH, expand=1)

    def create_remote(self, remote):

        with open('./remotes/%s.json' % remote) as j:
            remote = json.load(j)

        self.title = tk.Label(self, text=remote['name'])
        self.title.config(font=("Verdana", 18))
        self.title.place(x=self.width/2-(32), y=2)

        for i in remote['sliders']:
            self.slider = Slider(self, i['size'][0], i['size'][1], labels=i['labels'])
            self.slider.place(x=i['loc'][0], y=i['loc'][1])
        for i in remote['trackpads']:
            self.track = Trackpad(self, i['size'][0], i['size'][1])
            self.track.place(x=i['loc'][0], y=i['loc'][1])
        for i in remote['buttons']:
            self.button = RemoteButton(self, imgPath="./images/%s" % i['img'])
            self.button.place(x=i['loc'][0], y=i['loc'][1])


class Options(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Point or Pick").pack(side="top", fill="x", pady=20)
        tk.Button(self, text="Roku Remote",
                  command=lambda: master.switch_frame(Remote, 'Roku')).pack(pady=10)
        tk.Button(self, text="Lights Remote",
                  command=lambda: master.switch_frame(Remote, 'Lights')).pack(pady=10)