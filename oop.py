class Person:
    def __init__(self,firstname,age,gender):
        self.firstname=firstname
        self.age = age
        self.gender=gender
    def details(self):
        print(self.firstname,"is studying")
teacher = Person("John",25,"Male")
accountant = Person("Mary",56,"Female")
doctor = Person ("Joe", 57,"Male")
print(teacher.firstname,teacher.age,teacher.gender)
print(accountant.firstname,accountant.age,accountant.gender)
print(doctor.firstname,doctor.age,doctor.gender)
teacher.details()