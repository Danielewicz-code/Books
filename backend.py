class Book:
    def __init__(self, title, author, genre, content, publish_date) -> None:
        self.title = title
        self.author = author
        self.genre = genre
        self.content = content
        self.publish_date = publish_date

    def read(self, book_title):
        if book_title == self.title:
            print(self.content)
        else:
            raise ValueError(f"The book '{book_title}' was not found.")
        
    def get_preview(self, book_title):
        if book_title == self.title:
            print(f"\n{book_title} preview:\n{self.content[:100]}... for the full reading acces the main book '{book_title}'.\n")
        else:
            raise ValueError(f"The book '{book_title}' was not found.")
        
    def publish(self, library):
        library.publish_book(self)


class Library:
    def __init__(self) -> None:
        self.books_library = []
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        print(f"{user.username} was added to the main library")

    def publish_book(self, book):
        self.books_library.append(book)
        print(f"The book '{book.title}' by {book.author} has been added to the main library. Now anyone can read it!")

    def see_books(self):
        for i, book in enumerate(self.books_library):
            print(f"Index: {i}")
            print(f"Book Title: {book.title}\nAuthor: {book.author}\nGenre: {book.genre}\nPublish Date: {book.publish_date}\n")

    def find_by_title(self, book_title):
        return [book for book in self.books_library if book.title == book_title]
    
    def find_by_author(self, author_name):
        return [a for a in self.books_library if a.author == author_name]
    
    def find_by_genre(self, genre_search):
        return [g for g in self.books_library if g.genre == genre_search]
    
    

class User:
    def __init__(self, username, email, password, library) -> None:
        self.username = username
        self.email = email
        self.password = password
        self.main_library = library
        self.personal_library = []

    def browse_books(self):

        print("Choose a category to browse: Title, Author, Genre")
        category = input("Input the category: ").strip().lower()
        query = input(f"Input the {category}: ")

        browse_methods = {
            "title":self.main_library.find_by_title,
            "author":self.main_library.find_by_author,
            "genre":self.main_library.find_by_genre
        }

        if category in browse_methods:
            results = browse_methods[category](query)
            if results:
                print("Results:\n")
                for i, book in enumerate(results, start=1):
                    print(f"{i}. Book Title: {book.title}\nAuthor: {book.author}\nGenre: {book.genre}\nPublish Date: {book.publish_date}\n")
            else:
                print(f"No books for {category}: {query}")
        else:
            print(f"Invalid category: {category}")

    def add_to_library(self, book_title):
        book_found = None
        for book in self.main_library.books_library:
            if book.title == book_title:
                book_found = book
                break
        
        if book_found:
            self.personal_library.append(book_found)
            print(f"\n{book_found.title} has been added to {self.username} personal library.")
        else:
            print(f"\n{book_title} does not exist.")

    def publish_book(self, book):
        self.main_library.publish_book(book)

    def see_personal_library(self):
        for i, book in enumerate(self.personal_library):
            print(f"Index: {i}")
            print(f"Book Title: {book.title}\nAuthor: {book.author}\nGenre: {book.genre}\nPublish Date: {book.publish_date}\n")


