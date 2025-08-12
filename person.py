
# person = {
# "name": "Alice",
# "age": 30,
# "city": "Berlin"
#  }
# print (person ["name"])
# person ["email"] = "abc@xyz.com"
# person ["age"] = 35
# person ["number"] = 111
# del person ["number"]

# print ("age" in person)

# print (person)
# print (person.keys())
# print (person.values())

# user1 = {
#         'name': 'Yusuf',
#         'age': 35,
#         'location': 'DE',
#         'jobs': 'SysAd',
#         'experience': '6 years',
#         'certified': True
#         }
# print (user1)
# print (user1 ['jobs'])
# print (user1 ['name'])


# age = 17
# if age >= 18:
#     print ('na adult you be')

# else:
#     print ('u be minor')

# score = 78

# if score >= 70:
#     print ('A')

# elif score >= 60:
#     print ('B')

# elif score >= 50:
#     print ('C')

# elif score >= 45:
#     print ('D')

# else:
#     print ('F')


# languages = ["Python", "Java", "C++"]

# for items in languages:
#     print (items)


# for things in person:
#     print (things)


# tools = ["AWS", "Azure", "Slack"]

# for tool in tools:
#     print(tool)


# languages = ["Python", "Java", "C++"]

# for lang in languages:
#     print(lang)



# for classes in range (1,10):
#     print ('Class',classes)

# for apple in range(1, 6):
#     print("Check apple", apple)



# classez = 1

# while classez <= 5:
#     print ('classe', classez)

#     classez += 1

# tools = ["AWS", "Azure", "Slack"]


# for tool in tools:
#     print ('Now Checking', tool)
#     print ('Done Checking')

# def greet ():
#     print('Hello!')

# greet()

# def welcome_message ():
#     print ('Welcome to the IT Support')

# welcome_message ()
# welcome_message ()
# def greet_user (name):
#     print('Hello', name)
    
# greet_user('Yusuf')

# def it_support_ticket (name):
#     print('Ticket opened for', name)
    
# it_support_ticket('Yusuf')
# it_support_ticket('Bello')


# def add2numbers (a,b):
#     return a + b

# result = add2numbers (10,20)
# print (result)

# def years_to_days(years):
#     return years * 365

# # Call the function and store results
# days_2_years = years_to_days(2)
# days_5_years = years_to_days(5)

# # Print results
# print(days_2_years)
# print(days_5_years)

# word = 'mango'
# reversed_word = word [::-1]

# print (reversed_word)

# def minutes_to_seconds(minutes):
#     return minutes * 60

# print (minutes_to_seconds(3))
# print (minutes_to_seconds(10))



# # word = 'mango'
# # reversed_word = word [::-1]

# # print (reversed_word)


# student_name = ['Ade', 'Ola', 'Bola', 'shola', 12345,]

# print(student_name[3])

# student_name.append("Bayo")
# student_name.remove("Bayo")
# ---------------------------------------------------------------------------

# even_odd_no = [3,6,9,12,15,18,21]
# for values in even_odd_no:
#     if values == 3:
#         print ('3 is odd number')
#     elif values == 6:
#         print ('6 is even number')
#     elif values == 9:
#         print ('9 is odd number')
#     elif values == 12:
#         print ('12 is even number')
#     elif values == 15:
#         print ('15 is odd number')
#     elif values == 18:
#         print ('18 is even number')
#     elif values == 21:
#         print ('21 is odd number')
#     else:
#         print ('that is all')

# -----------------------------------------------------------------------
# even_odd_no = [3,6,9,12,15,18,21]

# for number in even_odd_no:
#     if number % 2 == 0:
#         print(number, 'is an even number')
#     else:
#         print(number, 'is an odd number')


# for index,number in enumerate (even_odd_no):
#     print (f"{number} is in {index}")


# for index,number in enumerate(even_odd_no):
#     if number % 2 == 0:
#         print (f'{number} is an even number in index {index}')
#     else:
#         print (f'{number} is an odd number in index {index}')
# -----------------------------------------------------------------------
# student_score = int(input('Enter your score: '))

