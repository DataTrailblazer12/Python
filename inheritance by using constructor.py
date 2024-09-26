class A:
    def __init__(s):        
        print('parrent')

class B(A):
    def __init__(s):
        super().__init__()
        print('child')

p=B()
