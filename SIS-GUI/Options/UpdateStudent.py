from tkinter import *
from pathlib import Path

class UpdateStudent(Frame):
    # constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    # update student init method
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.configure(bg="gray")
        Label(self, text="This is the update student page").pack()

    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)