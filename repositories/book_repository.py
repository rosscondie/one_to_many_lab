from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository

def save(book):
    sql = "INSERT INTO books (author_id, title, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [book.author.id, book.title, book.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book