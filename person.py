
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

def greet ():
    print('Hello!')

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
    
# numbers1_to_20 = list(range(1, 21))

# num_dict = {}

# for every_num in numbers1_to_20:
#     if every_num % 2 != 0:
#         num_dict[every_num] = "odd"
#     else:
#         num_dict[every_num] = "even"
# # print (num_dict)

# '''From the now populated num_dict, using a for loop, 
# create a new dictionary called "evens_and_odds" such that 
# the new dictionary shall now look like the below dict
# {
# "odd": [1,3,5,7,9,11,13,15,17,19],
# "even": [2,4,6,8,10,12,14,16,18,20]'''

# import pprint
# evens_and_odds = {'odd': [], 'even': []}
# for key in num_dict:
#     if num_dict[key] == "odd":
#         evens_and_odds['odd'].append(key)
#     else:
#         evens_and_odds['even'].append(key)
# pprint.pprint(evens_and_odds)


# numbers1_to_20 = list(range(1, 21))
# numbers_dict = {'even':[] , 'odd':[]}
# for numbers in numbers1_to_20:
#     if numbers % 2 == 0:
#         numbers_dict['even'].append(numbers)
#     else:
#         numbers_dict['odd'].append(numbers)
# pprint.pprint(numbers_dict)


# tuple_example = range(1, 10)
# # for t in tuple_example:
#     # print(t * 2)

# t_e = tuple( t  for t in tuple_example)
# print(t_e)

# '''
# Given a string name, generate a dictionary that shows each character in that string and their respective counts as the values.
# For example, if name is Yusufu, your generated dict should be 
# Python'''
# {
#     "Y": 1,
#     "u": 3,
#     "s": 1,
#     "f": 1
# }

# name = input('Type your name: ')
# name_dict = {}

# for alphabet in name:
#     # finding the alphabet for the first time, add to the new dict
#     if alphabet not in name_dict.keys():
#         name_dict[alphabet] = 1
            
#     # finding the alphabet for the subsequent times, add to the new dict(alphabet) e.g each alphabet
#     else:
#         name_dict[alphabet] += 1

# print(name_dict)


student_info = {
    "Gabriella": 5,
    "Paul": 20,
    "Jack": 3,
    "Bond": 1,
    "Ahmed": 10,
    "Tiara": 2,
    "Kaitlyn": 6,
    "Lucy": 4
}

# students_activeness = student_info.copy()

# for student_name in students_activeness:
#     if students_activeness[student_name] > 5:
#         students_activeness[student_name] = 'active'
#     else:
#         students_activeness[student_name] = 'inactive'

# print(students_activeness)



# students_activeness = student_info.copy()

# for student_name, days_since_last_login in students_activeness.items():
#     if days_since_last_login > 5:
#         students_activeness[student_name] = 'active'
#     else:
#         students_activeness[student_name] = 'inactive'


# students_activeness1 = {student_name:'active' if days_since_last_login > 5  else 'inactive'  for student_name, days_since_last_login in student_info.items() }
# # {'Gabriella': 'inactive', 'Paul': 'active', 'Jack': 'inactive', 'Bond': 'inactive', 'Ahmed': 'active', 'Tiara': 'inactive', 'Kaitlyn': 'active', 'Lucy': 'inactive'}
# active_students = {student_name:'active'  for student_name in students_activeness1 if students_activeness1[student_name] == 'active'}
# inactive_students =  {student_name:'inactive'  for student_name in students_activeness1 if students_activeness1[student_name] == 'inactive'}

# active_students_vR = {name: activeness for name, activeness in students_activeness1.items() if activeness == "active"}

# actives = {}
# for name, activeness in students_activeness1.items():
#     if activeness == "active":
#         actives[name] = activeness
# print(actives)

# print(active_students)
# print(inactive_students)
# print(students_activeness1)



# print(student_info)

# students_activeness = {}

# for student_name in student_info:
#     if student_info[student_name] > 5:
#         students_activeness[student_name] = 'active'
#     else:
#         students_activeness[student_name] = 'inactive'

# print(students_activeness)
# # print(student_info)


# student_name : is_active
# print(days_since_last_login)

# def narcissistic(number):
#     number = str(number)
#     total_num = 0
#     # want to check if the number would be equal to itself, if yes then return true
#     for num in number:
#         number_power = int(num) ** len(number)
#         total_num += number_power
#     print(total_num)
#     if total_num == int(number):
#         return True
#     # want to check if the number would not be equal to itself, if yes then return false
#     else:
#         return False
    
    
# print(narcissistic(7))

