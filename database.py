import json

class Database:
    def __init__(self, filename):
        self.filename = filename
        self.books = self.load_from_file()
    
    def load_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_to_file(self):
        with open(self.filename, 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_to_file()

    def get_books(self):
        return self.books