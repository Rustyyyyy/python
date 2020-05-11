class numbers(object):

    multiplier = 1

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self): return self.x + self.y

    @staticmethod
    def multiply(a): return a * numbers.multiplier

    @staticmethod
    def subract(b, c): return b - c

new_N = numbers(5,5)

print(new_N.add())
print(numbers.multiply(3))
print(numbers.subract(2,1))