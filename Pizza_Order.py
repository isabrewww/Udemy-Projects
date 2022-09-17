print("Welcome to Brewster Pizza Deliveries!")

pizzaSize = input("What size pizza would you like? S, M, or L: ").lower()
pepperoni = input("Would you like to add pepperoni? Y or N: ").lower()
extraCheese = input("Would you like extra cheese? Y or N: ").lower()
bill = 0

if pizzaSize == "s":
    bill += 15
elif pizzaSize == "m":
    bill += 20
elif pizzaSize == "l":
    bill += 25

if pepperoni == "y":
    if pizzaSize == "s":
        bill += 2
    else:
        bill += 3

if extraCheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")
