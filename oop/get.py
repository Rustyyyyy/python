import sys
import oop as op

# m = op.myclass()
op.m.hello("ajul")
# op.m.hello()

class myclass():
    def setAge(self, num):
        self.age =num

    def getAge(self):
        return self.age

ajul = myclass()
ajul.setAge(20)
print(ajul.getAge())

ram = myclass()
ram.setAge(12)
print(ram.getAge())

class car():
    def setPrice(self, num):
        self.price = num

    def getPrice(self):
        return self.price

if __name__ == "__main__":
    newCar = car()
    newCar.setPrice(10000)
    print(newCar.getPrice())


class alcohal():
    def setAge(self, age):
        self.number = age

    def getAge(self):
        return self.number

    def PersonAge(self):
        return ("The person who can drink alcohal is " + str(self.getAge()))
       


newAlcohal = alcohal()
newAlcohal.setAge(12)
print(newAlcohal.PersonAge())

class days():
    def SetDay(self, newDay):
        self.day = newDay

    def GetDay(self):
        return self.day

if __name__ == "__main__":
    day = days()
    day.SetDay("Thursday")
    print(day.GetDay())