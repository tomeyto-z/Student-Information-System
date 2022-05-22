from tkinter import *
from pathlib import Path
from database import delete as d

class DeleteStudent(Frame):
    #constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    # delete student init method
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.configure(bg="purple")
        Label(self, text="This is the delete student page").pack()
        self.msg = Label(self)
        self.msg.pack(pady=20)
        self.entry = Entry(self, width=50)
        self.entry.pack(pady=20)
        Button(self, text="Delete", command=self.delete_student).pack()

    # delete student
    def delete_student(self):
        if d.delete(self.entry.get()):
            self.msg.configure(text="Deleted Successfully!")
        else:
            self.msg.configure(text="Studet not found")
        self.entry.delete(0, END)

    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)