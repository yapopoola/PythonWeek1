
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

# print(tuple[1:3] if tuple == ( 'abcd', 786 , 2.23, 'john', 70.2 ) else tuple())
'''You receive the direction you are facing (one of the 8 directions: N, NE, E, SE, S, SW, W, NW) and a certain degree to turn (a multiple of 45, between -1080 and 1080); 
positive means clockwise, and negative means counter-clockwise.
Return the direction you will face after the turn.
Examples
"S",  180  -->  "N"
"SE", -45  -->  "E"
"W",  495  -->  "NE"
'''
# def direction(facing, turn):
#     # facing = {"N":0, "NE":45, "E":90, "SE":135, "S":180, "SW":225, "W":270, "NW":315}
#     positions =  ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
#     number_of_times_to_move = abs(turn // 45)
#     start_position = positions.index(facing)
#     if str(turn).startswith("-"):
#         current_position = start_position - number_of_times_to_move
#     else:
#         current_position = start_position + number_of_times_to_move
#     try:
#         final_facing = positions[current_position]
#         return final_facing
#     except IndexError:
#         increase_list_by = (number_of_times_to_move // len(positions) ) + 2   # ADDING 1 JUST TO BE SAFE
#         print(increase_list_by)
#         positions = positions * increase_list_by
#         print(positions)
        # final_facing = positions[current_position]
        # return final_facing
    # finally:
    #     return final_facing


    
# print(direction("S", 180))
# print(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'] * 4)
# print(direction("SE", -45))
# print(direction("W", 495))
    
        
# def get_new_direction(current, degrees):
#     directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
#     pos = directions.index(current)
#     turns = degrees // 45
#     new_pos = (pos + turns) % 8
#     return directions[new_pos]

# # Test cases
# print(get_new_direction("S", 180))    # "N"
# print(get_new_direction("SE", -45))   # "E"
# print(get_new_direction("W", -1085))    # "NE"

# new_pos = 7 % 8
# print(new_pos)
# middle = (x for x in 'Geeks 22966 for Geeks' if x.isdigit())
# middle = ("2", "2", "9", "6", "6")
# last = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# a = [x for x in middle if x in last] 
# # a = []
# print(a)
# text = "hello wor\tld, \thello Python"
# result = text.count('')
# print(result), print(text)
# print(len(text))           # Output: 2

# print(text.expandtabs(1))


# my_message = "Hi Lagbaja, I have called my motherly and my x-rays and I have also called my two brothers. I miss them so much"

# decoder = str.maketrans(
#     "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z", 
#     "x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x+ x"
#     # "called": "opened",
#     # "motherly": "assembly",
#     # "my": "the",
#     # "father": "x-rays", 
#     # "brothers": "minister",
#     # "miss": "need",
# )

# print(my_message.translate(decoder))

# # s = 'geeks' 
# a, b, c, d, e = "geeks"
# # b = c = '*'
# # s = (a, b, c, d, e) 
# print(a) 

# tup = (2e-04, True, False, 8, 1.001, True)
# val = 0
# for x in tup:
#     val += int(x)
# print(val)

'''Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

For example:

a = 1
b = 4
--> [1, 2, 3, 4]'''

# def between(a,b):
#     return list(range(a,b+1))

# print(between(-2,3))

'''Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).

Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).

Examples:

* With `name` = "john"  => return "Hello, John!"
* With `name` = "aliCE" => return "Hello, Alice!"
* With `name` not given 
  or `name` = ""        => return "Hello, World!"'''

# def hello(name: str | None = ""):
#     if name == "":
#         return "Hello, World!"
#     return f"Hello, {name.capitalize()}!"
# d = dict() 
# for x in enumerate(range(2)): 
# 	d[x[0]] = x[1]
#     d[(0,0)[0]] = (0,0)[1]
#     d[0] = 0 
# 	d[x[1]+7] = x[0]
#     d[(0,0)[1] + 7] = (0,0)[0]
#     d[7] = 0
# print(list(enumerate(range(2))))
# print(x[1])
# print(x)

# dict ={} 
# print (any([1,4,5,6,7,8,9,'d,d', None, False])) 

# a = {} 
# a.fromkeys(['a', 'b', 'c', 'd'], 98) 
# print (a) 
# d = {1 : [1, 2, 3], 2: (4, 6, 8)} 
# d[1].append(4) 
# print(d[1], end = " ") 
# li = [d[2]]
# li.append(10) 
# d[2] = tuple(li) 
# print(d[2]) 
'''d = {
    1 : {'A' : {1 : "A"}, 2 : "B"}, 
    3 :"C", 
    'B' : "D", 
    "D": 'E'
    } 
print(d[d[d[1][2]]], end = " ") # E
print(d[d[1]["A"][2]]) 

d[
    d[1]["A"][2]
]
'''
# def func(a, b=[]):
#     b.append(a)
#     return

# print(func(1))
# print(func(2))

# import os 
# cwd = os.getcwd() 
# print("Current working directory:", cwd)

