class A: #parent or bas or super class
    def f(s):
        print('hello')
class B(A):#child class 1
    def g(s):
        print('bye')

class Z(B):#child class 2
    def j(s):
        print('rtyuijh')

p=Z()
p.f()
p.g()
p.j()

