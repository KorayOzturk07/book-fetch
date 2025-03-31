
# 📚 Library Management Application

A simple yet powerful library management system that allows users to search for books using the Google Books API, add books to their personal library, and manage their library with various features like updating book status and searching within the library.

## Features

- Search for books using the Google Books API.
- Add books to your personal library.
- List all the books in your library.
- Update the status of books (To Read, Reading, Completed).
- Search books in your library by title.
- Store all data locally in a JSON file (`books.json`).

## Requirements

To run this project, you will need:

- Python 3.x
- `requests` library (for making API requests to Google Books API)
- A `books.json` file (for storing the library data)

### Install the required Python libraries:

```bash
pip install -r requirements.txt
```

If `requirements.txt` does not exist, you can manually install the required libraries with:

```bash
pip install requests
```

## Project Structure

- **`main.py`**: Entry point of the application that runs the menu and interacts with the user.
- **`books.py`**: Contains the `Books` class responsible for managing the book collection (add, list, update, search).
- **`database.py`**: Handles reading and writing data from the `books.json` file (database).
- **`books_fetch.py`**: Manages interaction with the Google Books API to search for books and retrieve book information.

## How to Use

1. **Clone the repository**:

```bash
git clone https://github.com/KorayOzturk07/book-fetch
cd library-management
```

2. **Run the application**:

```bash
python main.py
```

3. **Follow the on-screen prompts** to:
   - Search for books to add.
   - View the list of books in your library.
   - Update the reading status of your books.
   - Search for books in your library.

## Features Walkthrough

1. **Search and Add a Book**:
   - When you select this option, you will be prompted to enter a book title.
   - The app will display a list of matching books retrieved from Google Books API.
   - Select the book you want to add by entering the number corresponding to the book.
   - The selected book is then added to your library.

2. **List Books**:
   - This option lists all the books currently stored in your library along with their status and other details.

3. **Update Book Status**:
   - This option allows you to update the reading status of a book (To Read, Reading, Completed).

4. **Search for a Book in Library**:
   - You can search for a specific book in your library by entering a search term (book title).

## Data Storage

The book information is stored in a JSON file (`books.json`) which is automatically created if it doesn't already exist. This file will contain the following structure:

```json
[
    {
        "title": "Book Title",
        "authors": "Author Name",
        "page_count": 320,
        "status": "To Read",
        "link": "https://linktothebook.com"
    },
    ...
]
```

## Contributing

Feel free to fork this repository, submit issues, and send pull requests to improve this project!

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Create a new pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