'''Create a function that takes an input String and returns a String, where all the uppercase words of the input String are in front and all the lowercase words at the end. 
The order of the uppercase and lowercase words should be the order in which they occur.
If a word starts with a number or special character, skip the word and leave it out of the result.
Input String will not be empty.
For an input String: "hey You, Sort me Already!" the function should return: "You, Sort Already! hey me
("123 baby You and Me"), "You Me baby and"), 
text = 'gA8y8dYh m_rqXj;q ??Pe[;S3 |f73FBDK CMfsfv5@'
'gA8y8dYh m_rqXj;q ??Pe[;S3 |f73FBDK CMfsfv5@' should equal 'CMfsfv5@ gA8y8dYh m_rqXj;q'"'''

# def capitals_first(text: str) -> str:
#     uppercase = []
#     lowercase = []
#     for word in text.split():
#         if not word[0].isalpha():
#             pass
#         else:
#             if word[0].isupper():
#                 uppercase.append(word)
#             else:
#                 lowercase.append(word)

#     return (" ".join(uppercase) + " " + " ".join(lowercase)).strip()


    # else:
    #     for every_char in text:
    #         if every_char[]:


    #     text = text.split()
    #     uppercase = text.upper()
    #     lowercase = text.lower()
    #     return " ".join(uppercase) + " ".join(lowercase)


# print(capitals_first('  hey You, Sort me Already!'))   

'''Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

None of the arrays will be empty, so you don't have to worry about that!'''

# def remove_every_other(my_list):
#     return my_list[::2]

# print(remove_every_other([1,2,3,4,5,6,7,8,9,10]))
'''Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example (Input => Output):
35231 => [1,3,2,5,3]
0     => [0]'''
# na = 12345
# def digitize(n):
#     n = str(n)
#     n[::-1]
#     " ".join(n)

# print(digitize(na))
# def digitize(n):
#     n = str(n)
#     n = n[::-1]
#     n = list(n)
#     na = []
#     for element in n:
#         element = int(element)
#         na.append(element)
#     return na

# def digitize(n):
#     return [int(element) for element in str(n)[::-1]]

'''We all love to have some rest. Also we all hate the sound of our alarms but it's inevitable at the end of the day. 
However, one is definitely not enough to wake you up. You set multiple alarms, just to force yourself to get up and go back to work/studies or just anything.
It is getting annoying, setting those up manually, so you decide to write a script for this task.
Task
Given the time to be set to wake up and the amount of alarms needed to be set, return an array of all timestamps for the alarms. 
The typical interval between the alarms is 5 minutes (at least, I think so).

Examples
set_the_alarms_up("08:00", 5) # Should return ["08:00", "08:05", "08:10", "08:15", "08:20"]
set_the_alarms_up("07:45", 8) # Should return ["07:45", "07:50", "07:55", "08:00", "08:05", "08:10", "08:15", "08:20"]
set_the_alarms_up("23:55", 2) # Should return ["23:55", "00:00"]
Input
time - a string, representing the time. Will always be valid. (no 25:30, 08:65 and etc.)

n - a number of alarms, needed to be set up. (n > 1, simply cause noone wakes up to one alarm)

Output
An array, consisting of all timestamps, an alarm is going to ring.


Good luck!'''
# 
# first, second = [1, 3, 5], [2, 4, 6]
# def merge_arrays(first, second):
#     first.extend(second)
#     first.sort()
#     return first

# print(merge_arrays([1, 3, 5], [2, 4, 6]))

# first = [1, 3, 5, 5]
# second = [2, 4, 6, 1]
'''Write a function that merges two sorted arrays into a single one. 
The arrays only contain integers. Also, the final outcome must be sorted and not have any duplicate.'''

# def merge_arrays(first, second):
#     first.extend(second)
#     first = set(first)
#     first = list(first)
#     first.sort()
#     return first

# def merge_arrays(first, second):
#     first.extend(second)
#     return sorted(set(first))

    

# print(merge_arrays([1, 3, 5, 5, 5], [2, 4, 6, 1, 3, 5]))

# def count_sheeps(sheep: list) -> int:
#     sheeps = []
#     for every_sheep in sheep:
#         if every_sheep == True:
#             sheeps.append(every_sheep)
#     return len(sheeps)

    # return len([every_sheep for every_sheep in sheep if every_sheep])
        
        

# print(count_sheeps([True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]))

# def count_sheeps(sheep: list) -> int:
#     sheeps = 0
#     for every_sheep in sheep:
#         if every_sheep is True:
#             sheeps += 1
#     return sheeps
        

# print(count_sheeps([True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]))
            


