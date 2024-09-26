print('welcome to the python calculator enjoy!!!')


def add(a,b):
 c=a+b
 print(c)

def sub(a,b):
 c=a-b
 print(c)

def mul(a,b):
 c=a*b
 print(c)

def div(a,b):
 c=a/b
 print(c)


op=str(input('select any operator: +,-,*,/: '))

a=int(input('enter the first number: '))
b=int(input('enter the first number: '))

if op=='+':
    add(a,b)

elif op=='-':
    sub(a,b)

elif op=='*':
    mul(a,b)

elif op=='/':
    div(a,b)
else:
    print('please select from above operator!!')
