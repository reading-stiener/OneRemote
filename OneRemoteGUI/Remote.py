
class Remote():

    name = "Remote"
    widgets = []
    beacon = 1

    def __init__(self, name, widgets, beacon):
        self.name = name
        self.widgets = widgets
        self.beacon = beacon