'''Your Task
Given an array of Boolean values and a logical operator, return a Boolean result based on sequentially applying the operator to the values in the array.

Examples
booleans = [True, True, False], operator = "AND"
True AND True -> True
True AND False -> False
return False
booleans = [True, True, False], operator = "OR"
True OR True -> True
True OR False -> True
return True
booleans = [True, True, False], operator = "XOR"
True XOR True -> False
False XOR False -> False
return False
Input
an array of Boolean values (1 <= array_length <= 50)
a string specifying a logical operator: "AND", "OR", "XOR"
Output
A Boolean value (True or False).
'''
# def logical_calc(array, op):
#     if op != "XOR":
#         op = op.lower()
#     else:
#         op = "^"
        
#     statement = f" {op} ".join([str(i) for i in array])
#     return eval(statement)
        
#     return eval(f" {op.lower() if op != 'XOR' else '^'} ".join([str(i) for i in array]))

# or |, and &&, xor ^
'''You love coffee and want to know what beans you can afford to buy it.

The first argument to your search function will be a number which represents your budget.

The second argument will be an array of coffee bean prices.

Your 'search' function should return the stores that sell coffee within your budget.

The search function should return a string of prices for the coffees beans you can afford. The prices in this string are to be sorted in ascending order.
(3, [6, 1, 2, 9, 2], "1,2,2"),
(14, [7, 3, 23, 9, 14, 20, 7], "3,7,7,9,14"),
(0, [6, 1, 2, 9, 2], ""),
(10, [], ""),
(10, [0, 0, 0], "0,0,0"),
(0, [0, 0, 0], "0,0,0"),
(24, [24, 0, 100, 2, 5], "0,2,5,24"),
(24, [2.7, 0, 100.9, 1, 5.5], "0,1,2.7,5.5"),
(-1, [1, 2, 3, 4], ""),
(-1, [-1, 0, 1, 2, 3, 4], "-1"),
(14, [17, 33, 23, 19, 19, 20, 17], ""),
(14, [13, 15, 14, 14, 15, 13], "13,13,14,14"),
'''

# def search(budget, prices):
#     prices = sorted(prices, reverse=True)
#     first_index = prices.index(budget)
#     valid_beans = prices[first_index:]
#     valid_prices = sorted(valid_beans)
#     valid_prices = str(valid_prices)[1:-1].replace(" ", "")
#     # valid_prices = "".join((valid_prices))
#     return valid_prices
    # last_index = prices.index(budget)
    # # budget = range(0, budget + 1)
    # prin
    # prices = sorted(prices[:budget])
    # return prices


# def search(budget, prices):
#     valid_prices = []
#     for each_price in prices:
#         if each_price <= budget:
#             valid_prices.append(str(each_price))

#     valid_prices = sorted(valid_prices)
#     final_answer = ",".join(valid_prices)
#     return final_answer


# def search(budget, prices):
#     return ",".join(sorted([str(price) for price in prices if price <= budget], key=lambda val: int(val)))

# print(search(14, [7, 3, 23, 9, 14, 20, 7]))


# my_list = [13, 13, 14, 14]

# str(my_list)  # --> "[13, 13, 14, 14]"

# answer = [str(every_num) for every_num in my_list]  # --> ["13", "13", "14", "14"]

# new_list = []
# for every_num in my_list:
#     new_list.append(str(every_num))

'''reverse_by_center("secret")  == "retsec" # no center character
reverse_by_center("agent")   == "nteag"  # center character is "e"'''

# def reverse_by_center(word):
#     if len(word) % 2 == 0:
#         mid_index = int(len(word) / 2)
#         first_half = word[:mid_index]
#         second_half = word[mid_index:]
#         return second_half + first_half
#     else:
#         mid_index = len(word) // 2
#         first_half = word[:mid_index]
#         middle_value = word[mid_index]
#         second_half = word[mid_index + 1:]
#         return second_half + middle_value + first_half

    # return mid_index


# print(reverse_by_center("agent"))

'''Kate and Michael want to buy a pizza and share it. Depending on the price of the pizza, they are going to divide the costs:

If the pizza is less than €5,- Michael invites Kate, so Michael pays the full price.
Otherwise Kate will contribute 1/3 of the price, but no more than €10 (she's broke :-) and Michael pays the rest.
How much is Michael going to pay? Calculate the amount with two decimals, if necessary.
def basic_test_cases():
        test.assert_equals(michael_pays(15), 10)
        test.assert_equals(michael_pays(4), 4)
        test.assert_equals(michael_pays(30), 20)
        test.assert_equals(michael_pays(80), 70)
        test.assert_equals(michael_pays(22), 14.67)
        test.assert_equals(michael_pays(5.9181), 3.95)
        test.assert_equals(michael_pays(28.789), 19.19)
        test.assert_equals(michael_pays(4.325), 4.33)'''

# def michael_pays(cost):
#     # michael_cost = None
#     # kate_cost = None
#     if cost < 5: return cost
#     elif cost * 1/3 <= 10: return round(cost * 2/3, 2)
#     # else:
#     #     return cost
    
# print((michael_pays(5.9181)))

