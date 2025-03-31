class Books:
    def __init__(self, database):
        self.database = database

    def add_book(self, book):
        
        self.database.add_book(book)
        print(f"✅ '{book['title']}' successfully added to your library! 🎉")

    def list_books(self):
        
        books = self.database.get_books()
        if books:
            print("\n📚 Your Book Collection:")
            for idx, book in enumerate(books, start=1):
                print(f"📖 {idx}. {book['title']} | ✍️ {book['authors']} | 🏷️ Status: {book['status']} | 📄 Pages: {book['page_count']}")
        else:
            print("⚠️ No books found in your library! 🫣")

    def update_book_status(self):
        
        books = self.database.get_books()

        if not books:
            print("⚠️ Your library is empty. Add some books first! 📚")
            return

        filtered_books = books.copy()
        search_term = ""

        while True:
            print("\n📖 Your Books:")
            for idx, book in enumerate(filtered_books, start=1):
                print(f"📘 {idx}. {book['title']} ({book.get('status', 'Unknown')})")
            
            search_input = input("\n🔍 Type to filter (press ENTER to confirm selection): ").strip().lower()

            if search_input == "":
                break

            filtered_books = [book for book in books if search_input in book['title'].lower()]
            
            if not filtered_books:
                print("❌ No matching books found. Try again 🔄")
                filtered_books = books.copy()

        while True:
            try:
                choice = int(input("\n✏️ Enter the book number to update: ")) - 1
                if 0 <= choice < len(filtered_books):
                    selected_book = filtered_books[choice]
                    break
                else:
                    print("⚠️ Invalid number. Try again 🔄")
            except ValueError:
                print("❌ Please enter a valid number! 🔢")

        print("\n🎯 Select a new status:")
        print("1️⃣ To Read 📖")
        print("2️⃣ Reading 📚")
        print("3️⃣ Completed ✅")

        while True:
            status_choice = input("🔄 Enter your choice (1/2/3): ").strip()
            if status_choice == "1":
                selected_book['status'] = "To Read 📖"
                break
            elif status_choice == "2":
                selected_book['status'] = "Reading 📚"
                break
            elif status_choice == "3":
                selected_book['status'] = "Completed ✅"
                break
            else:
                print("⚠️ Invalid choice! Please enter 1, 2, or 3 🔢")

        self.database.save_to_file()
        print(f"✅ Status of '{selected_book['title']}' updated to '{selected_book['status']}'! 🎉")

    def search_book(self, search_term):
        
        books = self.database.get_books()
        found_books = [book for book in books if search_term.lower() in book['title'].lower()]

        if found_books:
            print("\n🔍 Found Books:")
            for book in found_books:
                print(f"📖 {book['title']} | ✍️ {book['authors']} | 🏷️ Status: {book['status']} | 📄 Pages: {book['page_count']}")
        else:
            print("❌ No matching books found in your library! 🫤")
