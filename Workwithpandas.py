import numpy as np
import pandas as pd

ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

df = pd.concat([ser1, ser2], axis=1)

df = pd.DataFrame({'col1': ser1, 'col2': ser2})

# print(df.head())


# How to get the items of series A not present in series B?

A = pd.Series([1, 2, 3, 4, 5, 10, 20, 30, 40])
B = pd.Series([4, 5, 6, 7, 8, 20, 40])

print(A[~A.isin(B)])
# print(A)



df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1), columns=list('pqrs'), index=list('abcdefghij'))
print(df)