def summation(num):
    output = 0
    for every_num in range(1, num+1):
        output += every_num
    return output

# print(summation(9))
    

# def to_alternating_case(string: str):
#     new_str = ""
#     for every_letter in string:
#         if every_letter.lower():
#             return new_str.upper
#         elif every_letter.upper():
#             return every_letter.lower()
#         return every_letter


    

# def to_alternating_case(string: str):
#     new_str = ""
#     for every_char in string:
#         # if that char is lower, add its upper version to new string.
#         if every_char == every_char.lower():
#             new_str = new_str +  every_char.upper()
#         else:
#             new_str = new_str + every_char.lower()
    
#     return new_str


# def to_alternating_case(string: str):
#     string = list(string)
#     for index in range(0, len(string)):
#         if string[index] == string[index].lower():
#             string[index] = string[index].upper()
#         else:
#             string[index] = string[index].lower()

#     return "".join(string)


# print(to_alternating_case("hello wORld"))


# def unusual_five():
#     my_dict = {"five" : 5}
#     return my_dict["five"]

'''
Two objects that return a one word name in response to the first letter of the first name and one for the first letter of the surname are already given. 
See the examples below for further details.
If the first character of either of the names given to the function is not a letter from A - Z, you should return "Your name must start with a letter from A - Z."
Sometimes people might forget to capitalize the first letter of their name so your function should accommodate for these grammatical errors.'''
# These two dictionaries are preloaded, you need to use them in your code
# FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache'}
# SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst'}

# # alias_gen('Larry', 'Brentwood') == 'Logic Bomb'
# # alias_gen('123abc', 'Petrovic') == 'Your name must start with a letter from A - Z.'

# # from preloaded import FIRST_NAME, SURNAME



# def alias_gen(f_name: str, l_name: str) -> str:
#     f_name = f_name.capitalize() 
#     l_name = l_name.capitalize()
#     if f_name[0] in FIRST_NAME.keys() and l_name[0] in SURNAME.keys():
#         return f'{FIRST_NAME[f_name[0]]} {SURNAME[l_name[0]]}'
    
#     else:
#         return "Your name must start with a letter from A - Z."
            

# print(alias_gen("ade", "bayo"))

# def hex_to_dec(s):
#     s = int(s, base=16) 
#     return s
''''Your task is to find the first element of an array that is not consecutive.

By not consecutive we mean not exactly 1 larger than the previous element of the array.

E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's the first non-consecutive number.

If the whole array is consecutive then return null2.

The array will always have at least 2 elements1 and all elements will be numbers. 
The numbers will also all be unique and in ascending order. The numbers could be positive or negative and the first non-consecutive could be either too!'''

arr = [1,2,3,4,5,7,8,9,11]
arr_2 = []
# def first_non_consecutive(arr):
#     cons = True
#     for every_num in arr:
#         if arr[0] + 1 == arr[1]:
#     else:
#         every_num != cons
    # print(every_num)

''''Write a function which calculates the average of the numbers in a given array.

Note: Empty arrays should return 0.'''

# def find_average(numbers):
#     if numbers != []:
#         average_number = sum(numbers)/len(numbers)
#         return average_number
#     else:
#         return 0
    

# def find_average(numbers: list) -> int | float:
#     try:
#         average = sum(numbers) / len(numbers)    
#         return average
#     except:
#         return 0
    

# def find_average(numbers):
#     if numbers:
#         average = sum(numbers) / len(numbers)    
#         return average
#     else:
#         return 0

# print(find_average(arr_2))

'''When it's spring Japanese cherries blossom, it's called "sakura" and it's admired a lot. The petals start to fall in late April.

Suppose that the falling speed of a petal is 5 centimeters per second (5 cm/s), and it takes 80 seconds for the petal to reach the ground from a certain branch.

Write a function that receives the speed (in cm/s) of a petal as input, and returns the time it takes for that petal to reach the ground from the same branch.

Notes:

The movement of the petal is quite complicated, so in this case we can see the velocity as a constant during its falling.
Pay attention to the data types.
If the initial velocity is non-positive, the return value should be 0
            test.assert_approx_equals(sakura_fall(5), 80)
            test.assert_approx_equals(sakura_fall(10), 40)
            test.assert_approx_equals(sakura_fall(-1), 0)'''

