# this will print the sum of every even number from 1 - 100 (including 1)
final = 1
for n in range (1, 101):
    if n % 2 == 0:
        final += n
print(final)