# Program to check if a number is prime or not

def isPrimeNum():
    while True:
        try:
            # Ask user to enter number
            number = int(input("Please enter a number: "))
            break
        except ValueError:
            # Exception if a user doesn't input an integer
            # User is asked to enter an integer
            print("Please try again. That wasn't an integer.")

    # define a flag variable
    not_prime = False

    if number > 1:
        # check for factors
        for i in range(2, number):
            if (number % i) == 0:
                # if factor is found, set flag to True
                not_prime = True
                # break out of loop
                break
    # prime numbers are greater than 1
    else:
        not_prime = True

    # check if flag is True
    if not_prime:
        print(number, "is not a prime number")
    else:
        print(number, "is a prime number")
    # To menu
    menu()


def menu():
    choice = input("""
    Would you like to test another number?
    1 YES
    2 NO
    Enter choice: """)
    if choice.upper() == "YES" or choice == "1":
        isPrimeNum()
    elif choice.upper() == "NO" or choice == "2":
        quit()
    else:
        print("Please enter a valid choice")
        menu()


def welcome_menu():
    print("Welcome to the Prime Number checker.")
    isPrimeNum()


welcome_menu()
