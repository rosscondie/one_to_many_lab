import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Christopher", "McDougall")
author_repository.save(author_1)

author_2 = Author("Phil", "Knight")
author_repository.save(author_2)

author_3 = Author("William", "Finnegan")
author_repository.save(author_3)

author_4 = Author("JK", "Rowling")
author_repository.save(author_4)

book_1 = Book(author_1, "Born To Run", "Memoir/Sport")
book_repository.save(book_1)

book_2 = Book(author_2, "Shoe Dog", "Memoir/Biography")
book_repository.save(book_2)

book_3 = Book(author_3, "Barbarian Days", "Biography/Sport")
book_repository.save(book_3)

book_4 = Book(author_4, "Harry Potter And The Philosopher's Stone", "Fantasy")
book_repository.save(book_4)

book_5 = Book(author_4, "Harry Potter And The Chamer of Secrets", "Fantasy")
book_repository.save(book_5)



# pdb.set_trace() Delete this to stop having to quit out of pdb