from tkinter import *
from HomePage import HomePage as hp
from PageOne import PageOne as po

class MainFrame(Tk):
    # init method of the class MainFrame
    def __init__(self, *args, **kwargs):
        # init method of the tk class
        Tk.__init__(self, *args, **kwargs)
        self.geometry("1280x720")
        self.resizable(0, 0)

        # creating a container for all
        container = Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # creating a dictionary
        self.frames = {}

        # looping in every page/class and creating an object of it
        # then storing the class name as the key 
        # and the object of it as the value 
        for f in {hp.HomePage, po.PageOne}:
            page_name = f.__name__
            frame = f(container, self)
            frame.grid(row=0, column=0, sticky="NSEW")
            self.frames[page_name] = frame

        self.show_frame("PageOne")

    # showing the current frame above everything
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


window = MainFrame()
window.mainloop()