# def sakura_fall(speed):
#     if speed < 0:
#         return 0
#     else:
#         time_taken = 400 / speed
#         return time_taken
    
'''Remove First and Last Character
Task
Your goal is to write a function that removes the first and last characters of a string. You're given one parameter, the original string.

Important: Your function should handle strings of any length ≥ 2 characters. For strings with exactly 2 characters, return an empty string.

Examples
'eloquent' --> 'loquen'
'country'  --> 'ountr' 
'person'   --> 'erso'
'ab'       --> '' (empty string)
'xyz'      --> 'y'
Requirements
The input string will always have at least 2 characters
For strings with exactly 2 characters, return an empty string
For strings with 3 or more characters, remove the first and last character
The function should handle strings containing letters, numbers, and special characters'''

# def remove_char(string_given):
#     if len(string_given) == 2:
#         return ""
#     if len(string_given) >= 3:
#         return string_given[1:-1]

# print(remove_char('string!000444'))

'''2(lw + wh + lh)
Write a function that returns the total surface area and volume of a box.

The given input will be three positive non-zero integers: width, height, and depth.

The output will be language dependant, so please check sample tests for the corresponding data type, (list, tuple, struct, query, etcetera).
'''

# def get_size(w,h,l):
#     TSA = 2 * (l*w + w*h + l*h)
#     VB = l * h * w
#     return [TSA, VB]

# print(get_size(7,17,111))

'''You are given two sorted arrays that contain only integers. These arrays may be sorted in either ascending or descending order. 
Your task is to merge them into a single array, ensuring that:

The resulting array is sorted in ascending order.

Any duplicate values are removed, so each integer appears only once.

If both input arrays are empty, return an empty array.

No input validation is needed, as both arrays are guaranteed to contain zero or more integers.

Examples (input -> output)
* [1, 2, 3, 4, 5], [6, 7, 8, 9, 10] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

* [1, 3, 5, 7, 9], [10, 8, 6, 4, 2] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

* [1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12] -> [1, 2, 3, 4, 5, 7, 9, 10, 11, 12]
Happy coding!'''
# arr1 = [11,33, 21, 3, 4, 5]
# arr2 = [33, 7, 2, 9, 10, 3]

# def merge_arrays(arr1, arr2):
#     '''create an empty array where it will be merged
#     add both arrays to the empty array
#     change it to set to remove duplication
#     then sort in ascending order'''
#     arr3 = arr1 + arr2
#     arr3 = set(arr3)
#     arr3 = list(arr3)
#     arr3.sort()
#     return arr3

# print(merge_arrays(arr1, arr2))

'''When provided with a number between 0-9, return it in words. Note that the input is guaranteed to be within the range of 0-9.
Input: 1
Output: "One".
If your language supports it, try using a switch statement.
'''

# def switch_it_up(number):
#     if number == 0:
#         return "Zero"
#     if number == 1:
#         return "One"
#     if number == 2:
#         return "Two"
#     if number == 3:
#         return "Three"
#     if number == 4:
#         return "Four"
#     if number == 5:
#         return "Five"
#     if number == 6:
#         return "Six"
#     if number == 7:
#         return "Seven"
#     if number == 8:
#         return "Eight"
#     if number == 9:
#         return "Nine"
# def switch_it_up(number):
#     numbers = {0: "Zero", 1: "One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9: "Nine"}
#     return numbers[number]

# def switch_it_up(number):
#     match number: 
#         case 0: return "Zero"
#         case 1: return "One"
#         case 2: return "Two"
#         case 3: return "Three"
#         case 4: return "Four"
#         case 5: return "Five"
#         case 6: return "Six"
#         case 7: return "Seven"
#         case 8: return "Eight"
#         case 9: return "Nine"
# print(switch_it_up(7))

# def sum_mix(arr: list):
#     arr1 = []
#     for every_num in arr:
#         every_num = int(every_num)
#         arr1.append(every_num)
#     return sum(arr1)

#     return (sum([int(every_num) for every_num in arr]))

# print(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']))
# print(sum_mix(['3', 9, 6, 0, '5', 8, 5, '6', 2,'0']))
# print(sum_mix(['3', 2, 6, 0, '5', 8, 5, '6', 2,'0']))
# print(sum_mix(['3', 9, 6, 0, '5', 8, 5, '6', 2,'0']))
# print(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']))

