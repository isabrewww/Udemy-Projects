# put input from user into a list
# convert from a string to an integer 
student_heights = input("Input a list of numbers:\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# use count to replace the len function
count = 0
total_height = 0
for height in student_heights:
    count += 1
    total_height += height
average_height = round(total_height / count, 2)

print(f"The average is:\n{average_height}")
