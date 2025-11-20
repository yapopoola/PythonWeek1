import pandas as pd
import matplotlib 
def rename_columns(df: pd.DataFrame, names: list):  
    df.columns=list('ABC')
    pass

# df_input = pd.DataFrame(data=[[1,2,3], [4,5,6]], columns=list('123'))
# print(df_input)
# names = ('A', 'B', 'C')
# df_output = pd.DataFrame(data=[[1,2,3], [4,5,6]], columns=list('ABC'))
# user_solution = rename_columns(df_input, names)

import pandas as pd

# Example DataFrame
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=list('ABC'))

# Rename all columns
df.columns=(names)
df.copy

print(df)
