print("Welcome to: OH NO, IM LATE FOR WORK!\n")
print("Select the correct choices to the following questions to make it to work!\n")
print("Good luck!")  

print("\nYou overslept and are running late for work!")
call_or_go = input("Will you call in sick (1) or try to make it on time (2)? Enter 1 or 2: ")
if call_or_go == "2":
    car_or_bike = input("Will you take the car (1) or ride your bicycle (2)? Enter 1 or 2: ")
    if car_or_bike == "2":
        which_path = input("You're usual path is blocked by construction. Will you ride around it (1), turn left (2), or turn right (3)? Enter 1, 2, or 3: ")
        if which_path == "1":
            print("Congratulations, you made it to work on time!")
        elif which_path == "2":
            print("You rode out to the highway and got hit by a car!")
        elif which_path == "3":
            print("There was debris on the road and your tires popped!")
    else:
        print("Your spouse forgot to fill up the tank and you ran out of gas!")
else:
    print("You are out of sick days and got fired!")