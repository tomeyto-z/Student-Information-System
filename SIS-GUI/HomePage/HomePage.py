from tkinter import *
from pathlib import Path

# Frame for the HomePgae
class HomePage(Frame):
    # constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    # HomePage class init method
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        # creating the whole canvas of the frame
        canvas = Canvas(self, bg="#093545", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x = 0, y = 0)

        # creating the bottom image for design
        self.curvy = PhotoImage(file=self.relative_to_assets("curvy.png"))
        canvas.create_image(640.0, 664.0, image=self.curvy)

        # creating canvas label text
        canvas.create_text(314.0, 243.0, anchor="nw", text="Student Information System",
                        fill="#FFFFFF", font=("LexendDeca ExtraLight", 50 * -1))

        # creating button for faculty
        self.imgFaculty = PhotoImage(file=self.relative_to_assets("btnFaculty.png"))
        btnFaculty = Button(self, image=self.imgFaculty, borderwidth=0, highlightthickness=0, 
                        command=lambda: controller.show_frame("SignInPage"), relief="flat")
        btnFaculty.place(x=491.0, y=432.0, width=300.0, height=45.0)

        # creating button for student
        self.imgStudent = PhotoImage(file=self.relative_to_assets("btnStudent.png"))
        btnStudent = Button(self, image=self.imgStudent, borderwidth=0, highlightthickness=0,
                        command=lambda: controller.show_frame("SignInPage"), relief="flat")
        btnStudent.place(x=491.0, y=355.0, width=300.0, height=45.0)

    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)