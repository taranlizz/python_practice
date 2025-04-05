import math


def get_input():
    try:
        value = float(input("\nEnter the amount of money to perform the operation: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
        return 0

    if value <= 0:
        print("You cannot perform the operation with a negative or zero amount.\n")
        return 0

    return value


def show_balance(balance):
    print(f"\nYour balance is ${balance:.2f}\n")


def deposit(balance):
    value = get_input()

    if value == 0:
        return balance

    balance += value

    print(
        f"\nSuccess! You deposited ${value:.2f} on your account.\nYour current balance is ${balance:.2f}\n"
    )

    return balance


def withdraw(balance):
    value = get_input()

    if value == 0:
        return balance

    if value > balance:
        print("Insufficient funds\n")
        return balance

    balance -= value

    print(
        f"\nSuccess! You withdrew ${value:.2f} from your account.\nYour current balance is ${balance:.2f}\n"
    )
    return balance