'''An ATM has banknotes of nominal values 10, 20, 50, 100, 200 and 500 dollars. You can consider that there is a large enough supply of each of these banknotes.
You have to write the ATM's function that determines the minimal number of banknotes needed to honor a withdrawal of n dollars, with 1 <= n <= 1500.
Return that number, or -1 if it is impossible.
Good Luck!!! 
@test.it("should work when chosing notes is possible")
def _():
    test.assert_equals(solve(770), 4, "Wrong result for 770")
    test.assert_equals(solve(550), 2, "Wrong result for 550")
    test.assert_equals(solve(10), 1, "Wrong result for 10")
    test.assert_equals(solve(1250), 4, "Wrong result for 1250")


@test.it("should return -1 if chosing notes is not possible")
def _():
    test.assert_equals(solve(125), -1, "Wrong result for 125")
    test.assert_equals(solve(666), -1, "Wrong result for 666")
    test.assert_equals(solve(42), -1, "Wrong result for 42")
'''
# def solve(withdrawal):
#     banknotes = [10, 20, 50, 100, 200, 500]
#     if 1 <= withdrawal <= 1500:
#         banknotes
'''
Everybody knows the classic "half your age plus seven" dating rule that a lot of people follow (including myself). It's the 'recommended' age range in which to date someone.

Min
=
Age
2
+
7
Min= 
2
Age
​
 +7

Max
=
2
⋅
(
Age - 7
)
Max=2⋅(Age - 7)

Minimum age
≤
Your age
≤
Maximum age
Minimum age≤Your age≤Maximum age

Task
Given an integer (1 <= n <= 100) representing a person's age, return their minimum and maximum age range.

This equation doesn't work when the age <= 14, so if the age <= 14, use this equation instead:

min = age - 0.10 * age
max = age + 0.10 * age
You should floor all your answers so that an integer is given instead of a float (which doesn't represent age). Return your answer in the form "[min]-[max]"

Examples:
age = 27   =>   "20-40"
age = 5    =>   "4-5"
age = 17   =>   "15-20"

test.assert_equals(dating_range(17), "15-20")
# '''


# def dating_range(age):
#     if age <= 14:
#         min = age - 0.10 * age
#         max = age + 0.10 * age
#     else:
#         min = age / 2 + 7
#         max = 2 * (age - 7)
#     return f"{int(min)}-{int(max)}"

# print(dating_range(25))


# def find_longest(arr):
#     str_nums = [str(num) for num in arr]
#     len_nums = [len(num) for num in str_nums]
#     highest_num_of_digits = max(len_nums)
#     location_of_highest = len_nums.index(highest_num_of_digits)
#     return arr[location_of_highest]

# # def find_longest(arr):
# #     arr.sort(reverse=True) 
# #     return arr[0]

# print(find_longest([1, 10, 100, 599, -3456, 780, "abcdef" ]))

# def alphabetic(s):
#     if list(s) != sorted(s):
#         return False
#     else:
#         return True

# print(alphabetic("abc"))

# ["abc"]
# list("abc") --> ['a', 'b', 'c']

# import re

# def is_valid_email(email):
#     # Define the regex pattern for a valid email
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
#     # Use re.match to check if the email matches the pattern
#     return re.match(pattern, email) is not None

# # Example usage
# emails = [
#     "9john.doe@example.com",
#     "invalid-email",
#     "user@sub.domain.co",
#     "user@domain",
#     "user@domain.c"
# ]

# for email in emails:
#     print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")
'''import codewars_test as test
from solution import hex_color

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(hex_color(''), 'black')
        test.assert_equals(hex_color('000 000 000'), 'black')
        test.assert_equals(hex_color('121 245 255'), 'blue')
        test.assert_equals(hex_color('027 100 100'), 'cyan')
        test.assert_equals(hex_color('021 021 021'), 'white')
        test.assert_equals(hex_color('255 000 000'), 'red')
        test.assert_equals(hex_color('000 147 000'), 'green')
        test.assert_equals(hex_color('212 103 212'), 'magenta')
        test.assert_equals(hex_color('101 101 092'), 'yellow')
        
red + blue = magenta

green + red = yellow

blue + green = cyan

red + blue + green = white'''

# def hex_color(codes):
#     if not codes or codes == "000 000 000":
#         return "black"
    
#     color_combos = {
#         "green+blue": "cyan",
#         "red+green": "yellow",
#         "red+blue": "magenta",
#         "red+green+blue": "white"
#     }

#     codes = codes.split()
#     colors = ["red", "green", "blue"]
#     color_codes = [(colors[i], int(codes[i])) for i in range(len(codes))]
#     color_codes.sort(key=lambda item: item[-1])
#     highest_intensity = color_codes[-1][-1]
#     colors_with_highest_intensity = [color[0] for color in color_codes if color[-1] == highest_intensity]

#     if len(colors_with_highest_intensity) == 1:
#         return colors_with_highest_intensity[0]
    
#     color_combo = "+".join(colors_with_highest_intensity)
#     return color_combos[color_combo]
    


# print(hex_color("834 833 887"))

