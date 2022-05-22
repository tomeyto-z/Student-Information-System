from tkinter import *
from pathlib import Path

class ViewStudent(Frame):
    # constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    # view student init method
    def __init__(self, parent):
        Frame.__init__(self, parent)

        # creating this frame canvas
        canvas = Canvas(self, bg = "green", height = 720, width = 987, bd = 0, highlightthickness = 0, relief = "ridge")
        canvas.place(x = 0, y = 0)

        Label(self, text="This is the view student page").pack()

    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)