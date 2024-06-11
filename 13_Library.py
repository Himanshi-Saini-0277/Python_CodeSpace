class Library:
  def __init__(self):
    self.no_of_books = 0
    self.books = []

  def add_books(self, books):
    self.books.append(books)
    self.no_of_books = len(self.books)

  def show_books(self):
    print(f"The no. of books are: {self.no_of_books}.The books are:")
    for book in self.books:
      print(book)

l = Library()
l.add_books("Harry Potter")
l.add_books("Harry Potter 2")
l.add_books("Harry Potter 3")
l.show_books()