from tkinter import *
from pathlib import Path
import account


# Frame for sign in page
class SignInPage(Frame):
    # constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    # sign in page class init method
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # creating the whole canvas of the frame
        self.canvas = Canvas(self, bg="#093545", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # creating the bottom image for design
        self.curvy = PhotoImage(file=self.relative_to_assets("curvy.png"))
        self.canvas.create_image(640.0, 664.0, image=self.curvy)

        # creating sign in label
        self.canvas.create_text(541.0, 174.0, anchor="nw", text="Sign in",
                                fill="#FFFFFF", font=("LexendDeca Regular", 64 * -1))

        # creating starting label
        self.canvas.create_text(485.0, 260.0, anchor="nw", text="Sign in to start managing student information",
                                fill="#FFFFFF", font=("LexendDeca Regular", 16 * -1))

        # creating email label
        self.canvas.create_text(490.0, 321.0, anchor="nw", text="Email",
                                fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating email entry
        self.imgEntry1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(640.0, 363.5, image=self.imgEntry1)
        self.entry1 = Entry(self, bd=0, bg="#224957", highlightthickness=0)
        self.entry1.place(x=500.0, y=341.0, width=280.0, height=43.0)

        # creating password label
        self.canvas.create_text(490.0, 398.0, anchor="nw", text="Password",
                                fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating password entry
        self.imgEntry2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.canvas.create_image(640.0, 440.5, image=self.imgEntry2)
        self.entry2 = Entry(self, bd=0, bg="#224957", highlightthickness=0)
        self.entry2.place(x=500.0, y=418.0, width=280.0, height=43.0)

        # creating login button
        self.imgLogin = PhotoImage(file=self.relative_to_assets("btnLogin.png"))
        btnLogin = Button(self, image=self.imgLogin, borderwidth=0, highlightthickness=0,
                          command=lambda: self.to_menu(controller), relief="flat")
        btnLogin.place(x=491.0, y=486.0, width=300.0, height=45.0)

        # creating label do you have an account
        self.canvas.create_text(490.0, 554.0, anchor="nw", text="Don't have an account?",
                                fill="#FFFFFF", font=("Montserrat Medium", 14 * -1))

        # creating sign up button
        self.imgSignUp = PhotoImage(file=self.relative_to_assets("btnSignUp.png"))
        btnSignUp = Button(self, image=self.imgSignUp, borderwidth=0, highlightthickness=0,
                           command=lambda: controller.show_frame("SignUpPage", controller.id), relief="flat")
        btnSignUp.place(x=731.0, y=551.0, width=63.0, height=25.0)

    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    # transition to the right menu
    def to_menu(self, controller):
        self.clear_text()
        if controller.id == "student":
            filename = "Student_Credentials.txt"
            email = str(self.entry1.get())
            password = str(self.entry2.get())
            sign_in = account.login(filename, email, password)

            if sign_in == 1:  # Logged in successfully
                response = Label(self.canvas,
                                 anchor="nw",
                                 text="Logged in successfully!",
                                 fg="#52EFA0",
                                 bg="#093545",
                                 font=("LexendDeca Regular", 16 * -1)).place(x=551, y=286)

                # then will proceed to student menu
                controller.show_frame("StudentMenu")

            elif sign_in == 2:  # Account does not exist!
                response = Label(self.canvas,
                                 anchor="nw",
                                 text="Account does not exist!",
                                 fg="#F04C42",
                                 bg="#093545",
                                 font=("LexendDeca Regular", 16 * -1)).place(x=550, y=286)

            else:   # Incorrect email or password!
                response = Label(self.canvas,
                                 anchor="nw",
                                 text="Incorrect email or password!",
                                 fg="#E7A90A",
                                 bg="#093545",
                                 font=("LexendDeca Regular", 16 * -1)).place(x=529, y=286)

        else:
            filename = "Admin_Credentials.txt"
            email = str(self.entry1.get())
            password = str(self.entry2.get())
            sign_in = account.login(filename, email, password)

            if sign_in == 1:  # Logged in successfully
                self.response = Label(self.canvas,
                                 anchor="nw",
                                 text="Logged in successfully!",
                                 fg="#52EFA0",
                                 bg="#093545",
                                 font=("LexendDeca Regular", 16 * -1)).place(x=551, y=286)

                # then will proceed to student menu
                controller.show_frame("AdminMenu")

            elif sign_in == 2:  # Account does not exist!
                self.response = Label(self.canvas,
                                 anchor="nw",
                                 text="Account does not exist!",
                                 fg="#F04C42",
                                 bg="#093545",
                                 font=("LexendDeca Regular", 16 * -1)).place(x=550, y=286)

            else:  # Incorrect email or password!
                self.response = Label(self.canvas,
                                 anchor="nw",
                                 text="Incorrect email or password!",
                                 fg="#E7A90A",
                                 bg="#093545",
                                 font=("LexendDeca Regular", 16 * -1)).place(x=529, y=286)

    # clearing entry inputs
    def clear_text(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)


