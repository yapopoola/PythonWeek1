 
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
         
# login_message = login_user_based_on_credentials()
# user_token = ...

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

def user_login():
    
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


def basic_function():
    return "Hi! I was called"


basic_funcs_final_answer = basic_function()


def basic_func_with_one_argument(username):
    message = f"Hello {username}"
    return message


def login_using_credentials(name, secret_key):  # function with two positional arguments
    message = f"Hello {name} with password {secret_key}"
    return message


# username = input('Please enter your username: ')
# password = input('Please enter your password: ')

# print(login_using_credentials(secret_key=password, name=username))


# function with multiple unknown number of positional arguments
def login_all_students(*student_names):
    for name in student_names:
        print(name)


# print(login_all_students("rafi", "My school is a goat", 345678, "tryyjhk"))

# function with multiple unknown number of keyword arguments
def login_all_student_users(**student_names):
    # return student_names
    for arg_name, student_name in student_names.items():
        print(arg_name, student_name)

# print(login_all_student_users(student_1="Rafihatu", student2="Yusuf", student_3="Jumai"))


# Function that takes in all the differnt argument types.
def login_anybody(username, password, *args, **kwargs): 
    return kwargs

# print(login_anybody("user1", "pass1", "kdgdh", 26884, "student", number=1854))


# How the `return` keyword works in python functions.
def is_number_odd_and_prime(number):
    # Check that the number is odd if it has a remainder after being divided by 2.
    if number % 2 != 0:
        return f"The number `{number}` is odd"

    elif number % 2 == 0:
        return f"The number `{number}` is even" 

    
    # check if any of the numbers smaller than it can divide it without remainder.
    # If it can be divided without remainder, then that number is not prime.
    else:
        for younger_num in range(2, number):
            if number % younger_num == 0:
                return f"The number `{number}` is not prime"
            
            else:
                return f"The number `{number}` is prime"
    


# num = int(input("Give me a number: "))
# print(is_number_odd_and_prime(3))

# Specifying the input datatypes of the function.
def login_anybody(username: str, password: int, *args, **kwargs): 
    return username


# Specifying the output datatypes of the function.
def login_anybody(username: str, password: str, *args, **kwargs) -> str: 
    return username[-3:]

# Specifying the default value of the function's arguments.
def login_anybody(username: str = "default_user", password: str = "passkey", *args, **kwargs) -> str: 
    return username[-3:]

# print(login_anybody())


arr = [1,20,3,5,7,8,9,11]

def first_non_consecutive(arr: list) -> int or str:
    previous_num = arr[0]

    for every_next_num in arr[1:]:
        if every_next_num != previous_num + 1:
            return every_next_num
        previous_num = every_next_num

arr = [1,2,3,4,5,6,7,8,9,10]
numbers_1_to_10 = arr


def first_non_consecutive_with_docstring(arr: list) -> int:
    """
    This function checks the `arr` to find the first number in the arr which does not follow consecutiveness.

    Args:
        arr (list): The python list containing the sequence of numbers to be checked.

    Note:
        Your `arr` must not be passed as an empty list into the function or it would throw an error.

    Returns:
        int: The first number in `arr` that is not consecutive.
    """
    try:
        for current_index in range(0, len(arr)):
            next_index = current_index + 1
            if arr[next_index] != arr[current_index] + 1:
                return arr[next_index]
    except (IndexError, ZeroDivisionError) as error:
        raise KeyError(f"I just wan do wetin I like: {error}")
        print(f"Omo! Your code don pass the limit for that list o!: {error}")
        return 0
    
    except ZeroDivisionError as err:
        print(err)
        print("Omo! You don go divide by zero, no be so o!")
        return 0
    
    else:
        return arr[next_index]


# non_consecutive = first_non_consecutive(arr)


# ------------------------------------------- LAMBDA FUNCTION (Functions with no name) --------------------------------------------
# def greater_than_nine(number):  return number > 9

# is_my_num_greater_than_nine = greater_than_nine(17)
# print(is_my_num_greater_than_nine)

is_greater_than_nine = lambda number1, number2: (number1 + number2) > 9
# print(is_greater_than_nine(1, 7))

participants = [("Yusuf", "Popoola"), ("Rafi", "Bello"), ("Adams", "Oshiomole"), ("Bola", "Tinubu")]

participants.sort(key=lambda each_name_group: each_name_group[0])
print(participants)