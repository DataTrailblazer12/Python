import pandas as pd  
  
info = {
        'name' : ['aa','bb','cc'],  
       'city' : ['jpr', 'dl', 'mum'],
        'age':[45.9,34.9,23.7]
        }  
  
d1 = pd.DataFrame(info)  
print (d1['city'])  
