

#UPPER CASE
a="hello world"
print(a.upper())

#lower case
a="HELLO WORLD"
print(a.lower())


#remove whitespace
a="  hello world  "
print(a.strip())

#replace string
a="hello world"
print(a.replace("world","python"))

#split string
a="hello world python"
print(a.split())

#string concatenation
a="hello "
b="world"
print(a+b) #here we can also do c=a+b and then print(c)



quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item_no {} for {} dollars."
print(myorder.format(quantity, itemno, price))







#escape character---------------

#txt="we are the so-called "Vikings" from the north.."   so this is incorrect

txt="we are the so called \"vikings\" of the north"
print(txt)





#string methods #capitalize()
a="hello bro"
b=a.capitalize()
print(b) 

#casefold
a="Hello, World!"
b=a.casefold()
print(b)

#endswith
a="hello"
b=a.endswith('l')
print(b)

#find
a="hello"
b=a.find('o')
print(b)

#format
a="hello"
b=a.format()
print(b)
