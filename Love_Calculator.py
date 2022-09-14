print("Welcome to the love calculator!\n")

name1 = input("Enter your name:\n").lower()
name2 = input("Enter their name:\n").lower()
combined_name = name1 + name2

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")

print(f"\nT occurs {t} times\n")
print(f"R occurs {r} times\n")
print(f"U occurs {u} times\n")
print(f"E occurs {e} times\n")

total_true = t + r + u + e

print(f"Total = {total_true}.\n")

print(f"L occurs {l} times\n")
print(f"O occurs {o} times\n")
print(f"V occurs {v} times\n")
print(f"E occurs {e} times\n")

total_love = l + o + v + e

print(f"Total = {total_love}.\n")

love_score = int(str(total_true) + str(total_love))

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos!")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your love score is {love_score}.")