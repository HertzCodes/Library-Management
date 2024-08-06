import customtkinter as ctk
from PIL import Image, ImageTk, ImageFilter
import tkinter as tk
from abc import ABC, abstractmethod
from tkinter import messagebox

class Homepage_main(ctk.CTkFrame, ABC):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent)
        self.controller = controller
        self.main()

    def main(self, username=None):
        _image = Image.open("gui/media/login_signup/login_signup.jpg").resize((1200, 700))
        blurred_image = _image.filter(ImageFilter.GaussianBlur(radius=0))
        image = ImageTk.PhotoImage(blurred_image)

        self.image_left = ctk.CTkLabel(self, image=image, text='')
        self.image_left.grid(row=0, column=0)

        self.side_bar_frame = ctk.CTkFrame(self, height=700, width=52, bg_color='black')
        self.side_bar_frame.grid(row=0, column=0, sticky='W')

        self.side_bar()
        self.show_username(username)


    def show_username(self, username=None):
        username_lable = ctk.CTkLabel(self, text=f'Hello {username}', font=("Oswald", 12, 'bold'))
        username_lable.grid(row=0, column=0, sticky='NE', padx=70, pady=15)
        logout_icon = ctk.CTkImage(dark_image=Image.open("/home/roozbeh/Downloads/icons8-logout-48.png"), size=(30, 30))
        self.logout_icon = ctk.CTkButton(self, image=logout_icon,
                                            text=None, width=30, height=30, fg_color='white', corner_radius=10, command=self.Exit_app)
        self.logout_icon.place(x=1140, y=10)

    @staticmethod
    def Exit_app():
        msg = tk.messagebox.askquestion("Close Library", "Are you sure you want to CLOSE LIBRARY?", icon="warning")
        if msg == 'yes':
            exit()
        else:
            messagebox.showinfo('Return', 'you will return to Home Page')
    
    @abstractmethod
    def side_bar(self):
        pass

    @abstractmethod
    def side_bar_toggle(self):
        pass

    @abstractmethod
    def close_side_bar(self):
        pass

