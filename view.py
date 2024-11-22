def view():
    with open("allBooks.csv", "r") as allBooksFile:
        content = allBooksFile.readlines()

        if content:
            for index, item in enumerate(content):
                print(f"{index + 1}. {item.strip()}")

        else:
            print("No book found.")