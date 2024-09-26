#lambda Function

f=lambda a,b:a+b

k=f(23,45)
print(k,'\n')
print('-------------------\n')


#filter function

a=[3,4,6,2,3,8,9,4,3]
b=list(filter(lambda i : i%2==0,a))
print(b,'\n')
print('-------------------\n')


#list mapping function

a=[6,3,3,6,7,5,4]
b=[3,4,6,3,8,9,3]
c=[]
for i in range(len(a)):
    c.append(a[i]+b[i])
    print(c,'\n')
   


#Map function
print('=======Map Function========\n')
a=[6,3,3,6,7,5,4]
b=[3,4,6,3,8,9,3]
c=list(map(lambda i,j:i+j,a,b))
m=list(c)

print(m)


#reduce function
print('======Reduce function=========\n')
a=[6,3,56,7,9,3,5]
import functools as fn
s=fn.reduce(lambda i,j:i+j,a)
print(s)


#partial function
print('========Partial function========\n')
import functools as t
def f(a,b,c):
    return a+b+c

k=t.partial(f,6)
g=t.partial(k,9)
print(g(7))


#zip function
print('========Zip function========\n')
a=[1,2,3,4,5]
b=['a','b','c','d','e']
c=list(zip(a,b))
print(c)


#unzip function
print('========Unzip function========\n')
a=[(1,'a'),(2,'b'),(3,'c'),(4,'d')]
b=list(zip(*a))
print(b)
                            



#-----------------------------------------------
#--------- monkey patching--------------------


# Create a module monk.py with the following code:
# monk.py


class A:
    def func(self):
        print('func() is being called')

def monkey_f(self):
    print('monkey_f() is being called')

A.func = monkey_f
obj = A()
obj.func()








#-------Now Importing A calender----------

import calendar
print(calendar.calendar(2024))


#---------calender according to the month-----

import calendar
print(calendar.month (2024, 6))



#now print calender from 2020--2024

import calendar
i=2020
while i<=2024:
    print(calendar.calendar(i))
    i+=1



#import date and time(there are many options available to show time and date)
import datetime
# print the current date and time
print(datetime.datetime.now())


import datetime
x=datetime.datetime(2018, 6, 1)
print(x.strftime("%Y-%m-%d"))



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#***********************************************************
#---------Exception Handling--------------------------

try:
    a=[5,3,7]
    print(a[5])
except IndexError:
 print('array is out of range')


try: print(6/0)
except ZeroDivisionError: 
 print('you cant divide by zero')

try:
   print('k'*'m')
except ZeroDivisionError:
   print('you cant divide by zero')
except IndexError:
   print('array out of range')
except TypeError:
   print('invalid type')
except Exception as e:
   print('something went wrong',e)




#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#*************custom exception**************


class InvalidAgeException(Exception):
    pass

try:
    age = int(input('Enter the age of the person'))
    if age < 18:
        raise InvalidAgeException('You are not eligible to vote')
    else:
        print('You are eligible to vote')
except InvalidAgeException as e:
    print(e)







#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#%%%%%%%%%%%%% File Handling %%%%%%%%%%%%%%%%%%%

#Read
f = open('file.txt','r')
print(f.read())
f.close()


#Write
f = open('','w')
f.write('Hello, world!')
f.close()


#append
f = open('file.txt','a')
f.write('Hello, world!')
f.close()


#for loop in this file handling
i=0
f = open('xyz.txt','r')
for line in f:
   print(line)
   i+=1
print(i)



