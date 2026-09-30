#LIBRARY MANAGEMENT SYSTEM

books = []
issued_books = []
total_fine = 0

#ADD BOOK
def add_book():
    book_id = input("Enter Book ID: ")
    if book_id:
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        book = {"id": book_id,"title": title,"author": author,"status": "Available"}
        books.append(book)
        print(" Book added successfully!")


#DISPLAY BOOKS
def display_books():
    if len(books) == 0:
        print("No books are available.")
        return

    print("BOOK LIST")

    for book in books:
        print("Book ID :", book["id"])
        print("Title   :", book["title"])
        print("Author  :", book["author"])
        print("Status  :", book["status"])

#SEARCH BOOK
def search_book():
    search = input("Enter Book ID or Title to search: ")

    found = False

    for book in books:
        if book["id"] == search or book["title"].lower() == search.lower():
            print("Book Found :)")
            print("Book ID :", book["id"])
            print("Title   :", book["title"])
            print("Author  :", book["author"])
            print("Status  :", book["status"])

            found = True

    if found == False:
        print("Book not found.")


#ISSUE BOOK
def issue_book():
    book_id = input("Enter Book ID to issue: ")
    student_name = input("Enter Student Name: ")
    student_id = input("Enter Student ID: ")

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Available":
                book["status"] = "Issued"
                issue_record = {"book_id": book_id,"student_name": student_name,"student_id": student_id}
                issued_books.append(issue_record)

                print("Book issued successfully!")
                print("Student Name:", student_name)
                print("Book:", book["title"])
                return
            else:
                print("Book is already issued.")
                return
    print("Book not found.")


# RETURN BOOK
def return_book():
    global total_fine

    book_id = input("Enter Book ID to return: ")
    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Issued":
                book["status"] = "Available"
                days = int(input("Enter number of days book was kept: "))
                fine = calculate_fine(days)
                total_fine = total_fine + fine
                print("Book returned successfully!")
                if fine > 0:
                    print("Fine to be paid: ₹ ", fine)
                else:
                    print("No fine.")
                return
            else:
                print("This book was not issued.")
                return
    print("Book not found.")


# CALCULATE FINE
def calculate_fine(days):
    ad = 7

    if days > ad:
        ld = days - ad
        fine = ld * 5
        return fine

    return 0


#LIBRARY REPORT
def library_report():

    total_books = len(books)
    available_books = 0
    issued = 0

    for book in books:
        if book["status"] == "Available":
            available_books += 1
        else:
            issued += 1

    print("LIBRARY REPORT")
    print("Total Books     :", total_books)
    print("Available Books :", available_books)
    print("Issued Books    :", issued)

    
# MAIN PROGRAM
while True:
    print("LIBRARY MANAGEMENT SYSTEM")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Library Report")
    print("7. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        display_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        library_report()

    elif choice == "7":
        print(" Thanks for using the Library Management System <3 ")
        break

    else:
        print(" Invalid choice :(")