# if student_score <= 39:
#     print('You have failed the course and need to re-sit the exam.')
# elif student_score <=49:
#     print("Your grade is `D`")
# elif student_score <=59:
#     print("Your grade is `C`")
# elif student_score <=69:
#     print("Your grade is `B`")
# elif student_score >= 70:
#     print("Your grade is `A`")
# else:
#     print('Invalid input')
# ------------------------------------------------------------------
# student_score = float(input('Enter your score: '))

# if student_score in range(0,40):
#     print('You have failed the course and need to re-sit the exam.')
# elif student_score in range(40,50):
#     print("Your grade is `D`")
# elif student_score in range(50,60):
#     print("Your grade is `C`")
# elif student_score in range(60,70):
#     print("Your grade is `B`")
# elif student_score in range(70,101):
#     print("Your grade is `A`")
# else:
#     print('Invalid input')
# ---------------------------------------------------------

# student_score = float(input('Enter your score: '))
    
# if student_score < 0 or student_score > 100:
#         print('Invalid input! Score must be between 0 and 100.')
# elif student_score <= 39:
#         print('You have failed the course and need to re-sit the exam.')
# elif 40 <= student_score <= 49:
#         print("Your grade is `D`")
# elif 50 <= student_score <= 59:
#         print("Your grade is `C`")
# elif 60 <= student_score <= 69:
#         print("Your grade is `B`")
# elif student_score >= 70:
#         print("Your grade is `A`")
# else:
#     print('Invalid input! Please enter a numeric score.')
# ------------------------------------------------------------------

# days = ['Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# user_input = input('Enter day of the week: ').capitalize

# if user_input == days[0]:
#         print ('Ojo Aje')
# elif user_input == days[1]:
#         print ('Ojo Isegun')
# elif user_input == days[2]:
#         print ('Ojoru')
# elif user_input == days[3]:
#         print ('Ojobo')
# elif user_input == days[4]:
#         print ('Ojo eti')
# elif user_input == days[5]:
#         print ('Ojo abameta')
# elif user_input == days[6]:
#         print ('Ojo Aiku')
# else:
#         print('Thats not a valid day in the English language.')

# ---------------------------------------------------------------------------

# cost = float(input('How much money do you intend to spend at the store sale: '))

# if cost < 75:
#         print ('You receive no discount')
# elif cost >= 75 and cost <100:
#         new_cost1 = float(cost*0.15)
#         print (f"You receive 15'%' discount. Your discount is {new_cost1}. Please pay {cost - new_cost1}")
# elif cost >= 100 and cost <150:
#         new_cost2 = float(cost*0.25)
#         print (f"You receive 25'%' discount. Your discount is {new_cost2}. Please pay {cost - new_cost2}")
# elif cost >= 150 :
#         new_cost3 = float(cost*0.35)
#         print (f"You receive 35'%' discount. Your discount is {new_cost3}. Please pay {cost - new_cost3}")
# else:
#         print ('Error')

# -------------------------------------------------------------------------------
# x = -567
# x = str(x)
# reversed_x = x[ : : -1]
# if reversed_x.endswith('-'):
#     reversed_x2 = reversed_x[0:-1]
#     result = '-' + reversed_x2
# # else:
# #     reversed_x = x[ : : -1]
# print(result)

# # --------------------------------------------------------------------

# x = int(input('Number = '))
# x = str(x)
# reversed_x = x[ : : -1]
# if reversed_x.endswith('-'):
#     reversed_x2 = reversed_x[0:-1]
#     result = '-' + reversed_x2
# else:
#     result = reversed_x

# print(int(result))

# --------------------------------------------------------------
# x = int(input('Number = '))
# x = str(x)
# reversed_x = x[ : : -1]
# if reversed_x.endswith('-'):
#     reversed_x2 = reversed_x[0:-1]
#     result = '-' + reversed_x2
# else:
#     result = reversed_x

# if -2_147_483_648 <= int(result) <= 2_147_483_647:
#     print (0)

# print(int(result))

# x = int(input('Number = '))
# x_str = str(x)
# reversed_x = x_str[::-1]

