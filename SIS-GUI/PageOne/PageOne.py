from tkinter import *

# Frame for PageOne
class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text="Page One", font=("Helvetica", 20)).pack()
        Button(self, text="To Home Page", command=lambda: controller.show_frame("HomePage"),
                font=("Helvetica", 20)).place(x=100, y=100)