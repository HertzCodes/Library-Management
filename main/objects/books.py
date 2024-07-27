class Book:
    def __init__(self,ID ,title , summary , genre , date_added , writer, is_borrowed = False, borrowed_by = None) -> None:
        self.information = {'id': ID , 'title': title , 'summary' : summary , 'genre' : genre , 'date_added' : date_added
                            , 'writer' : writer , 'is_borrowed': is_borrowed , 'borrowed_by' : borrowed_by}