from flask import Flask, render_template, request, redirect
from repositories import book_repository, author_repository
from models.book import Book


from flask import Blueprint

books_blueprint = Blueprint("books", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/books'
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

# NEW
# GET '/books/new'
# Return an HTML form to the browser for us to fill in
@books_blueprint.route("/books/new")
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors = authors)


# CREATE 
# POST '/books'
# Recieve the data from the form and put a new entry into the database

# SHOW
# GET '/books/<id>' 
# Return a seperate HTML file '/books/show.html'

# EDIT
# GET '/books/<id>/edit'
# Return a seperate HTML file '/books/edit.html'

# UPDATE 
# POST '/books/<id>'
# Redirect back to '/books'

# DELETE
# POST /'books/<id> 
# Redirect back to '/books'