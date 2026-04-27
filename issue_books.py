from utlis import books, issued_books

def issue_book():
    book_id = input("Enter Book ID to issue: ").strip()

    # check if book exists in library
    if book_id in books:

        # optional: ask student name
        student_name = input("Enter student name: ").strip()

        # move book from available → issued
        issued_books[book_id] = {
            "book_name": books.pop(book_id),
            "issued_to": student_name
        }

        print(f"Book '{book_id}' issued to {student_name}")

    else:
        # check if already issued
        if book_id in issued_books:
            print("Book is already issued")
        else:
            print("Book ID not found")