import customtkinter as ctk

  
class Book_list_page(ctk.CTkFrame):
    def __init__(self, parent, controller, *args, **kwargs): 
        super().__init__(parent)
        ctk.set_default_color_theme("blue")
        self.controller = controller
        label = ctk.CTkLabel(self, text ="Book list", font = ("Verdana", 35))
        label.pack(side="top", fill="x", pady=10)
        button1 = ctk.CTkButton(self, text ="Page 1",command = lambda : controller.show_frame(Search_filter))
        button1.pack()
  

class Search_filter(ctk.CTkFrame):
    """
    query by booktitle, author, genre
    """
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent)
        self.controller = controller

        ctk.set_default_color_theme("green") 
        inner_frame = ctk.CTkFrame(self, width=400, height=700, corner_radius=50)
        inner_frame.grid(pady=175, padx=325, sticky='NSWE')
        
        book_title_lable = ctk.CTkLabel(inner_frame, text='Book Title')
        book_title_lable.grid(row=0, column=1, padx=40, pady=20, sticky='EW')

        booktitle_Entry = ctk.CTkEntry(inner_frame, placeholder_text='Title', width=200)
        booktitle_Entry.grid(row=0, column=2, padx=100, pady=20, sticky='EW')

        author_lable = ctk.CTkLabel(inner_frame, text='Book Author')
        author_lable.grid(row=1, column=1, padx=40, pady=20, sticky='EW')

        author_Entry = ctk.CTkEntry(inner_frame, placeholder_text='Title', width=200)
        author_Entry.grid(row=1, column=2, padx=100, pady=20, sticky='EW')

        genres_lable = ctk.CTkLabel(inner_frame,text="Genres")
        genres_lable.grid(row=4, column=1,padx=20, pady=20,sticky="ew")

        genres_option = ctk.CTkOptionMenu(inner_frame, values=["Sci-fi","Horror", "Mystery", "Thriller"], width=100,)
        genres_option.grid(row=4, column=2, padx=20, pady=20, sticky="ew")
                                       
        self.generateResultsButton = ctk.CTkButton(inner_frame, text="Filter", command=lambda : controller.show_frame(Book_list_page))
        self.generateResultsButton.grid(row=5, column=2, padx=50, pady=20, sticky="W")

