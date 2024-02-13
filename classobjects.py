# A class is a blueprint of an object
# An object is an instance of a class


class person:
    #Properties/attributes/characteristics/beharvior
    name = "Joe"
    age = 24
    # Method/Function/Beharvior
    def talk(self):
        print("Person is talking")

teacher = person()
print(teacher.name)
print(teacher.age)
teacher.talk()

