class person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printName(self):
        print(self.firstname, self.lastname)

newPersonClass = person("ajul", "maharjan")
newPersonClass.printName()

class animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating %s." %(self.name, food) )

class dog(animal):
    def fetch(self,thing):
        print("%s goes after the  %s." %(self.name, thing) )

d = dog("tommy")
d.fetch('cookies')

a = animal('dog')
a.eat('dog food')