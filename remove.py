def remove():
    with open("allBooks.csv", "r") as allBooksFile:
        content = allBooksFile.readlines()

        if content:
            for index, item in enumerate(content):
                print(f"{index + 1}. {item.strip()}")

            removeBook = int(input("Choose a book to remove : "))

            if 1 <= removeBook <= len(content):
                content.pop(removeBook - 1)

                with open("allBooks.csv", "w") as allBooksFile:
                    allBooksFile.writelines(content)

                print("Book removed successfully.")

            else:
                print("Invalid option.")

        else:
            print("No book found.")