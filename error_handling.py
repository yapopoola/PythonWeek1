# Exceptions are errors that happen while the code is being executed.
# In Python, you can handle exceptions using the try/except syntax. 

try:
    pass # some block of code you want to run

except:
    pass # would be executed if the specified error was raised in your try block.

else:
    pass # would be executed if no error occured in the try block.

finally:
    pass # finally, whether an error occurred or not, do this...



def first_non_consecutive(arr):
    try:
        answer = None
        for current_index in range(0, len(arr) - 1):
            next_index = current_index + 1
            if arr[next_index] != arr[current_index] + 1:
                answer = arr[next_index]
    except (IndexError, ZeroDivisionError) as error:
        # raise KeyError(f"I just wan do wetin I like: {error}")
        print(f"Omo! Your code don pass the limit for that list o!: {error}")
        return 0
    else:
        print("The else block was executed in this run.")
        return answer
    finally:
        print("At the end of the day, we got here.")
        
    # except ZeroDivisionError as err:
    #     print(err)
    #     print("Omo! You don go divide by zero, no be so o!")
    #     return 0


print(first_non_consecutive([1,2,3,4,5,6,7,8,9,10]))