'''Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[] --> []
You can assume that all values are integers. Do not mutate the input array.'''

# def invert(lst):
#     return [-num for num in lst]
        
# # print(invert([1, 2, 3, 4, 5]))
# # def invert(lst):
# # abc=[1, 2, 3, 4, 5]
# # for num in abc:
# #     print([-num])

        
# print(invert([1, 2, 3, 4, 5]))
'''Your function takes two arguments:
current father's age (years)
current age of his son (years)
Сalculate how many years ago the father was twice as old as his son
(or in how many years he will be twice as old). 
The answer is always greater or equal to 0,
no matter if it was in the past or it is in the future.
def basic_test_cases():
        test.assert_equals(twice_as_old(36,7) , 22)
        test.assert_equals(twice_as_old(55,30) , 5)
        test.assert_equals(twice_as_old(42,21) , 0)
        test.assert_equals(twice_as_old(22,1) , 20)
        test.assert_equals(twice_as_old(29,0) , 29)'''

# def twice_as_old(dad_years_old, son_years_old):
#     dad, son = dad_years_old, son_years_old
#     count = 0
#     while dad != son * 2:
#         dad -= 1
#         son -= 1
#         count += 1
#         if son <= 0:
#             dad, son, count = dad_years_old, son_years_old, 0
#             while dad != son * 2:
#                 dad += 1
#                 son += 1
#                 count += 1
#     return count

# def twice_as_old(dad_years_old, son_years_old):
#     return dad_years_old - 2 * son_years_old
    
# print(twice_as_old(42, 21))

# def sum_two_smallest_numbers(numbers):
#     numbers = sorted(numbers)
#     numbers = sum(numbers[0:2])
#     return (numbers)

# print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))

# def factorial(n):
#     if n < 0 or n > 12: raise ValueError
#     for en in range(1, n): n = n * en
#     return n
        
#     print(n)

# print(factorial(10))
# from collections import Counter


# def get_socks(name, socks):
#     if name == "Punky":
#         first_sock = socks[0]
#         for sock in socks[1:]:
#             if sock != first_sock:
#                 return [first_sock, sock]
#         return []
#     else:
#         count_of_each_sock = [key for key, value in Counter(socks).items() if value >= 2]
#         return [count_of_each_sock[0], count_of_each_sock[0]] if count_of_each_sock else []
    

# print(get_socks("Henry", ['blue','green',"green", "red", "black"]))

'''Sample Tests
1
test.describe('Test cases analogy:')
2
## you can use your own test cases here
3
test.assert_equals(array_info([1,2,3.33,4,5.01,'bass','kick',' ']),[[8],[3],[2],[2],[1]],'Incorrect, check your code')
4
test.assert_equals(array_info([0.001,2,' ']),[[3],[1],[1],[None],[1]],'Incorrect, check your code')
5
test.assert_equals(array_info([]),'Nothing in the array!','Incorrect, check your code')
6
test.assert_equals(array_info([' ']),[[1],[None],[None],[None],[1]],'Incorrect, check your code')

Brief
Sometimes we need information about the list/arrays we're dealing with. You'll have to write such a function in this kata. Your function must provide the following informations:

Length of the array
Number of integer items in the array
Number of float items in the array
Number of string character items in the array
Number of whitespace items in the array
The informations will be supplied in arrays that are items of another array. Like below:
Output array = [[array length],[no of integer items],[no of float items],[no of string chars items],[no of whitespace items]]
Added Difficulty
If any item count in the array is zero, you'll have to replace it with a None/nil/null value (according to the language). 
And of course, if the array is empty then return 'Nothing in the array!. For the sake of simplicity, let's just suppose that there are no nested structures.
Output ====== If you're head is spinning (just kidding!) then these examples will help you out-
array_info([1,2,3.33,4,5.01,'bass','kick',' '])--------->[[8],[3],[2],[2],[1]]    
array_info([0.001,2,' '])------------------------------>[[3],[1],[1],[None],[1]]   
array_info([])----------------------------------------->'Nothing in the array!'
array_info([' '])-------------------------------------->[[1],[None],[None],[None],[1]]
Remarks
The input will always be arrays/lists. So no need to check the inputs.
Hint ==== See the tags!!!
Now let's get going !
# '''
# def array_info(xxxxx):
#     if xxxxx == []:
#         return "Nothing in the array!"
#     len_xxxxx = len(xxxxx)
#     no_of_int = 0
#     no_of_float = 0
#     no_of_str = 0
#     no_of_whitespaces = 0
#     for xxx in xxxxx:
#         if type(xxx) == int:
#             no_of_int += 1
#         if type(xxx) == float:
#             no_of_float += 1
#         if type(xxx) == str and xxx != " ":
#             no_of_str += 1
#         if xxx == " ":
#             no_of_whitespaces += 1

