from books_fetch import GoogleBooksAPI
from books import Books
from database import Database

def main():
    
    database = Database("books.json")
    books_manager = Books(database)
    books_fetch = GoogleBooksAPI()

    while True:
        print("\n📚 Library Application")
        print("1️⃣ Search and Add a Book")
        print("2️⃣ List Books")
        print("3️⃣ Update Book Status")
        print("4️⃣ Search for a Book in Library")
        print("5️⃣ Exit")

        choice = input("➡️ Choose an option: ").strip()

        if choice == "1":
            book_title = input("\n🔍 Enter the book title you want to search for: ").strip()
            books = books_fetch.search_books(book_title)

            if not books:
                print("❌ No books found. Try again!")
                continue

            books_fetch.display_search_results(books)

            while True:
                try:
                    index = int(input("\n📌 Select the number of the book to add: ")) - 1
                    if 0 <= index < len(books):
                        break
                    else:
                        print("⚠️ Invalid selection. Enter a valid book number.")
                except ValueError:
                    print("❌ Please enter a number.")

            book = books_fetch.select_book(books, index)

            if book is None:  
                print("❌ Failed to fetch book details. Try another selection.")
                continue

            books_manager.add_book(book)
            print(f"✅ '{book['title']}' has been added to your library! 🎉")

        elif choice == "2":
            books_manager.list_books()

        elif choice == "3":
            books_manager.update_book_status()

        elif choice == "4":
            search_term = input("\n🔎 Enter a search term: ").strip()
            books_manager.search_book(search_term)

        elif choice == "5":
            print("👋 Goodbye! See you next time. 📖")
            break

        else:
            print("❌ Invalid choice! Please enter a number between 1-5.")

if __name__ == "__main__":
    main()
