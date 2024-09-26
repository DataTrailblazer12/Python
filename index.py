import pandas as pd

x={'name':['yogesh','aman','shivam'],'age':[19,18,19]}

df=pd.DataFrame(x,index = ['first','second','third'])
print(df)

print(df.loc["second"])
