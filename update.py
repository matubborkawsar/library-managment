def update():
    with open("allBooks.csv", "r") as allBooksFile:
        content = allBooksFile.readlines()

        if content:
            for index, item in enumerate(content):
                print(f"{index + 1}. {item.strip()}")

            updateBook = int(input("Choose a book to update : "))

            bookDetails = content[updateBook - 1].strip().split(", ")

            if 1 <= updateBook <= len(content):
                print("1. Update title")
                print("2. Update author")
                print("3. Update ISBN")
                print("4. Update price")

                updateOption = int(input("Choose an option : "))

                if updateOption == 1:
                    newTitle = input("Enter new title : ")
                    bookDetails[0] = newTitle

                elif updateOption == 2:
                    newAuthor = input("Enter new author : ")
                    bookDetails[1] = newAuthor

                elif updateOption == 3:
                    newIsbn = input("Enter new ISBN : ")
                    bookDetails[2] = newIsbn

                elif updateOption == 4:
                    newPrice = input("Enter new price : ")
                    bookDetails[3] = newPrice

                else:
                    print("Invalid option.")

                content[updateBook - 1] = f"{bookDetails[0]}, {bookDetails[1]}, {bookDetails[2]}, {bookDetails[3]}\n"

                with open("allBooks.csv", "w") as allBooksFile:
                    allBooksFile.writelines(content)

                print("Book updated successfully.")

            else:
                print("Invalid option.")

        else:
            print("No book found.")