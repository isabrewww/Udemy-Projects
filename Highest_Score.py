student_scores = input("Input a list of student scores:\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

high_score = 0
for score in student_scores:
    if high_score < score:
        high_score = score

print(f"The highest score in the class is: {high_score}")