#     output = [[len_xxxxx if len_xxxxx != 0 else None],
#               [no_of_int if no_of_int != 0 else None],
#               [no_of_float if no_of_float != 0 else None],
#               [no_of_str if no_of_str != 0 else None],
#               [no_of_whitespaces if no_of_whitespaces != 0 else None]]
    
#     return output


    # for xxx in xxxxx:
    #     if xxx == 0:
    #         return None
    #     if xxxxx == []:
    #         return "Nothing in the array!"
    # else:
    # if len_xxxxx == 0 or no_of_int == 0 or no_of_float == 0 or no_of_str == 0 or no_of_whitespaces == 0:
    #     return 

# print(array_info([1,2,3.33,4,5.01,'bass','kick',' ']))
# print(array_info([" "]))
'''import codewars_test as test
from solution import band_name_generator

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(band_name_generator("knife"), "The Knife")
        test.assert_equals(band_name_generator("tart"), "Tartart")
        test.assert_equals(band_name_generator("sandles"), "Sandlesandles")
        test.assert_equals(band_name_generator("bed"), "The Bed")
        test.assert_equals(band_name_generator("qq"), "Qqq")
        
My friend wants a new band name for her band. She like bands that use the formula: 
"The" + a noun with the first letter capitalized, for example:
"dolphin" -> "The Dolphin"
However, when a noun STARTS and ENDS with the same letter, 
she likes to repeat the noun twice and connect them together with the first and last letter, 
combined into one word (WITHOUT "The" in front), like this:
"alaska" -> "Alaskalaska"
Complete the function that takes a noun as a string, and returns her preferred band name written as a string.

'''
# def band_name_generator(name: str):
#     name = name.lower()
#     if name.startswith(name[0]) and name.endswith(name[0]):
#         return name.capitalize()[:-2] + name.lower()
#     else:
#         return "The " + name.capitalize()
        
# print( band_name_generator("Tart"))


'''Ahoy matey!

You are a leader of a small pirate crew. And you have a plan. With the help of OOP you wish to make a pretty efficient system to identify ships with heavy booty on board!

Unfortunately for you, people weigh a lot these days, so how do you know if a ship is full of gold and not people?

You begin with writing a generic Ship class / struct:

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
Every time your spies see a new ship enter the dock, they will create a new ship object based on their observations:

draft - an estimate of the ship's weight based on how low it is in the water
crew - the count of crew on board
Titanic = Ship(15, 10)
Task
You have access to the ship "draft" and "crew". "Draft" is the total ship weight and "crew" is the number of humans on the ship.

Each crew member adds 1.5 units to the ship draft. If after removing the weight of the crew, the draft is still more than 20, 
then the ship is worth looting. Any ship weighing that much must have a lot of booty!

Add the method

is_worth_it
to decide if the ship is worthy to loot. For example:

Titanic.is_worth_it()
False
Good luck and may you find GOOOLD!'''

# class Ship:
#     def __init__(self, draft, crew):
#         self.draft = draft
#         self.crew = crew

#     def is_worth_it(self):
#         self.crew = self.crew * 1.5
#         if self.draft - self.crew > 20:
#             return True
#         else: 
#             return False

# Ship(100,20)
#     ship_total_weight = 100
#     weight_per_person = 1.5
#     crew_total_weight = crew * weight_per_person = 30
#     weight_of_items_in_ship = ship_total_weight - crew_total_weight = 70
'''Task Description
You're re-designing a blog, and the blog's posts have the Weekday Month Day, time format for showing the date and time when a post was made, e.g., Friday May 2, 7pm.
You're running out of screen real estate, and on some pages you want to display a shorter format, Weekday Month Day that omits the time.
Write a function that takes the website date/time in its original string format and returns the shortened format.
Input
Input will always be a string, e.g., "Friday May 2, 7pm". 
Output
Output will be the shortened string, e.g., "Friday May 2".'''

# def shorten_to_date(long_date: str):
#     long_date = long_date.split()
#     del long_date[-1]
#     long_date = " ".join(long_date)
#     return long_date[:-1]

# print(shorten_to_date("Monday February 2, 8pm"))

# def remove_bmw(string: str):
#     try:
#         string = string.replace("B", "")
#         string = string.replace('b', "")
#         string = string.replace('M', "")
#         string = string.replace('m', "")
#         string = string.replace('W', "")
#         string = string.replace('w', "")
#         return string
#     except:
#         raise TypeError("This program only works for text.")
    
# def remove_bmw(string: str):
#     import re
#     if type(string) != str:
#         raise TypeError("This program only works for text.")
#     return re.sub("[BMWbmw]", "", string)

# print(remove_bmw("bmwvolvoBMW"))

# def find_function(func):
#         for x in func:
#             if type(x) == type(find_function):
#                 return x


# print(find_function([lambda a: a%2==0,9,3,1,0]))


# arr = [2,1,5,3]

# def get_val(a):
#     return a % 2 == 0


# x = lambda a: a % 5 == 0

# [lambda a: a%2==0,9,3,1,0]
# result = [i for i in arr if x(i)]
# print (result)

