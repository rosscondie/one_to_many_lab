class Book:
    def __init__(self, author, title, genre, id = None):
        self.author = author
        self.title = title
        self.genre = genre
        self.id = id

    # def __repr__(self):
    #     return f"author: {self.author.first_name}\ntitle: {self.title}\ngenre: {self.genre}\nid: {self.id}"