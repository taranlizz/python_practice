import api


def main():
    balance = 0
    is_running = True

    while is_running == True:
        print("Banking Program")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit the program\n")

        choice = input("Enter the operation number (1-4): ")

        match choice:
            case "1":
                api.show_balance(balance)
            case "2":
                balance = api.deposit(balance)
            case "3":
                balance = api.withdraw(balance)
            case "4":
                print("Exiting the program...")
                is_running = False
            case _:
                print("Invalid operation type\n")


if __name__ == "__main__":
    main()
