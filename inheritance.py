# Paren class/Super class/Base class
class Animal:
    def sound(self):
        print("Animal is speaking")

# Child class/Sub class/Derived class
class Dog(Animal):
    def bark(self):
        print("dog is barking")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

a = Animal()
d = Dog()
d.bark()
c = Cat()
c.meow()


