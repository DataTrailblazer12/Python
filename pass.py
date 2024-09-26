class A:
    def f(s):
        print('hello')
class B(A):
    def g(s):
        print('bye')

p=B()
p.f()
p.g()

