from tkinter import *
from pathlib import Path

class AddStudent(Frame):
    # constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    # add student init method
    def __init__(self, parent):
        Frame.__init__(self, parent)

        # creating this frame canvas
        canvas = Canvas(self, bg = "#093545", height = 720, width = 987, bd = 0, highlightthickness = 0, relief = "ridge")
        canvas.place(x = 0, y = 0)
        
        # creating add student label
        canvas.create_text(62.0, 35.0, anchor="nw", text="Add student", fill="#FFFFFF", font=("LexendDeca Light", 36 * -1))

        # creating student number label
        canvas.create_text(23.0, 171.0, anchor="nw", text="Student Number",
                        fill="#FFFFFF", font=("LexendDeca Light", 14 * -1))

        # creating student number entry
        self.imgStuNum = PhotoImage(file=self.relative_to_assets("entry_StuNum.png"))
        canvas.create_image(172.0, 215.5, image=self.imgStuNum)
        entry_StuNum = Entry(self, bd=0, bg="#224957", highlightthickness=0)
        entry_StuNum.place(x=32.0, y=193.0, width=280.0, height=43.0)

        # creating last name label
        canvas.create_text(23.0, 285.0, anchor="nw", text="Last name", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating last name entry
        self.imgLastN = PhotoImage(file=self.relative_to_assets("entry_LastN.png"))
        canvas.create_image(172.0, 327.5, image=self.imgLastN)
        entry_LastN = Entry(self, bd=0, bg="#224957", highlightthickness=0)
        entry_LastN.place(x=32.0, y=305.0, width=280.0, height=43.0)

        # creating first name label
        canvas.create_text(342.0, 285.0, anchor="nw", text="First name",
                        fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating first name entry
        self.imgFirstN = PhotoImage(file=self.relative_to_assets("entry_FirstN.png"))
        canvas.create_image(492.0, 327.5, image=self.imgFirstN)
        entry_FirstN = Entry(self, bd=0, bg="#224957", highlightthickness=0)
        entry_FirstN.place(x=352.0, y=305.0, width=280.0, height=43.0)

        # creating middle name label
        canvas.create_text(661.0, 285.0, anchor="nw", text="Middle name", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating middle name entry
        self.imgMiddleN = PhotoImage(file=self.relative_to_assets("entry_MiddleN.png"))
        canvas.create_image(811.0, 327.5, image=self.imgMiddleN)
        entry_MiddleN = Entry(self, bd=0, bg="#224957", highlightthickness=0)
        entry_MiddleN.place(x=671.0, y=305.0, width=280.0, height=43.0)

        # creating email address label
        canvas.create_text(23.0, 397.0, anchor="nw", text="Email Address", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating last name entry
        self.imgEmail = PhotoImage(file=self.relative_to_assets("entry_Email.png"))
        canvas.create_image(172.0, 439.5, image=self.imgEmail)
        entry_Email = Entry(self, bd=0, bg="#224957", highlightthickness=0)
        entry_Email.place(x=32.0, y=417.0, width=280.0, height=43.0)

        # creating contact number label
        canvas.create_text(23.0, 509.0, anchor="nw", text="Contact Number", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating contact number entry
        self.imgContNum = PhotoImage(file=self.relative_to_assets("entry_ContNum.png"))
        canvas.create_image(172.0, 551.5, image=self.imgContNum)
        entry_ContNum = Entry(self, bd=0, bg="#224957", highlightthickness=0)
        entry_ContNum.place(x=32.0, y=529.0, width=280.0, height=43.0)

    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)