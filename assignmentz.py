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

# import datetime
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# start_time = datetime.datetime.now()
# print(f"code started running at {start_time}")

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


# numbers1_21 = range(1, 21)
# numbers1_12 = range(1, 13)
# for each_num in numbers1_21: 
#     for every_num in numbers1_12:  
#         result = each_num * every_num
#         print(f'{each_num} x {every_num} = {result}')
#     print()

# end_time = datetime.datetime.now()
# print(f"code stopped running at {end_time}")  



"""
Create a program that allows the user to guess your secret number between 1 and 100. 
The program should keep prompting the user until they guess the correct number. 
If they guess your number correctly, tell them congratulations and terminate the program 
but if they are unable to guess your secret number after 10 tries, 
you should tell them they failed and terminate the program.
"""
# import random

# my_num = random.randint(1, 10)

# their_num = int(input("Guess a number between 1 and 100: "))  # e.g. 20
# number_of_attempts = 1

# if their_num == my_num:
#     print("Congratulations! You guessed correctly.")

# else: 
#     while their_num != my_num:
#         number_of_attempts += 1
#         their_num = int(input(f"This is your {number_of_attempts}/10 attempts. Guess another number between 1 and 100: "))  # e.g. 40

#         if their_num == my_num:
#             print("Congratulations! You guessed correctly.")

#         if number_of_attempts >= 10:
#             print("Sorry, you have exceeded your limit. Better luck next time!")
#             break



# ------------------------------------
 
'''
Write a basic login program in Python that takes in a username and a password.
Your programs database is a Python dictionary containing all usernames and their respective passwords.
Your program should start by asking the user for their username and then ask the user for their password.
If the username exists in your database and the password they provide is the same as the password 
attributed to their username in your database, the system should print a message 
saying their login was successful and exit.
If the username exists in your database but the password they provide is incorrect, the system should continue prompting
them to provide the correct password and once they provide the correct password, they should receive the login message.
If, however, they provide an incorrect password 5 times, the system should show a message saying their account has been suspended for 24 hours.
If they provide a username that does not exist in your database, they should receive a message saying ”Invalid User”.
'''
user_db = {
    "user1": "pass1",
    "user2": "pass2",
    "user3": "pass3",
    "user4": "pass4",
    "user5": "pass5",
    "user6": "pass6",
    "user7": "pass7",
    "user8": "pass8",
    "user9": "pass9",
    "user10": "pass10"
}
attempts = 0

username = input('Please enter your username: ')
password = input('Please enter your password: ')
attempts += 1

if username in user_db.keys():
    # Check that the password is correct
    if password == user_db[username]:
        print("Login Successful")

    # Check if the password is incorrect and ask again.
    elif password != user_db[username]:
        while password != user_db[username]:
            password = input("Incorrect password, retry: ")
            attempts += 1

            if password == user_db[username]:
                print("Login Successful")
                break

            elif attempts == 5:
                print("Attempted the wrong password 5 times. Your account is now on 24hr hold.")
                break

elif password in user_db.values():
    print("Incorrect username provided!")
         