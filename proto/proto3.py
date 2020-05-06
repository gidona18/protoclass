class X:
    def __init__(self, x):
        self.x = x

x = X(10)
x.put = (lambda self: print(self.x)).__get__(x)

x.put()

