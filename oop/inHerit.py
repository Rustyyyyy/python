# print("hello world!!")
class student():
    def __init__(self, name):
        self.fullname = name
    
    def printName(self):
        print('\nFull Name: %s.\n' %(self.fullname))

if __name__ == '__main__':
    obj = student('Ajul Maharjan')
    obj.printName()
    