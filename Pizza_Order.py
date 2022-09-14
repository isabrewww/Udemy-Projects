print("Welcome to Brewster Pizza Deliveries!")

pizzaSize = input("What size pizza would you like? S, M, or L: ")
pepperoni = input("Would you like to add pepperoni? Y or N: ")
extraCheese = input("Would you like extra cheese? Y or N: ")
bill = 0

if pizzaSize == "s" or pizzaSize == "S":
    bill += 15
elif pizzaSize == "m" or pizzaSize == "M":
    bill += 20
elif pizzaSize == "l" or pizzaSize == "L":
    bill += 25

if pepperoni == "y" or pepperoni == "Y":
    if pizzaSize == "s" or pizzaSize == "S":
        bill += 2
    else:
        bill += 3

if extraCheese == "y" or extraCheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")