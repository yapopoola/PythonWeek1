# Decorators are functions that change the behaviour of other functions.
# They are called using the `@` symbol and followed directly by the function to be decorated.
# A decorator takes in a function as argument and returns a function.
from functools import wraps

def log_frequency_of_use(original_function_that_was_called):
    def function_that_would_actually_be_called(*args):
        print("I have started to run my own steps.")

        log_file = open("add_function_logs.txt", "r+")
        current_count = int(log_file.readlines()[0].split()[-1])
        print(f"The current count gotten from the file is: {current_count}")

        result = original_function_that_was_called(*args)
        print("I just executed the original function that you called upon")

        
        log_file.close()

        # number_of_times_func_was_called += 1
        # print(f"The `{str(original_function_that_was_called)}` function has been called {number_of_times_func_was_called} times.")

        return result

    
    return function_that_would_actually_be_called


# @log_frequency_of_use
def add(first_num: int, second_num: int):
    """
    Adds two numbers together.
    Note:
        remember to call the counter object immediately after you call this add function
    """
    return first_num + second_num


# print(add(10, 5))
# print(add(20, 5))
# print(add(30, 5))
# print(add(40, 5))
def return_string_result_instead(casing: str):     # The main decorator function which takes in its own arguments
    def return_string_result(input_func):          # The function within the decorator that takes in the function to be deocrated as argument.
        """Take the input function, get its result and convert its to a message in the format:
        'The result of the function you called is: {the return value from the actual function I called}'.
        """
        def my_own_return_func(*args, **kwargs):   # The innermost func which takes in the arguments passed into the func to be deocrated as arguments.
            # print("The arg is now: ", args)
            # print("The kwarg is now: ", kwargs)

            result = input_func(*args, **kwargs)
            final_string = f'The result of the function you called is: {result}.'
            return final_string.lower() if casing == "lower" else final_string.upper()
        
        return my_own_return_func
    return return_string_result


@return_string_result_instead("lower")  
def add(first_num: int, second_num: int):
    """
    Adds two numbers together.
    Note:
        remember to call the counter object immediately after you call this add function
    """
    return first_num + second_num

# print(add(2, 6))

@return_string_result_instead("lower")
def subtract(first_num: int, second_num: int):
    """
    Subtract two numbers from each other.
    Note:
        remember to call the counter object immediately after you call this subtract function
    """
    return first_num - second_num


@return_string_result_instead("upper")
def divide(first_num: int, second_num: int):
    """
    Divides two numbers together.
    Note:
        remember to call the counter object immediately after you call this add function
    """
    return first_num / second_num


@return_string_result_instead("upper")
def multiply(first_num: int, second_num: int) -> int:
    """
    Adds two numbers together.
    Note:
        remember to call the counter object immediately after you call this add function
    """
    print("I received first num as: ", first_num)
    print("I received second num as: ", second_num)
    return first_num * second_num


# print(subtract(2, 6))

# tuple_example = (2, 6)
# dict_example = {
#     "first": 2,
#     "second": 6
# }


# multiply((2, 6), {"first": 2, "second": 6}) 
def changecase(n):
  def changecase_by_specific_number(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase_by_specific_number

@changecase(1)
def myfunction():
  return "Hello Linus"

# print(myfunction())

def changecase(func):
  def myinner():
    return_value_from_the_func_that_was_decorated = func()
    return return_value_from_the_func_that_was_decorated.upper()
  return myinner

def addgreeting(func):
  def myinner():
    return_value_from_the_func_that_was_decorated = func()  
    return "Hello " + return_value_from_the_func_that_was_decorated + " Have a good day!"
  return myinner


@addgreeting
@changecase
def myfunction():
  return "Tobias Popoola"


print(myfunction())