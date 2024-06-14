#test
library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", "In my younger and more vulnerable years...", "1925-04-10")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", "When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow...", "1960-07-11")

library.publish_book(book1)
library.publish_book(book2)

user = User("Jozef", "jozef@gmail.com", "Violin15", library)
library.add_user(user)
#User browsing main library
user.browse_books()

# User adding book to personal library
user.add_to_library("The Great Gatsby")

# User viewing personal library
user.see_personal_library()
library.see_books()

# User publishing a new book to the main library
new_book = Book("1984", "George Orwell", "Dystopian", "It was a bright cold day in April, and the clocks were striking thirteen.", "1949-06-08")
user.publish_book(new_book)

# User browsing main library again to see the newly added book
user.browse_books()
