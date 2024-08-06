import customtkinter as ctk

from login_signup import login, signup
from home_page import owner_home_page, librarian_home_page, user_home_page
from books_list import book_list


class main(ctk.CTk):
    def __init__(self, permision=0, *args, **kwargs): 
        super().__init__()
        self.geometry('1200x700')
        self.title('Books list')
        self.resizable(False, False)
        self._set_appearance_mode('dark')
         
        container = ctk.CTkFrame(self)  
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        

        pages = [login.Login_page,
                 signup.Signup_page,
                 book_list.Book_list_page,
                 book_list.Search_filter]
         
        home_pages_module = {
            0: owner_home_page.Homepage_Owner,
            1: librarian_home_page.Homepage_Librarian,
            2: user_home_page.Homepage_User,
        }

        try:
            pages += [home_pages_module[permision]]
        except:
            raise ValueError('not valid permision')                
        
        self.frames = {}  
        for page in pages:
            window = page(container, self, permision)
            self.frames[page] = window
            window.grid(row = 0, column = 0, sticky='NWES')
        self.show_frame(login.Login_page)
        self.mainloop()


    def show_frame(self, current_window):
        frame = self.frames[current_window]
        frame.tkraise()

app = main()
