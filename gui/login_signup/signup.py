import customtkinter as ctk
from . import login_signup_main, login

class Signup_page(login_signup_main.Login_Signup_page):
    def __init__(self, parent, controller, permision: int, *args, **kwargs):
        super().__init__(parent, controller, permision)
        self.parent=parent
        self.controller = controller
        self.permision = permision

    def login_signup_form(self):
        self.login_welcome_title = ctk.CTkLabel(self.login_frame,text="Welcome", text_color="white",font=("gupter",25))
        self.login_welcome_title.grid(row=0, column=0, sticky='N', pady=10)

        self.login_title = ctk.CTkLabel(self.login_frame, text="Enter your email address \nto create an account.",
                                        text_color='white', font=("nunito sans",12))
        self.login_title.grid(row=1, column=0, sticky='N', pady=10)

        self.email_input = ctk.CTkEntry(self.login_frame, placeholder_text='Email',
                                text_color='White', fg_color='Black', font=('inter', 12),
                                width=200, height=45, corner_radius=15)
        self.email_input.grid(row=2, column=0, padx=30, pady=10)

        self.password_input = ctk.CTkEntry(self.login_frame, placeholder_text='Password',
                                text_color='White', fg_color='Black', font=('inter', 12),
                                width=200, height=45, corner_radius=15)
        self.password_input.grid(row=3, column=0, padx=30, pady=5)

        self.confirm_password_input = ctk.CTkEntry(self.login_frame, placeholder_text='Confirm Password',
                                text_color='White', fg_color='Black', font=('inter', 12),
                                width=200, height=45, corner_radius=15)
        self.confirm_password_input.grid(row=4, column=0, padx=30, pady=5)

        self.submit_button = ctk.CTkButton(self.login_frame, text='Sign up',
                                font=('inter', 15, 'bold'), width=100, height=40,
                                command=self.validate_user)
        self.submit_button.grid(row=5, column=0, padx=35, pady=20, sticky='S')

        self.log_in = ctk.CTkLabel(self.login_frame, text='Already have an account? \nLog in',
                                                  text_color='white',font=("",12,"bold"))
        self.log_in.grid(row=6, column=0, sticky='N')  
        self.log_in.bind("<Button-1>",
                        lambda event: self.controller.show_frame(login.Login_page))

    def validate_user(self):
        if self.password_input.get() != self.confirm_password_input.get():
            raise ValueError('password must be matched')
        
        # TODO check email dosen't exist in database
        
        else:
            # TODO
            pass











