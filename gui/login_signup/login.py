import customtkinter as ctk
from . import login_signup_main, signup

class Login_page(login_signup_main.Login_Signup_page):
    def __init__(self, parent, controller, permision: int, *args, **kwargs):
        super().__init__(parent, controller, permision)
        self.parent=parent
        self.controller = controller
        self.permision = permision

    def login_signup_form(self):
        self.login_welcome_title = ctk.CTkLabel(self.login_frame,text="Welcome Back", text_color="white",font=("gupter",25))
        self.login_welcome_title.grid(row=0, column=0, sticky='N', pady=10)

        self.login_title = ctk.CTkLabel(self.login_frame, text="Enter your name and passwrd \nto access to your account",
                                        text_color='white', font=("nunito sans",12))
        self.login_title.grid(row=1, column=0, sticky='N', pady=30)

        self.email_input = ctk.CTkEntry(self.login_frame, placeholder_text='Email',
                                text_color='White', fg_color='Black', font=('inter', 12),
                                width=200, height=45, corner_radius=15)
        self.email_input.grid(row=2, column=0, padx=30, pady=10)

        self.password_input = ctk.CTkEntry(self.login_frame, placeholder_text='Password',
                                text_color='White', fg_color='Black', font=('inter', 12),
                                width=200, height=45, corner_radius=15)
        self.password_input.grid(row=3, column=0, padx=30, pady=10)

        self.submit_button = ctk.CTkButton(self.login_frame, text='Login',
                                font=('inter', 15, 'bold'), width=100, height=40,
                                command=self.validate_user)
        self.submit_button.grid(row=4, column=0, padx=35, pady=20, sticky='S')

        self.signup = ctk.CTkLabel(self.login_frame, text='No accout? Create one', text_color='white',font=("",12,"bold"))
        self.signup.grid(row=5, column=0, sticky='N')  
        self.signup.bind("<Button-1>",
                        lambda event: self.controller.show_frame(signup.Signup_page))

    def validate_user(self):
        if self.email_input.get() and self.password_input.get():
            entered_email = self.email_input.get()
            entered_password = self.password_input.get()

            user = True
            
            # TODO: VALIDATE USER FROM DATABASE

            if not user:
                self.login_title.configure(text="Incorrect password or username")
                self.password_input.delete(0, 'end')

            else:
                # TODO
                self.redirect_to_home_page()
                
        else:
            if not self.email_input.get() and not self.password_input.get():
                self.login_title.configure(text="enter your email and password")
            elif not self.password_input.get():
                self.login_title.configure(text="enter your password")
            else:
                self.login_title.configure(text="enter your email")