# for i in arr:
#     if i == 1:
#         print (i)
# a = [i for i in arr if i == "a"]
# print (a)


# find_function(
#     [
#         lambda a: a%2==0,
#         9,
#         3,
#         1,
#         0
#     ],
#     [1,2,3,4]
# )

# def cap_me(arr: str):
#     return [i.capitalize() for i in arr]


# print(cap_me(["jo", "nelson", "jurie"]))

# def time_convert(num):
#     if num <= 0:
#         return "00:00"
#     else:
#         hour = num // 60
#         min = num % 60
#         return f"{hour}:{min}"

# def better_than_average(class_points, your_points):
#     if sum(class_points) / len(class_points) < your_points: return True
#     return False

# print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))

# class_points = [100, 40, 34, 57, 29, 72, 57, 88]
# print(sum(class_points) / len(class_points))

# def str_count(strng, letter):
#     count = 0
#     for letter in strng:
#         if letter in strng:
#             count += 1
#     return count


# print (str_count('striiing', 'i'))
# strng = "Panda has 48 apples and loses 4"
# def calculate(strng: str):
#     if "loses" in strng:
#         return int(strng.split()[2]) - int(strng.split()[-1])
#     else:
#         return int(strng.split()[2]) + int(strng.split()[-1])
        

# print(calculate("Panda has 48 apples and gains 4"))
# def what_list_am_i_on(actions: str):
#     for word in actions:
#         if word.startswith(("b", "f", "k")): return "naughty"
#         elif word.startswith(("g", "s", "n")): return "nice"
#         else: return "naughty"

# def what_list_am_i_on(actions: str):
#     naughty_words = 0
#     nice_words = 0
#     for word in actions:
#         if word.startswith(("b", "f", "k")): 
#             naughty_words += 1
#         elif word.startswith(("g", "s", "n")): 
#             nice_words += 1
#     if naughty_words >= nice_words:
#         return "naughty"
#     else:
#         return "nice"


# print(what_list_am_i_on(['never got into a fight', 'tied someone\'s shoes', 'broke a vending machine' ]))

# def create_template(template):
#     def answer(*args, **kwargs):
#         new_string = []
#         for word in template.split():
#             if word.startswith("{"):
#                 new_string.append(kwargs.get(word[2:-2]))
#             else:
#                 new_string.append(word)
#         return " ".join([str(word) for word in new_string]).replace("None", "")
                
#     return answer

# template = create_template("{{firstName}} {{lastName}} likes {{interests}}")
# print(template(firstName="John", lastName="Smith", interests="sport"))
# print(template(firstName="Albert", occuptation="physicist"))

'''Create a function that takes a number as an argument and returns a grade based on that number.

Score	Grade
Anything greater than 1 or less than 0.6	"F"
0.9 or greater	"A"
0.8 or greater	"B"
0.7 or greater	"C"
0.6 or greater	"D"
Examples:

grader(0)   should be "F"
grader(1.1) should be "F"
grader(0.9) should be "A"
grader(0.8) should be "B"
grader(0.7) should be "C"
grader(0.6) should be "D"'''

# def grader(score):
#     # grade_points = {
#     #     0.6 : 'F',
#     #     0.9 : 'A',
#     #     0.8 : 'B',
#     #     0.7 : 'C',
#     #     0.6 : 'D',
#     # }
#     if score > 1 or score < 0.6: return "F"
#     elif score >= 0.9: return "A"
#     elif score >= 0.8: return "B"
#     elif score >= 0.7: return "C"
#     elif score >= 0.6: return "D"

# grader(0.87)

# '''Complete the solution so that it reverses all of the words within the string passed in.

# Words are separated by exactly one space and there are no leading or trailing spaces.

# Example(Input --> Output):

# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"'''

# def reverse_words(s: str):
#     s = s.split()[::-1]
#     s = " ".join(s)
#     return s

#     s = s[::-1]
#     return s
    
# print(reverse_words('mango is a fruit'))

# '''Is the string uppercase?
# Task
# Create a method to see whether the string is ALL CAPS.

# Examples (input -> output)
# "c" -> False
# "C" -> True
# "hello I AM DONALD" -> False
# "HELLO I AM DONALD" -> True
# "ACSKLDFJSgSKLDFJSKLDFJ" -> False
# "ACSKLDFJSGSKLDFJSKLDFJ" -> True'''
# def is_uppercase(inp: str):
#     # if inp == inp.upper(): return True
#     # else: return False
#     return True if inp == inp.upper()  else False
# print(is_uppercase(inp))

