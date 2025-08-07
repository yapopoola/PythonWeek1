# days = {
#     'Monday': 'Ojo Aje', 
#     'Tuesday': 'Ojo Isegun', 
#     'Wednesday': 'Ojoru', 
#     'Thursday': 'Ojobo', 
#     'Friday': 'Ojo eti', 
#     'Saturday': 'Ojo abameta', 
#     'Sunday': 'Ojo Aiku'
# }

# user_input = input('Enter day of the week: ').capitalize()

# print(days.get(user_input, "No such day exist in the English Language."))


"""
Write Python code that asks a user how much money they intend to spend at the store sale.
If they spend less than $75, they receive no discount.
If the user spends $75 or more, they receive 15% off.
If the user spends $100 or more, they receive 25% off.
If the user spends $150 or more, they receive 35% off (with a maximum discount of $100).
In each case, print the amount the user would pay after the discount has been applied.
"""
 
# cost = round(float(input('How much money do you intend to spend at the store sale: ')), 2)

 
# if cost < 75:  
#     answer = "You receive no discount"

# elif cost >= 75 and cost < 100:
#     discount = round(cost * 0.15, 2)
#     answer = f"You receive 15% discount. Your discount is {discount}. Please pay {cost - discount}"

# elif cost >= 100 and cost < 150:
#     discount = round(cost * 0.25, 2)
#     answer = f"You receive 25% discount. Your discount is {discount}. Please pay {cost - discount}"

# elif cost >= 150:
#     calculated_discount = cost * 0.35
#     if calculated_discount > 100:
#         discount = 100
#     else:
#         discount = calculated_discount
        
#     answer = f"You receive 35% discount. Your discount is {discount: .2f}. Please pay {cost - discount: .2f}"

# else:
#     answer = 'Error'

# # print(answer)

"""
Write Python code that checks that a number is a prime number.
A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11)
If that number is prime, your code should print "The number {num} is prime number", otherwise if the number is not prime, print "The number {num} is NOT a prime number"
"""

import datetime
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
start_time = datetime.datetime.now()
print(f"code started running at {start_time}")

# my_num = int(input("What number do you want to check? "))   # e.g 11
# result = f"The number {my_num} is a prime number"


# if my_num == 0 or my_num == 1:
#     result = f"The number {my_num} is not a prime number"

# else:
#     for each_num in range(2, my_num):    # i.e. 2, 3, 4, 5, 6, 7, 8, 9
#         if my_num % each_num == 0:       # 11/2 = 0
#             result = f"The number {my_num} is not a prime number"
#             break
#         # else:  # meaning if the number did not divide our main number successfully.
#         #     continue

# print(result)

"""
Write the python code that when given a number, 
it prints out the multiplication table of that number
"""
# given_number = int(input('Given number is: '))
# for each_num in range(1, 13):
#     result = each_num * given_number
#     print(f'{given_number} x {each_num} = {result}')


numbers1_21 = range(1, 21)
numbers1_12 = range(1, 13)
for each_num in numbers1_21: 
    for every_num in numbers1_12:  
        result = each_num * every_num
        print(f'{each_num} x {every_num} = {result}')
    print()

end_time = datetime.datetime.now()
print(f"code stopped running at {end_time}")  