# if reversed_x.endswith('-'):
#     reversed_x = '-' + reversed_x[:-1]

# result = int(reversed_x)

# if -2_147_483_648 <= result <= 2_147_483_647:
#     print(result)
# else:
#     print(0)

# def reverse(x: int) -> int:
#     INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
#     sign = -1 if x < 0 else 1
#     x_abs = abs(x)
    
#     reversed_num = 0
#     while x_abs != 0:
#         digit = x_abs % 10
#         x_abs //= 10
        
#         # Check overflow before adding the next digit
#         if (reversed_num > INT_MAX // 10 or 
#            (reversed_num == INT_MAX // 10 and digit > 7)):
#             return 0
        
#         reversed_num = reversed_num * 10 + digit
    
#     return sign * reversed_num


# x = str(-121)
# rx = x[ : : -1]
# if x == rx:
#     print (True)
# else:
#     print (False)

# s = "Hello World"
# s = s.strip()
# s = s.split(' ')
# result  = len(s[-1])
# print (result)

# s = 
# I:1
# V:5
# X:10
# L:50
# C:100
# D:500
# M:1000


# start = int(input('Start from: '))
# stop = int(input('stop at: '))
# prime_numbers = list(range(start,stop))
# for num in prime_numbers:
#     if num / 1 == num and num / num == 1:
#         print (num)

# stop = int(input('stop at: '))
# for nom in range(2, stop):


# numbers1_21 = range(1, 21)
# numbers1_12 = range(1, 13)
# # given_number = given_number * int(range(1, 13))
# for each_num in numbers1_21:
#     for every_num in numbers1_12:
#         result = each_num * every_num
#         print(f'{each_num} x {every_num} = {result}')

# # abc = range(0,9)
# for i in range(0,9):
#     print (i)


# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')


# status = 4180
# match status:
#     case 400:
#         print( "Bad request")
#     case 404:
#         print ("Not found")
#     case 418:
#         print ("I'm a teapot")
#     case _:
#         print ("Something's wrong with the internet")


# number = 12345
# while not number == 112233:
#     print ("continue counting")

'''
Create a program that allows the user to guess your secret number between 1 and 100. 
The program should keep prompting the user until they guess the correct number. If they guess your number correctly, 
tell them congratulations and terminate the program but if they are unable to guess your secret number after 10 tries, 
you should tell them they failed and terminate the program.
'''
# import random
# secret_number = int(random.randint(1, 100))
# input_number = int(input('Type in your lucky number:  '))
# correct_number = secret_number == input_number
# while input_number != secret_number:
#     input_number = int(input('Type in your lucky number:  '))
#     print('Incorrect guess')
#     if input_number == secret_number:
#         print('Congratulations. Correct guess!!!')
#         break

# -----------------------------


# # import random
# secret_number = 75
# input_number = int(input('Type in your lucky number:  '))
# while input_number not in range(1,101):
#     print('num must be 1 to 100')
#     input_number = int(input('Type in your lucky number:  '))
# mumber_of_attemps = 1

# if secret_number == input_number:
#         print('Congratulations. Correct guess!!!')
# else:
#     while input_number != secret_number:
#         input_number = int(input('Type in your lucky number again:  '))
#         mumber_of_attemps += 1
#         while input_number not in range(1,101):
#             print('num must be 1 to 100')
#             input_number = int(input('Type in your lucky number:  '))
#         if mumber_of_attemps >= 10:
#             print('the end!!!')
#             break

# ------------------------------------

'''
Write a basic login program in Python that takes in a username and a password.
Your programs database is a Python dictionary containing all usernames and their respective passwords.
Your program should start by asking the user for their username and then ask the user for their password.
If the username exists in your database and the password they provide is the same as the password attributed to their 
username in your database, the system should print a message saying their login was successful and exit.
If the username exists in your database but the password they provide is incorrect, the system should continue prompting 
them to provide the correct password and once they provide the correct password, they should receive the login message. 
If, however, l they provide an incorrect password 5 times, the system should show a message saying their account has been suspended for 24 hours.
If they provide a username that does not exist in your database, they should receive a message saying ”Invalid User”.
'''

