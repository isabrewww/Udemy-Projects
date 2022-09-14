# This program will choose a name from a list at random.

import random

initial_names = input("Give me everybody's name, seperated by a comma and a space (\", \"):\n")
names = initial_names.split(", ")
result = random.choice(names)

print("")
input("And the winner is... Press ENTER to continue\n") 
print(f"{result.upper()}!!!!")


# could also be written like this if you want to try without the "random.choice" function:

# initial_names = input("Give me everybody's name, seperated by a comma and a space (\", \"):\n")
# names = initial_names.split(", ")
# result = len(names)
# random_choice = random.randint(0, result - 1)