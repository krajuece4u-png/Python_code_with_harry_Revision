# 4. Magic/Dunder Methods
#     1. Create a class Book with attributes title and author .
#         1. Implement __str__() so that printing the object displays "Title by Author" .
#         2. Implement __len__() so that len(book) returns the length of the title.
#     2. Create two Book objects and test these methods.

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        print(f"The book {self.title} by {self.author}")

    def __len__(self):
        return len(self.title)
    

B1 = Book("Electomagnetic", "Raju")
B1.__str__()
Len_Book = B1.__len__()
print(Len_Book)
        