# Combine 2 series to form a data frame

import pandas as pd
import numpy as np
ser1 = pd.Series(list('abcd'))
ser2 = pd.Series(np.arange(4))

df1 = pd.concat([ser1, ser2], axis = 1)
df2 = pd.DataFrame({'col1': ser1, 'col2': ser2})
df3 = pd.concat([ser1, ser2], axis = 0) # Get a serie

print(df1, df2, df3, sep='\n\n')
print(type(df1), type(df2), type(df3))


# Joining 2 dataframes
data1={'Student_ID': [3, 4, 6, 8, 10], 'CGPA': [4.5, 3, 4.37, 3.5, 4]}
df1=pd.DataFrame(data=data1)
data2={'Student_ID': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
'Maths': [4,52, 5, 2.5, 3, 3.9, 2.8, 4.75, 3.68, 5, 4.8]}
df2=pd.DataFrame(data=data2)
df3=pd.merge(df2, df1, on='Student_ID', how='left') 
print(df3)


# Stack
import pandas as pd
header = pd.MultiIndex.from_product([['Before Course','After Course'],['Marks']])
d=([[82,95],[78,89]])
 
my_df = pd.DataFrame(d,
 index=['Alisa','Bobby'],
 columns=header)

print(my_df.stack(level=0).unstack(level=0))