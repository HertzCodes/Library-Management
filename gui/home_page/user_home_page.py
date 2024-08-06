import customtkinter as ctk
from PIL import Image
from . import home_page
from books_list import book_list


class Homepage_User(home_page.Homepage_main):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, controller)
        self.controller = controller

    # abstractmethod
    def side_bar(self):
        # open icons
        profile_icon = ctk.CTkImage(dark_image=Image.open("gui/media/home_page/users.png"), size=(30, 30))
        bookstore_icon = ctk.CTkImage(dark_image=Image.open("gui/media/home_page/bookstore.png"), size=(30, 30))
        setting_icon = ctk.CTkImage(dark_image=Image.open("gui/media/home_page/setting.png"), size=(30, 30))
        question_icon = ctk.CTkImage(dark_image=Image.open("gui/media/home_page/question.png"), size=(30, 30))

        self.side_bar_button = ctk.CTkButton(self.side_bar_frame, text='☰',font=("nunito sans", 20, 'bold'), corner_radius=10,
                                            command=self.side_bar_toggle,width=42, height=42, fg_color='white', text_color='black')
        self.side_bar_button.place(x=5, y=5)

        self.side_profile_icon = ctk.CTkButton(self.side_bar_frame, image=profile_icon,
                                            text=None, width=30, height=30, fg_color='white', corner_radius=10)
        self.side_profile_icon.place(x=0, y=160)

        self.side_bookstore_icon = ctk.CTkButton(self.side_bar_frame, image=bookstore_icon,
                                                text=None, width=30, height=30, fg_color='white', corner_radius=10,
                                                command=lambda : self.controller.show_frame(book_list.Book_list_page))
        self.side_bookstore_icon.place(x=0, y=200)

        self.side_question_icon = ctk.CTkButton(self.side_bar_frame, image=question_icon,
                                            text=None, width=30, height=30, fg_color='white', corner_radius=10)
        self.side_question_icon.place(x=0, y=600)

        self.side_sttings_icon = ctk.CTkButton(self.side_bar_frame, image=setting_icon,
                                            text=None, width=30, height=30, fg_color='white', corner_radius=10)
        self.side_sttings_icon.place(x=0, y=650)
    
    # abstractmethod 
    def side_bar_toggle(self):
        self.side_bar_frame.configure(width=200)

        self.side_bar_button.configure(text='X', command=self.close_side_bar, width=190)
        self.side_profile_icon.configure(text = 'Profile', font=("nunito sans", 10, 'bold'), text_color='black', width=192)
        self.side_bookstore_icon.configure(text = 'Book store', font=("nunito sans", 10, 'bold'), text_color='black', width=192)
        self.side_sttings_icon.configure(text = 'Settings', font=("nunito sans", 10, 'bold'), text_color='black', width=192)
        self.side_question_icon.configure(text = 'Ask question', font=("nunito sans", 10, 'bold'), text_color='black', width=192)
    
    # abstractmethod 
    def close_side_bar(self):
        self.side_bar_frame.configure(width=50)

        self.side_bar_button.configure(text='☰', width=42, command=self.side_bar_toggle)
        self.side_profile_icon.configure(width=30)
        self.side_bookstore_icon.configure(width=30)
        self.side_sttings_icon.configure(width=30)
        self.side_question_icon.configure(width=30)

