from utlis import books, issued_books

def return_book():
    book_id = input("Enter Book ID to return: ").strip()

    if book_id in issued_books:
        # get book details
        book_data = issued_books.pop(book_id)

        # add back to library
        books[book_id] = book_data["book_name"]

        print(f"Book '{book_data['book_name']}' returned successfully")

    else:
        print("This book was not issued")