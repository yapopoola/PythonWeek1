"""Simple module explaining how imports work in Python."""

# To import a whole script/module in python, you simply use the import keyword
# import functionz
# functionz.user_db

# Import external libraries after pip installing them.

# import datetime
# import math
# import random
# import requests

# import pandas as pd
# import matplotlib as mp
# import numpy as np

# from functionz import user_db, basic_func_with_one_argument, basic_function
# from for_loopz import students


# data = {
#     "Name": ["Elon", "Trevor", "Swastik"],
#     "Age": [25, 30, 35]
# }

# df = pd.DataFrame(data).reset_index()
# print(df)


# # To import a specific thing from a script, use `from {script} import {thing}` syntax.
# from functionz import user_db
# user_db.get("user1")

# To import multiple things from a script, use `from {script} import {thing1}, {thing2}...` syntax.
# from functionz import user_db, user_login, basic_funcs_final_answer, basic_function

# To import all of the items from a script so that they can all be accessed by their names directly
# from functionz import *
# print(user_db)

# You can use the `as` keyword to change the name of an imported attribute at the point of import
# In other words, you use `as` to give your import an alias.
# from functionz import user_db as database
# import datetime as dt

# You can import from any folder accessible by your python script.
from katas.reverse_it import reverse_it
# from .person import student_info
# print(student_info)

print(reverse_it(345678))
""