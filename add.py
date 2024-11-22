def add():
    title = input("Enter book title : ")
    author = input("Enter author name : ")
    isbn = input("Enter ISBN number : ")
    price = input("Enter unit price : ")

    book = {
        'title': title,
        'author': author,
        'isbn': isbn,
        'price': price
    }

    with open("allBooks.csv", "a") as allBooksFile:
        allBooksFile.write(f"{book['title']}, {book['author']}, {book['isbn']}, {book['price']}\n")

    print("Book added successfully.")