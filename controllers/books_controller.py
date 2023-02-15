from flask import Flask, render_template, request, redirect
from repositories import book_repository, author_repository
from models.book import Book
from models.author import Author

from flask import Blueprint

books_blueprint = Blueprint("books", __name__)

# RESTful CRUD Routes

# NEW
# GET '/books/new'
# Return an HTML form to the browser for us to fill in

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