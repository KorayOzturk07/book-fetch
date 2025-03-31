import requests

class GoogleBooksAPI:
    def __init__(self):
        self.api_url = "https://www.googleapis.com/books/v1/volumes?q="

    def search_books(self, query):
        
        url = f"{self.api_url}{query}&maxResults=10"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data.get('items', [])
        else:
            print("❌ Error fetching data from Google Books API.")
            return []

    def display_search_results(self, books):
        
        if not books:
            print("❌ No books found.")
            return

        print("\n📚 Search Results:")
        for i, book in enumerate(books, 1):
            volume_info = book.get('volumeInfo', {})
            title = volume_info.get('title', 'No title')
            authors = ', '.join(volume_info.get('authors', ['No authors']))
            page_count = volume_info.get('pageCount', 'No page count')
            link = volume_info.get('infoLink', 'No link available')

            print(f"{i}. 📖 {title} | 🖊️ {authors} | 📄 {page_count} pages")
            print(f"   🔗 {link}\n")

    def select_book(self, books, index):
        
        if not books:
            print("❌ No books available to select.")
            return None

        if index < 1 or index > len(books):
            print("❌ Invalid book selection. Please enter a valid number.")
            return None

        selected_book = books[index - 1]
        volume_info = selected_book.get('volumeInfo', {})

        title = volume_info.get('title', 'No title')
        authors = ', '.join(volume_info.get('authors', ['No authors']))
        page_count = volume_info.get('pageCount', 'No page count')
        link = volume_info.get('infoLink', 'No link available')

        return {
            "title": title,
            "authors": authors,
            "page_count": page_count,
            "status": "To Read",
            "link": link
        }
