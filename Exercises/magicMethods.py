# Magic Methods -> Dunder methods (double underscore) __init__, __str__, __eq__
#                  They are automatically called by many of Python's built in operations
#                  They allow developers to define or customize the behaviors of objects

class Book:
    
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key =='pages':
            return self.num_pages
        else:
            return f"key '{key}' not found"

book1 = Book('To Kill a Mockingbird', 'Harper Lee', 281)
book2 = Book('1984', 'George Orwell', 328)
book3 = Book('Pride and Prejudice', 'Jane Austen', 279)

# print(book1) #__str__ returns string values instead of memory address
# print(book1 == book2)
# print(book2 > book1)
# print(book1 + book2)
# print("Mockingbird" in book1) or # print("Harper" in book1)
print(book1 ['audio'] )