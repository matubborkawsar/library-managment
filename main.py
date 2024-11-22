import  add, remove, update, view
print("Welcome")

while True:
    print(f"\n1. Add a book")
    print("2. Remove a book")
    print("3. Update a book")
    print("4. view all books")
    print("0. Exit")

    option = int(input("Choose an option : "))

    if option == 1:
        add.add()

    elif option == 2:
        remove.remove()

    elif option == 3:
        update.update()

    elif option == 4:
        view.view()

    elif option == 0:
        print("Thank you.")
        break

    else:
        print("Invalid option. Try 1,2,3,4 or 0")