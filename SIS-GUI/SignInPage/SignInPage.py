from tkinter import *
from pathlib import Path

# Frame for sign in page
class SignInPage(Frame):
    # constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    # sign in page class init method
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # creating the whole canvas of the frame
        canvas = Canvas(self, bg = "#093545", height = 720, width = 1280, bd = 0, highlightthickness = 0, relief = "ridge")
        canvas.place(x = 0, y = 0)

        # creating the bottom image for design
        self.curvy = PhotoImage(file=self.relative_to_assets("curvy.png"))
        canvas.create_image(640.0, 664.0, image=self.curvy)

        # creating sign in label
        canvas.create_text(541.0, 174.0, anchor="nw", text="Sign in", 
                        fill="#FFFFFF", font=("LexendDeca Regular", 64 * -1))

        # creating starting label
        canvas.create_text(485.0, 260.0, anchor="nw", text="Sign in to start managing student information", 
                        fill="#FFFFFF", font=("LexendDeca Regular", 16 * -1))

        # creating email label
        canvas.create_text(490.0, 321.0, anchor="nw", text="Email", 
                        fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))
                    
        # creating email entry
        self.imgEntry1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        canvas.create_image(640.0, 363.5, image=self.imgEntry1)
        self.entry1 = Entry(self, bd=0, bg="#224957", highlightthickness=0)
        self.entry1.place(x=500.0, y=341.0, width=280.0, height=43.0)

        # creating password label
        canvas.create_text(490.0, 398.0, anchor="nw", text="Password", 
                        fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating password entry
        self.imgEntry2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        canvas.create_image(640.0, 440.5, image=self.imgEntry2)
        self.entry2 = Entry(self, bd=0, bg="#224957", highlightthickness=0)
        self.entry2.place(x=500.0, y=418.0, width=280.0, height=43.0)

        # creating login button
        self.imgLogin = PhotoImage(file=self.relative_to_assets("btnLogin.png"))
        btnLogin = Button(self, image=self.imgLogin, borderwidth=0, highlightthickness=0, 
                        command=lambda: self.to_menu(controller), relief="flat")
        btnLogin.place(x=491.0, y=486.0, width=300.0, height=45.0)

        # creating label do you have an account
        canvas.create_text(490.0, 554.0, anchor="nw", text="Don't have an account?", 
                        fill="#FFFFFF", font=("Montserrat Medium", 14 * -1))

        # creating sign up button
        self.imgSignUp = PhotoImage(file=self.relative_to_assets("btnSignUp.png"))
        btnSignUp = Button(self, image=self.imgSignUp, borderwidth=0, highlightthickness=0, 
                        command=lambda: controller.show_frame("SignUpPage"), relief="flat")
        btnSignUp.place(x=731.0, y=551.0, width=63.0, height=25.0)

    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    # transition to the right menu
    def to_menu(self, controller):
        self.clear_text()
        if controller.id == "student":
            controller.show_frame("StudentMenu")
        else:
            controller.show_frame("FacultyMenu")

    # clearing entry inputs
    def clear_text(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)