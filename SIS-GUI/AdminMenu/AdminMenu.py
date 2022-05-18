from tkinter import *
from pathlib import Path

# Frame for admin menu page
class AdminMenu(Frame):
    # constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    # admin menu class init method
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # creating the whole canvas of the frame
        canvas = Canvas(self, bg = "#093545", height = 720, width = 1280, bd = 0, highlightthickness = 0, relief = "ridge")
        canvas.place(x = 0, y = 0)

        # creating the bottom image for design
        self.curvy = PhotoImage(file=self.relative_to_assets("curvy.png"))
        canvas.create_image(640.0, 664.0, image=self.curvy)

        # creating panel menu
        canvas.create_rectangle(0.0, 0.0, 293.0, 720.0, fill="#214D5E", outline="")

        # creating delete students button
        self.imgDelete = PhotoImage(file=self.relative_to_assets("btnDelete.png"))
        btnDelete = Button(self, image=self.imgDelete, borderwidth=0, highlightthickness=0,
                    command=None, relief="flat")
        btnDelete.place(x=41.0, y=439.0, width=212.0, height=46.0)

        # creating update students button
        self.imgUpdate = PhotoImage(file=self.relative_to_assets("btnUpdate.png"))
        btnUpdate = Button(self, image=self.imgUpdate, borderwidth=0, highlightthickness=0,
                    command=None, relief="flat")
        btnUpdate.place(x=41.0, y=375.0, width=212.0, height=46.0)

        # creating search students button
        self.imgSearch = PhotoImage(file=self.relative_to_assets("btnSearch.png"))
        btnSearch = Button(self, image=self.imgSearch, borderwidth=0, highlightthickness=0,
                    command=None, relief="flat")
        btnSearch.place(x=41.0, y=311.0, width=212.0, height=46.0)

        # creating view students button
        self.imgView = PhotoImage(file=self.relative_to_assets("btnView.png"))
        btnView = Button(self, image=self.imgView, borderwidth=0, highlightthickness=0,
                    command=None, relief="flat")
        btnView.place(x=41.0, y=247.0, width=212.0, height=46.0)

        # creating add students button
        self.imgAdd = PhotoImage(file=self.relative_to_assets("btnAdd.png"))
        btnAdd = Button(self, image=self.imgAdd, borderwidth=0, highlightthickness=0,
                    command=None, relief="flat")
        btnAdd.place(x=41.0, y=182.0, width=212.0, height=46.0)

        # creating menu label
        canvas.create_text(116.0, 139.0, anchor="nw", text="MENU", 
                        fill="#FFFFFF", font=("LexendDeca Regular", 20 * -1))

        # creating quit button
        self.imgQuit = PhotoImage(file=self.relative_to_assets("btnQuit.png"))
        btnQuit = Button(self, image=self.imgQuit, borderwidth=0, highlightthickness=0,
                    command=lambda: controller.show_frame("HomePage"), relief="flat")
        btnQuit.place(x=41.0, y=665.0, width=90.0, height=27.0)

        # creating SIS label
        canvas.create_text(355.0, 35.0, anchor="nw", text="Student Management System", 
                        fill="#FFFFFF", font=("LexendDeca Regular", 36 * -1))

        # creating students image bottom right
        self.imgStudents = PhotoImage(file=self.relative_to_assets("imgStudents.png"))
        canvas.create_image(1085.0, 509.0, image=self.imgStudents)

    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
