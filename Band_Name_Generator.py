# This program generates a band name based off of the city the user grew up in, and the name of their pet

# Greeting
print("Welcome to the band name generator!")

# Get user input
city_name = input("What city did you grow up in?\n")
pet_name = input("What is the name of your pet?\n")

# Generate band name
band_name = (city_name + " " + pet_name)
print("Your band name could be:\n" + band_name)