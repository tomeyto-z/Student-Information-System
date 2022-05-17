import tkinter as tk
from pathlib import Path

# Frame for the HomePgae
class HomePage(tk.Frame):
    # constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = "#093545")
        
        # creating the whole canvas to take up the frame
        canvas = tk.Canvas(self, bg = "#093545", height = 720, width = 1280, bd = 0, highlightthickness = 0, relief = "ridge")
        canvas.place(x = 0, y = 0)

        # creating images for buttons
        image_image_1 = tk.PhotoImage(file=self.relative_to_assets("curvy.png"))
        canvas.create_image(640.0, 664.0, image=image_image_1)

        # creating canvas label text
        canvas.create_text(314.0, 243.0, anchor="nw", text="Student Information System",
                        fill="#FFFFFF", font=("LexendDeca ExtraLight", 50 * -1))

        # creating button for faculty
        imgFaculty = tk.PhotoImage(file=self.relative_to_assets("btnFaculty.png"))
        btnFaculty = tk.Button(self, image=imgFaculty, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"), relief="flat")
        btnFaculty.place(x=491.0, y=432.0, width=300.0, height=45.0)

        # creating button for student
        imgStudent = tk.PhotoImage(file=self.relative_to_assets("btnStudent.png"))
        btnStudent = tk.Button(self, image=imgStudent, borderwidth=0, highlightthickness=0,
                command=lambda: print("button_2 clicked"), relief="flat")
        btnStudent.place(x=491.0, y=355.0, width=300.0, height=45.0)

    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)