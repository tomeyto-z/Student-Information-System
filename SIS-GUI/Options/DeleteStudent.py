from tkinter import *
from pathlib import Path

class DeleteStudent(Frame):
    #constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    # delete student init method
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.configure(bg="purple")
        Label(self, text="This is the delete student page").pack()

    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)