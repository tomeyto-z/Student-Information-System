from tkinter import *
from pathlib import Path

# Frame for Sign up page
class SignUpPage(Frame):
    # constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    # SignUpPage init method
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # creating the whole canvas of the frame
        canvas = Canvas(self, bg = "#093545", height = 720, width = 1280, bd = 0, highlightthickness = 0, relief = "ridge")
        canvas.place(x = 0, y = 0)

        # creating the bottom image for design
        self.curvy = PhotoImage(file=self.relative_to_assets("curvy.png"))
        canvas.create_image(640.0, 664.0, image=self.curvy)

        # creating sign up label
        canvas.create_text(530.0, 93.0, anchor="nw", text="Sign up", 
                        fill="#FFFFFF", font=("LexendDeca Regular", 64 * -1))

        # creating starting label
        canvas.create_text(485.0, 185.0, anchor="nw", text="Sign up to start managing student information", 
                        fill="#FFFFFF", font=("LexendDeca Regular", 16 * -1))

        # creating email label
        canvas.create_text(491.0, 240.0, anchor="nw", text="Email", 
                        fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))
                    
        # creating email entry
        self.imgEntry1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        canvas.create_image(641.0, 282.5, image=self.imgEntry1)
        entry1 = Entry(self, bd=0, bg="#224957", highlightthickness=0)
        entry1.place(x=501.0, y=260.0, width=280.0, height=43.0)

        # creating password label
        canvas.create_text(491.0, 317.0, anchor="nw", text="Password", 
                        fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating password entry
        self.imgEntry2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        canvas.create_image(641.0, 359.5, image=self.imgEntry2)
        entry2 = Entry(self, bd=0, bg="#224957", highlightthickness=0)
        entry2.place(x=501.0, y=337.0, width=280.0, height=43.0)

        # creating confirm password label
        canvas.create_text(491.0, 394.0, anchor="nw", text="Confirm password", 
                        fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating confirm password entry
        self.imgEntry3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        canvas.create_image(641.0, 436.5, image=self.imgEntry3)
        entry3 = Entry(self, bd=0, bg="#224957", highlightthickness=0)
        entry3.place(x=501.0, y=414.0, width=280.0, height=43.0)

        # creating create account button
        self.imgCreate = PhotoImage(file=self.relative_to_assets("btnCreate.png"))
        btnCreate = Button(self, image=self.imgCreate, borderwidth=0, highlightthickness=0, 
                        command=None, relief="flat")
        btnCreate.place(x=491.0, y=486.0, width=300.0, height=45.0)

        # creating label do you have an account
        canvas.create_text(491.0, 554.0, anchor="nw", text="Do you have an account?", 
                        fill="#FFFFFF", font=("Montserrat Medium", 14 * -1))

        # creating sign in button
        self.imgSignIn = PhotoImage(file=self.relative_to_assets("btnSignIn.png"))
        btnSignIn = Button(self, image=self.imgSignIn, borderwidth=0, highlightthickness=0, 
                        command=lambda: controller.show_frame("SignInPage"), relief="flat")
        btnSignIn.place(x=737.0, y=554.0, width=59.0, height=21.0)

    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
        
        