class A:
    def f(s):
        print('hello')
class B(A):
    def g(s):
        print('bye')

class Z(B):
    def j(s):
        print('rtyuijh')

p=Z()
p.f()
p.g()
p.j()

