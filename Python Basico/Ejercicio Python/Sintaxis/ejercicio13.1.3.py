user_number = int(input("Enter a number: "))
counter_user_number = 1
final_sum = 0

while counter_user_number <= user_number:
    final_sum += counter_user_number
    counter_user_number += 1

print(f"The sum of all numbers from 1 to {user_number} is: {final_sum}")
