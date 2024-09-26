#MultiThreading------------
#----To apply thread use thread class has 'run' method and invoked using 'start' method

import threading
import time
class Test(threading.Thread):
    def run(self):
        for i in range(1,11):
            print(i)
            time.sleep(1)

class Test1(threading.Thread):
    def run(self):
        for i in range(1,11):
            print(3*i)
            time.sleep(2)



p=Test()
p.start()
p.join()
p=Test1()
p.start()
p.join()









#--------------------------------------

from threading import Thread
from time import sleep
class M(Thread):
    def run(self):
        for i in range(5):
            print(i*5)
            sleep(1)

class N(Thread):
    def run(self):
        for i in range(5):
            print(2*i)
            sleep(3)


M().start()
N().start()
#--------------------------------------

#---------------------------------------










#-------------------------- Random Module-----------------------
#generates random number's
import random
print(random.random())


#generates random number between 10 and 100
import random
print(random.randint(10,100))
print(random.randrange(10,100,10))





#----------------------------

import random
random.seed(20)
print(random.random())
random.seed(21)
print(random.random())



#------------------------
import random

mylist=["apple","banana","cherry"]
random.shuffle(mylist)
print(mylist)