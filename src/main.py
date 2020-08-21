class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return 'i am ' + self.name + ',i am ' + str(self.age)


s = Student('igsnow', 10)
print(s.say())
