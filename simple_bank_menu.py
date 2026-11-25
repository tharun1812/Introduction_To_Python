balance = 0

while True:
    print("1) Deposit 2) Balance 0) Quit")

    choice = input("Choice: ")

    if choice == "1":
        amount = float(input("Amount: "))
        balance = balance + amount

    elif choice == "2":
        print(f"Balance: {balance:.2f} €")

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")