student = "Yusuf"
teacher = student

listy = {"Rafi", 1, "Bello", 20}
dicty = {"name": "Rafi", "score": 200, "last_name": "Bella"}
# To check that two elements are equal in value, you use the double equals to sign.

if 3 + 2 == 3 + 2:
    print("This is true")

# To check that two elements are not equal in value, 
# you use the exclamation mark followed by equals to sign.
# print(student != teacher)

# To check that the element on the left is greater than the one on the right.
# print(student > teacher)

# To check that the element on the left is less than the one on the right.
# print(student < teacher)

# To check that the element on the left is greater than or equal to the one on the right.
# print(student >= teacher)

# To check that the element on the left is less than or equal to the one on the right.
# print(listy <= dicty)


# all_students = ["Jumai", "John", "James", "Johnny", "Jack", "Jill"]
# name = input("What is your name? ")

# # To define an `if` statement, the syntax is if, followed by the condition, followed by the colon
# # i.e if condition:
# # on the next line the rest of the code that should be run if that condition is true.
# if name in all_students:
#     print(f'Yes, {name} is registered for the class.')
# else:
#     print(f"No, {name} is NOT registered for the class.")



available_soaps = ["Delta", "Dudu Osun", "Dettol", "Imperial Leather", "Dove", "Nivea"]
unavailable_soaps = ["Nivea", "Delta", "Dudu Osun", "Dettol", "Imperial Leather", "Dove"]

# print(available_soaps == unavailable_soaps)
# soap_name = input("What soap do you want to buy? ")
# biscuit_name = input("What biscuit do you want to buy? ")

# To define an `if` statement, the syntax is if, followed by the condition, followed by the colon
# i.e if condition:
# on the next line the rest of the code that should be run if that condition is true.
# if soap_name == "Dettol":
#     print(f'Yes, it is available. Here is your {soap_name} soap')

# elif soap_name == "Dove":
#     print(f'Yes, it is available. Here is your {soap_name} soap')

# elif soap_name == "Nivea":
#     print(f'Yes, it is available. Here is your {soap_name} soap')

# else:
#     print(f"No, {soap_name} is NOT available. Check again later.")


# if soap_name == "Dettol":
#     print(f'Yes, it is available. Here is your {soap_name} soap')

# if soap_name == "Dove":
#     print(f'Yes, it is available. Here is your {soap_name} soap')

# if soap_name == "Nivea":
#     print(f'Yes, it is available. Here is your {soap_name} soap')

# if soap_name in available_soaps:
#     print(f"No, {soap_name} is available. Welcome.")

# if soap_name not in available_soaps:
#     print(f"No, {soap_name} is not available. Check back later.")

"""
If they have dettol, buy dettol.
If they dont have dettol, buy dove.
if dettol and dove are not available, by nivea.
if they dont have any of these, come back home.
Then buy biscuit for yourself.
"""

# The `in` keyword is used to check if an element exists in a container.
# check a char exists in a string
# class_description = "This is an adhoc python class for one student only."
# search_param = input("What are you searching for today? ")

# if search_param in class_description:
#     result = f"You search criteria of {search_param} was found in the class description."
#     print(result)

# class_description = {"This", "is", "an", "adhoc", "python", "class"}
# search_param = input("What are you searching for today? ")

# if search_param in class_description:
#     result = f"You search criteria of `{search_param}` was found in the class description."
#     print(result)

# participants = {"student": "YP", "teacher": "RB", "is_class_active": True, "price": 199.99}
# search_param = input("What are you searching for today? ")

# if search_param in participants:
# # if ("student", "YP") in [("student", "YP"), ("teacher", "RB"), ("is_class_active", True)]:
#     result = f"You search criteria of {search_param} was found in the class description."
#     print(result)

# Some keywords used in checking criteria are: in, not, and, or, is

"""
Write a python script that takes a student's score as input from the command prompt and 
prints out their grade based on their score.
Students who score 70 and above, their grade is `A`.
Students who score between 60 and 69, their grade is `B`.
Students who score between 50 and 59, their grade is `C`.
Students who score between 40 and 49, their grade is `D`.
Students with scores below 40 have failed the course and should resit the exam.
"""

# score = float(input("What is your score? "))

# if (score >= 70) or (score <= 100):
#     print("You are a very bright student. A+")

# elif (score >= 60) and (score <= 69.99):
#     print("You are a very bright student. B+")

# elif (score >= 50) and (score <= 59):
#     print("You are a very bright student. C+")

# elif (score >= 40) and (score <= 49):
#     print("You are a very bright student. D+")

# elif (score >= 0) and (score <= 39):
#     print("You are NOT a very bright student.")

# else:
#     print("This your score no follow o!")


# Get the student's score from the command prompt
# score = float(input("Enter the student's score: "))

# #     # Validate the score is within a reasonable range (0-100)
# if score < 0 or score > 100:
#     print("Invalid score! Please enter a score between 0 and 100.")
# else:
# # Determine the grade based on the score
#     if score >= 70:
#         grade = 'A'
#         print(f"The student's grade is {grade}.")
#     elif score >= 60:
#         grade = 'B'
#         print(f"The student's grade is {grade}.")
#     elif score >= 50:
#         grade = 'C'
#         print(f"The student's grade is {grade}.")
#     elif score >= 40:
#         grade = 'D'
#         print(f"The student's grade is {grade}.")
#     else:
#         print("The student has failed the course and needs to re-sit the exam.")