# username = input('Username: ')
# password = input('Password: ')
# usernames_and_passwords = {
#     "user1": "pass1",
#     "user2": "pass2",
#     "user3": "pass3",
#     "user4": "pass4",
#     "user5": "pass5",
#     "user6": "pass6",
#     "user7": "pass7",
#     "user8": "pass8",
#     "user9": "pass9",
#     "user10": "pass10"
# }
# attempts = 0

# if usernames_and_passwords[username] == password:
#         print ('login was successful')
    
# while usernames_and_passwords[username] != password:
#     if usernames_and_passwords[username] != password:
#         print ('provide the correct password')
        
#     password = input('Password: ')
    

#     attempts += 1
          
#     if usernames_and_passwords[username] == password:
#         print ('login was successful')

#     if attempts >= 5:
#         print ('Your account has been suspended for 24 hours...')

#     if username not in usernames_and_passwords:
#         print ('Invalid User')
#         break

'''Write a python program that takes a list of numbers and creates a new list of numbers 
where every item in the new list is the square of each item in the initial list.
'''

# list_of_num1 = list(range(1, 20, 2))
# list_of_num2 = []
# for items in list_of_num1:
#     list_of_num2.append(items **2)
#     print (list_of_num2)


# '''
# Write a python program that takes a list of numbers and creates a new list of numbers 
# where for every number in the new list if the number is even in the old list, 
# divide it by 2, and if the number is odd, multiply it by 2 

# e.g. 
# old_list = [1,2,3,4,5,6,7,8,9,10]
# new_list = [1,1,6,2,10,3,14,4,18,5]
# list_of_num1 = list(range(1, 21))
# list_of_num2 = []

# for num in list_of_num1:
#     if num % 2 == 0:
#         list_of_num2.append(int(num / 2))
#     elif num % 2 != 0:
#         list_of_num2.append(int(num * 2))
# # print (list_of_num1)
# # print (list_of_num2)

# set_comprh = {int(num / 2) if num % 2 == 0 else int(num * 2)  for num in list_of_num1}

# print (set_comprh)
# '''
# Create a list of numbers from 1 to 20 and then create
# a set of those numbers where each number in the set
# is each number in the list multiplied by 10
#  '''

# list_of_nums = list(range(1,21))
# set_of_nums = set()
# for every_num in list_of_nums:
#     set_of_nums.add(every_num * 10)
# print(set_of_nums)

# set_comp = {every_num * 10 for every_num in list_of_nums}
# print (set_comp)

'''numbers1_to_20 = list(range(1, 21))
"""
We want to create a dict that looks like this from the list we have above.
{
1: "odd",
2: "even",
3: "odd"
}'''

# numbers1_to_20 = list(range(1, 21))

# for every_num in numbers1_to_20:
#     if every_num % 2 == 1:
#         print (dict(f'{every_num}: odd'))
#     elif every_num % 2 == 0:
#         print (dict(f'{every_num}: even'))
    
numbers1_to_20 = list(range(1, 21))

num_dict = {}

for every_num in numbers1_to_20:
    if every_num % 2 != 0:
        num_dict[every_num] = "odd"
    else:
        num_dict[every_num] = "even"
# print (num_dict)

'''From the now populated num_dict, using a for loop, 
create a new dictionary called "evens_and_odds" such that 
the new dictionary shall now look like the below dict
{
"odd": [1,3,5,7,9,11,13,15,17,19],
"even": [2,4,6,8,10,12,14,16,18,20]'''

import pprint
evens_and_odds = {'odd': [], 'even': []}
for key in num_dict:
    if num_dict[key] == "odd":
        evens_and_odds['odd'].append(key)
    else:
        evens_and_odds['even'].append(key)
# pprint.pprint(evens_and_odds)


numbers1_to_20 = list(range(1, 21))
numbers_dict = {'even':[] , 'odd':[]}
for numbers in numbers1_to_20:
    if numbers % 2 == 0:
        numbers_dict['even'].append(numbers)
    else:
        numbers_dict['odd'].append(numbers)
pprint.pprint(numbers_dict)