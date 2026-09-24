user_number = 0
highest_number = 0

for number in range(3):
    user_number = int(input("Enter number " + str(number + 1) + ": "))
    if user_number > highest_number:
        highest_number = user_number

print(f"The highest number entered is: {highest_number}")