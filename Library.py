class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True
        print("Borrowed:",self.title)

    def return_book(self):
        self.is_borrowed = False
        print("Returned:",self.title)

    Book1 = ("Oliver Twist" , "Charles Dickens")
    Book2 = ("Foundling" , "Nina Podlesynak")
    Book3 = ("The Witches" , "Roald Dahl")

    Book1.borrow()
    Book1.return_book()
    Book2.borrow()

    print(Book1.title,"Borrowed:" , Book1.is__borrowed)
    print(Book2.title,"Borrowed:" , Book2.is__borrowed)
    print(Book3.title,"Borrowed:" , Book3.is__borrowed)



