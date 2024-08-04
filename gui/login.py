import customtkinter as ctk
from PIL import Image, ImageFilter, ImageTk

class Login:
    def __init__(self):
        self.login_page()
    
    def login_page(self):
        self.root = ctk.CTk()
        self.root.title('Login')
        self.root.resizable(False, False)
        self.root._set_appearance_mode('dark')
        ctk.set_default_color_theme("dark-blue") 

        _image = Image.open("gui/media/login_image.jpg").resize((800, 700))
        blurred_image = _image.filter(ImageFilter.GaussianBlur(radius=2))
        image = ImageTk.PhotoImage(blurred_image)

        self.image_left = ctk.CTkLabel(self.root, image=image, text='')
        self.image_left.grid(row=0, column=0)
    
        self.login_frame = ctk.CTkFrame(self.root, corner_radius=25, height=400)
        self.login_frame.grid(row=0, column=1, padx=60, pady=150, sticky='NS')

        self.login_welcome_title = ctk.CTkLabel(self.login_frame,text="Welcome Back", text_color="white",font=("gupter",25))
        self.login_welcome_title.grid(row=0, column=0, sticky='N', pady=10)

        self.login_title = ctk.CTkLabel(self.login_frame, text="Enter your name and passwrd \nto access to your account",
                                        text_color='white', font=("nunito sans",12))
        self.login_title.grid(row=1, column=0, sticky='N', pady=10)

        self.email_input = ctk.CTkEntry(self.login_frame, placeholder_text='Email',
                                text_color='White', fg_color='Black', font=('inter', 12),
                                width=200, height=45, corner_radius=15)
        self.email_input.grid(row=2, column=0, padx=30, pady=10)
        self.password_input = ctk.CTkEntry(self.login_frame, placeholder_text='Email',
                                text_color='White', fg_color='Black', font=('inter', 12),
                                width=200, height=45, corner_radius=15)
        self.password_input.grid(row=3, column=0, padx=30, pady=10)

        self.submit_button = ctk.CTkButton(self.login_frame, text='Login',
                                font=('inter', 15, 'bold'), width=100, height=40,
                                command=self.validate_user_login)
        self.submit_button.grid(row=4, column=0, padx=35, pady=20, sticky='S')

        self.forget_password_lable = ctk.CTkLabel(self.login_frame, text='forgot password', text_color='white', font=("",12,"bold"))
        self.forget_password_lable.grid(row=5, column=0, sticky='N')

        self.root.mainloop()

    def validate_user_login(self):
        if self.email_input.get() and self.password_input.get():
            entered_email = self.email_input.get()
            entered_password = self.password_input.get()

            user = None
            
            # TODO: VALIDATE USER FROM DATABASE

            if not user:
                self.login_title.configure(text="Incorrect password or username")
                self.password_input.delete(0, 'end')

            else:
                # TODO
                pass
        else:
            if not self.email_input.get() and not self.password_input.get():
                self.login_title.configure(text="enter your email and password")
            elif not self.password_input.get():
                self.login_title.configure(text="enter your password")
            else:
                self.login_title.configure(text="enter your email")
