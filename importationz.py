# To import a whole script/module in python, you simply use the import keyword
# import functionz

# To import a specific thing from a script, use `from {script} import {thing}` syntax.
# from functionz import user_db

# To import multiple things from a script, use `from {script} import {thing1}, {thing2}...` syntax.
# from functionz import user_db, user_login, basic_funcs_final_answer, basic_function

# You can use the `as` keyword to change the name of an imported attribute at the point of import
# In other words, you use `as` to give your import an alias.
# from functionz import user_db as database
# import datetime as dt

# You can import from any folder accessible by your python script.
from katas.reverse_it import reverse_it

print(reverse_it(345678))
