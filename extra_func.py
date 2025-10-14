

# two_times_five = multiply(2, 5)
# five_plus_five = add(5, 5)

# divide_by_10 = divide(multiply(2, 5), add(5, 5))
# print(divide_by_10)


numerical_datatype = int or float
def calculate(first_num: numerical_datatype, second_num: numerical_datatype, operation: str) -> numerical_datatype: 
    # add = first_num + second_num
    # new_num = add + (first_num * second_num)
    def add(first_num: int, second_num: int):
        print(f"When divided, the remainder is: {get_remainder(first_num, second_num)}")
        return first_num + second_num
    
    # print("The add function has been called", add(first_num, second_num))

    def subtract(first_num: int, second_num: int):
        # print(f"When added together, I am: {add(first_num, second_num)}")
        return first_num - second_num

    def divide(first_num: int, second_num: int):
        return first_num / second_num

    def multiply(first_num: int, second_num: int):
        return first_num * second_num
    
    if operation == "add":
        return add(first_num, second_num)
    elif operation == "multiply":
        return multiply(first_num, second_num)
    elif operation == "divide":
        return divide(first_num, second_num)
    elif operation == "subtract":
        return subtract(first_num, second_num)
    else:
        return get_remainder(first_num, second_num)
    

def get_remainder(first: int, second: int) -> int:
    answer = first % second
    return answer

    # operations_map = {
    #     "add": add,
    #     "subtract": subtract,
    #     "divide": divide,
    #     "multiply": multiply
    # }

    # operation_to_be_performed = operations_map.get(operation, add)
    # # print("operation to be performed is:", operation_to_be_performed)
    # return operation_to_be_performed(first_num, second_num)


# print(calculate(144, 13, "add"))
    
def add(first_num: int, second_num: int):
    """
    Adds two numbers together.
    Note:
        remember to call the counter object immediately after you call this add function
    """
    return first_num + second_num


def subtract(first_num: int, second_num: int):
    """
    Subtract two numbers from each other.
    Note:
        remember to call the counter object immediately after you call this subtract function
    """
    return first_num - second_num



def divide(first_num: int, second_num: int):
    """
    Divides two numbers together.
    Note:
        remember to call the counter object immediately after you call this add function
    """
    return first_num / second_num


def multiply1(first_num: int, second_num: int):
    """
    Adds two numbers together.
    Note:
        remember to call the counter object immediately after you call this add function
    """
    return first_num * second_num


def scientifically_calculate(first, second, operation):
    return operation(first, second)


def scientifically_calculate_2(operation_func, *args, **kwargs):
    return operation_func

# print(scientifically_calculate_2(multiply, 12, 14, 20, first_name="Rafi", second_name="Bello", first_num=12, second_num=12))


# def decorator(input_param: function) -> function:
#     def some_other_func(): ...
#     return some_other_func

# @decorator

