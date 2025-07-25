# In Python, we have integers which are regular numbers without any decimal
days = 5

# We also have floats which include decimal points e.g
float_days = 7.

# Complex numbers e.g
complex_days = 1j

# To convert a number to an integer, we can use the python builtin `int` function e.g
# print(int(float_days))

# # To convert a number to a float, we can use the python builtin `float` function e.g
# print(float(days))

# # To convert a number to its string representation, we can use the python builtin `str` function e.g
# print(str(float_days))

# # To round a number to its nearest whole number, we can use the python builtin `round` function e.g
print(round(float_days))


addition = days + float_days
subtraction = days - float_days
multiplication = days * float_days
division = days / float_days
rounded_div = days // float_days
exponential = days ** 2
modulus = float_days % days

print(modulus)
