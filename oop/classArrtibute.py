# constructor in python
class myClass():

    agee = 12
    
    def __init__(self, age):
        self.a = age



myClass.a = 11
print(myClass.a)

newAge = myClass(12)
print(myClass.agee)


# print(newAge.age)
# 
# del newAge.age #deletes overriden value
# 
# print(newAge.age)
# 

# print(myClass.age)
# 
# myClass.age = 12
# 
# print(myClass.age)
# 