shopping_list = []

while True:
    choice = input("1 add, 2 remove, 3 show, 4 clear, 0 quit: ")

    if choice == "1":
        item = input("Item: ").strip().lower()

        if item not in shopping_list:
            shopping_list.append(item)
        else:
            print("Item already exists")

    elif choice == "2":
        item = input("Item: ").strip().lower()

        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("Not in the list")

    elif choice == "3":
        if len(shopping_list) == 0:
            print("Shopping list is empty")
        else:
            for i, item in enumerate(sorted(shopping_list), start=1):
                print(f"{i}. {item}")

    elif choice == "4":
        shopping_list.clear()
        print("Shopping list cleared")

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")