# print(list(map(sum_mix, [['3', 6, 6, 0, '5', 8, 5, '6', 2,'0'], ['3', 9, 6, 0, '5', 8, 5, '6', 2,'0'], ['3', 2, 6, 0, '5', 8, 5, '6', 2,'0']])))
# sum = list(range(2,9,2))
# print(sum)

# def sum_mul(n, m):
#     sums = list(range(n,m,n))
#     return sum(sums)
# def calculator(a, b, op):
#     # check if a and b are int or float using type()
#     if not (type(a) in [int, float] and type(b) in [int, float]):

#     # if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
#         return "unknown value"

#         return "unknown value"
    
#     else:
#         return "unknown value"

#     abc = [1, 'ade', 1.6, True]

# print(isinstance(2, (int, float)))
# print(isinstance("what is my name?", (dict,)))
# type1 = [int, float]
# print(type(2))
# a = 2
# b = 6
# op = "*"
# evaluated_code = eval(f"a op b")

# print(evaluated_code)
'''For this problem you must create a program that says who ate the last cookie. If the input is a string then "Zach" ate the cookie. If the input is a float or an int then 
"Monica" ate the cookie. If the input is anything else "the dog" ate the cookie. The way to return the statement is: "Who ate the last cookie? It was (name)!"

Ex: Input = "hi" --> Output = "Who ate the last cookie? It was Zach! (The reason you return Zach is because the input is a string)

Note: Make sure you return the correct message with correct spaces and punctuation.

Please leave feedback for this kata. Cheers!

'''
# def cookie(x):
#     if type(x) == str:
#         x = "Zach"
#     elif type(x) == int or type(x) == float:
#         x = "Monica"
#     else:
#         x = "the dog"
        
#     return f"Who ate the last cookie? It was {x}!"
    
# print(cookie([1,1,2]))

# def cookie(x):
#     if type(x) == str:
#         suffix = "Zach!"
#     elif isinstance(x, (float, int)):
#         suffix = "Monica!"
#     else:
#         suffix = "the dog!"

#     return f"Who ate the last cookie? It was {suffix}!"
    
# print(cookie([1,1,2]))

'''You have to create a function named reverseIt.

Write your function so that in the case a string or a number is passed in as the data , you will return the data in reverse order. If the data is any other type, return it as it is.

Examples of inputs and subsequent outputs:

"Hello" -> "olleH"

"314159" -> "951413"

[1,2,3] -> [1,2,3]'''

# def reverse_it(data):
#     if type(data) == str:
#         return data[::-1]
#     elif type(data) == int:
#         data = str(data)
#         data = data[::-1]
#         return int(data)
#     elif type(data) == float:
#         data = str(data)
#         data = data[::-1]
#         return float(data)
#     else:
#         return data


    
# def reverse_it(data):
#     original_datatype = type(data)
#     if type(data) == str:
#         return data[::-1]
#     elif type(data) == int or type(float):
#         data = str(data)
#         data = data[::-1]
#         return original_datatype(data)
#     else:
#         return data
    
# print(reverse_it(456.8))
'''This is a spin off of my first kata.

You are given a string containing a sequence of character sequences separated by commas.

Write a function which returns a new string containing the same character sequences except the first and the last ones but this time separated by spaces.

If the input string is empty or the removal of the first and last items would cause the resulting string to be empty, return an empty value (represented as a generic value NULL in the examples below).

Examples
"1,2,3"      =>  "2"
"1,2,3,4"    =>  "2 3"
"1,2,3,4,5"  =>  "2 3 4"

""     =>  NULL
"1"    =>  NULL
"1,2"  =>  NULL'''

# def array(string: str):
#     if len(string) <= 3:
#         return None
#     else:
#         string = string[1:-1]
#         string = string.split(',')[1:-1]
#         return " ".join(string)

# def array(string: str):
#     if len(string) <= 3:
#         return None
#     else:
#         string = string[1:-1]
#         string = string.split(',')[1:-1]
#         result = " ".join(string)
#         if result == "":
#             return None
#         else:
#             return result
        

# def array(string: str):
#     result = " ".join(string.replace(",", " ").split()[1:-1])
#     return result or None

# print(len(array("1,2,3,4,5")))
# print(len(array("")))
# print(array("3445671"))

# def who_is_paying(name):
#     short_name = name[0:2]
#     if len(name) == 2:
#         return [short_name]
#     elif len(name) <= 2:
#         return [name]
#     else: return [name, short_name]

# print(who_is_paying("M"))

# def ensure_question(s: str):
#     if s.endswith('?'):
#         return s
#     else:
#         return s + '?'



