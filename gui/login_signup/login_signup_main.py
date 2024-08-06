import customtkinter as ctk
from PIL import Image, ImageFilter, ImageTk
from home_page import owner_home_page, librarian_home_page, user_home_page
from abc import ABC, abstractmethod

class Login_Signup_page(ctk.CTkFrame):
    def __init__(self, parent, controller, permision: int, *args, **kwargs):
        super().__init__(parent)
        self.controller = controller
        self.permision = permision

        self.main_page()

    def main_page(self):
        _image = Image.open("gui/media/login_signup/login_signup.jpg").resize((800, 700))
        blurred_image = _image.filter(ImageFilter.GaussianBlur(radius=2))
        image = ImageTk.PhotoImage(blurred_image)

        self.image_left = ctk.CTkLabel(self, image=image, text='')
        self.image_left.grid(row=0, column=0)
    
        self.login_frame = ctk.CTkFrame(self, corner_radius=25, height=420)
        self.login_frame.grid(row=0, column=1, padx=60, pady=130, sticky='NS')
        
        self.login_signup_form()

    def redirect_to_home_page(self):
        home_pages_module = {
            0: owner_home_page.Homepage_Owner,
            1: librarian_home_page.Homepage_Librarian,
            2: user_home_page.Homepage_User,
        }
        self.controller.show_frame(home_pages_module[self.permision])

    @abstractmethod
    def login_signup_form(self):
        pass

    @abstractmethod
    def validate_user(self):
        pass