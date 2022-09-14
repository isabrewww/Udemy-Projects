import random

def main():

    letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the Password Generator!\n")

    while True:
        nr_letters_lower = input("How many LOWER-CASE LETTERS would you like in your password?\n\n")
        if (nr_letters_lower).isnumeric() == False:
            print("INVALID INPUT\n")
        else:
            break
    while True:
        nr_letters_upper = (input("\nHow many UPPER-CASE LETTERS would you like?\n\n"))
        if (nr_letters_upper).isnumeric() == False:
            print("INVALID INPUT\n")
        else:
            break
    while True:
        nr_symbols = (input(f"\nHow many SYMBOLS would you like?\n\n"))
        if (nr_symbols).isnumeric() == False:
            print("INVALID INPUT\n")
        else:
            break
    while True:
        nr_numbers = (input(f"\nHow many NUMBERS would you like?\n\n"))
        if (nr_numbers).isnumeric() == False:
            print("INVALID INPUT\n")
        else:
            break
    
    password = []

    for l in range(0, int(nr_letters_lower)):
        password.append(random.choice(letters_lower))

    for l in range(0, int(nr_letters_upper)):
        password.append(random.choice(letters_upper))

    for s in range(0, int(nr_symbols)):
        password.append(random.choice(symbols))

    for n in range(0, int(nr_numbers)):
        password.append(random.choice(numbers))

    length = len(password)
    # this will ask the user if they are happy with the number of characters, and ensure they provide valid input.
    while True:
        verify = input(f"\nYour password will be {length} characters long. Is this okay? Y/N:\n\n").upper()
        if verify == "N":
            main()
            break
        elif verify == "Y":
            random.shuffle(password)
            password = ''.join(password)
            print(f"\nYour password is:\n\n{password}\n")
            break
        else:
            print("INVALID INPUT\n")

if __name__ == '__main__':
    main()