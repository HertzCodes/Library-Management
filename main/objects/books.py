class Book:
    def __init__(self, book_id, title, author , summary , genre , date_added , is_borrowed , borrowed_by: list, stock):
        self.id = book_id
        self.title = title
        self.author = author
        self.summary = summary
        self.genre = genre
        self.date_added = date_added
        self.is_borrowed = is_borrowed
        self.borrowed_by = borrowed_by
        self.stock = stock
        self.in_library = self.stock - len(self.borrowed_by)

