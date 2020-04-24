# constructor in python
class myClass(object):

    age = 11

    def __init__(self,h,w):
        self.a = h 
        self.b = w 


print(myClass.age)

if __name__ == "__main__":
    newObj = myClass("Hello", "world !!")
    print(newObj.a , newObj.b)

    

    obj = myClass(1,2)
    print(obj.a, obj.b)

class newClass():
    def __init__(self, aa, bb):
        self.a = aa
        self.b = bb

obj1 = newClass("a" , "b")
print(obj1.a, obj1.b)
