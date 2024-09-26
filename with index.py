import pandas as pd  
  
info = {'name' : pd.Series(['aa','bb','cc'], index=['a', 'b', 'c']),  
   'city' : pd.Series(['jpr', 'dl', 'mum'], index=['a', 'b', 'c']),
        'age':pd.Series([45.9,34.9,23.7],  index=['a', 'b', 'c'])}  
  
d1 = pd.DataFrame(info)  
print (d1)  
