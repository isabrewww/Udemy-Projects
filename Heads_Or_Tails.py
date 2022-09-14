import random

print("\nWelcome to the coin toss!\n")

headsOrTails = int(input("Will you choose heads or tails? (1) HEADS (2) TAILS:\n"))
toss = random.randint(1,2)
print("")

if toss == 1:
    print("It is HEADS!")
else:
    print("It is TAILS!")
print("")

if toss == headsOrTails:
    print("You WON the toss!")
else:
    print("You LOST the toss...")