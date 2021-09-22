# Markhus Dammar
# 22 September 2021
# This program will take user input, append numbers to a list, and then find min and max

user_list = []

amt = int(input("How many numbers do you want in this list? >>>"))          # asks user how many values will be in list

for amt in range(0, amt):                                                   # appends list with each number inputted by user
    nums = input(f"Enter integer number {amt} >>>")
    user_list.append(nums)

print(user_list)                                                                        # prints list
print("the minimum is: " + min(user_list) + "\nthe maximum is: " + max(user_list))      # prints min/max