#     fruits_dict = {
#     1: "kiwi",
#     2: "pear",
#     3: "kiwi",
#     4: "banana",
#     5: "melon",
#     6: "banana",
#     7: "melon",
#     8: "pineapple",
#     9: "apple",
#     10: "pineapple",
#     11: "cucumber",
#     12: "pineapple",
#     13: "cucumber",
#     14: "orange",
#     15: "grape",
#     16: "orange",
#     17: "grape",
#     18: "apple",
#     19: "grape",
#     20: "cherry",
#     21: "pear",
#     22: "cherry",
#     23: "pear",
#     24: "kiwi",
#     25: "banana",
#     26: "kiwi",
#     27: "apple",
#     28: "melon",
#     29: "banana",
#     30: "melon",
#     31: "pineapple",
#     32: "melon",
#     33: "pineapple",
#     34: "cucumber",
#     35: "orange",
#     36: "apple",
#     37: "orange",
#     38: "grape",
#     39: "orange",
#     40: "grape",
#     41: "cherry",
#     42: "pear",
#     43: "cherry",
#     44: "pear",
#     45: "apple",
#     46: "pear",
#     47: "kiwi",
#     48: "banana",
#     49: "kiwi",
#     50: "banana",
#     51: "melon",
#     52: "pineapple",
#     53: "melon",
#     54: "apple",
#     55: "cucumber",
#     56: "pineapple",
#     57: "cucumber",
#     58: "orange",
#     59: "cucumber",
#     60: "orange",
#     61: "grape",
#     62: "cherry",
#     63: "apple",
#     64: "cherry",
#     65: "pear",
#     66: "cherry",
#     67: "pear",
#     68: "kiwi",
#     69: "pear",
#     70: "kiwi",
#     71: "banana",
#     72: "apple",
#     73: "banana",
#     74: "melon",
#     75: "pineapple",
#     76: "melon",
#     77: "pineapple",
#     78: "cucumber",
#     79: "pineapple",
#     80: "cucumber",
#     81: "apple",
#     82: "grape",
#     83: "orange",
#     84: "grape",
#     85: "cherry",
#     86: "grape",
#     87: "cherry",
#     88: "pear",
#     89: "cherry",
#     90: "apple",
#     91: "kiwi",
#     92: "banana",
#     93: "kiwi",
#     94: "banana",
#     95: "melon",
#     96: "banana",
#     97: "melon",
#     98: "pineapple",
#     99: "apple",
#     100: "pineapple"
# }


# '''
# Subtract the sum
# NOTE! This kata can be more difficult than regular 8-kyu katas (lets say 7 or 6 kyu)

# Complete the function which get an input number n such that n >= 10 and n < 10000, then:

# Sum all the digits of n.
# Subtract the sum from n, and it is your new n.
# If the new n is in the list below return the associated fruit, otherwise return back to task 1.
# Example
# n = 325
# sum = 3+2+5 = 10
# n = 325-10 = 315 (not in the list)
# sum = 3+1+5 = 9
# n = 315-9 = 306 (not in the list)
# sum = 3+0+6 = 9
# n =306-9 = 297 (not in the list)
# .
# .
# .
# ...until you find the first n in the list below.

# There is no preloaded code to help you. This is not about coding skills; think before you code'''


# def subtract_sum(number: int):
#     number = str(number)
#     total = 0
    
#     for evry_num in number:
#         total += int(evry_num)

#     number = int(number) - total
    
#     if number in fruits_dict:
#         return fruits_dict[number]
#     else:
#         return subtract_sum(number)
        

# print(subtract_sum(123))

# class Solution:
#     def isUgly(self, n: int) -> bool:
#         divisibility = dict()
#         for small_num in range(2, n):
#             if n % small_num == 0:
#                 divisibility[small_num] = True
#             else:
#                 divisibility[small_num] = False
        
#         not_included = [key for key, value in divisibility.items() if value is True and key not in (2, 3, 5)]
#         return False if not_included else True
    
# print(Solution().isUgly(15))

# def filter_numbers(string: str):
#     return "".join(x for x in string if x.isalpha() or x == " ")


# print(filter_numbers("test123"))


'''Create a function with two arguments that will return an array of the first n multiples of x.
Assume both the given number and the number of times to count will be positive numbers greater than 0.
Return the results as an array or list ( depending on language ).
Examples
x = 1, n = 10 --> [1,2,3,4,5,6,7,8,9,10]
x = 2, n = 5  --> [2,4,6,8,10]  test.assert_equals(count_by(1, 5), [1, 2, 3, 4, 5])
        test.assert_equals(count_by(2, 5), [2, 4, 6, 8, 10])
        test.assert_equals(count_by(3, 5), [3, 6, 9, 12, 15])
        test.assert_equals(count_by(50, 5), [50, 100, 150, 200, 250])
        test.assert_equals(count_by(100, 5), [100, 200, 300, 400, 500])'''


# def count_by(x, n):
#     return list(range(x, x*n+1, x))

# print(count_by(50,5))


# def string_to_array(s: str):
#     return [""] if s == "" else s.split()
    
# def dna_to_rna(dna):
#     return dna.replace("T", "U")

def even_or_odd(number: int):
    if type(number) == int:
        return "Even" if int(number) % 2 == 0 else "Odd"
    raise TypeError("Please provide a valid number")

# print(even_or_odd(["Benny", 123]))