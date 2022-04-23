import math


def is_perfect_square(x):
    # if x is perfect square
    s = int(math.sqrt(x))
    return s * s == x


def is_fibonacci(n):
    # if n is a Fibonacci Number
    # if one of 5*n*n + 4 or 5*n*n - 4 or both is a perfect square
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


def welcome_menu():
    print("Welcome to the Fibonacci Series number checker.")
    start()


def start():
    while True:
        try:
            # Ask user to enter number
            number = int(input("Please enter a number: "))
            break
        except ValueError:
            # Exception if a user doesn't input an integer
            # User is asked to enter an integer
            print("Please try again. That wasn't an integer.")
    if is_fibonacci(number):
        print(number, "is a Fibonacci Number")
    else:
        print(number, "is a not Fibonacci Number")
    menu()


def menu():
    choice = input("""
    Would you like to test another number?
    1 YES
    2 NO
    Enter choice: """)
    if choice.upper() == "YES" or choice == "1":
        start()
    elif choice.upper() == "NO" or choice == "2":
        quit()
    else:
        print("Please enter a valid choice")
        menu()


welcome_menu()
