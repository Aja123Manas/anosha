# Inbuilt functions
number = max(34, 78, 90, 123, 45)
print(number)

y = min(45, 78, 34, 23)
print(y)

z = pow(2,3)
print(z)


# User-defined functions
def name():
    print("Aja")


name()  # Calling a function

def details():
    name = "Aziz"
    age = 18
    course = "MIT"
    print(name, age, course)
details()

# Parameters/variable and arguments/value assigned to a variable
def patient(name, gender, age, MarriageStatus):
    print(name, gender, age, MarriageStatus)
patient("Job","female",45,"single")
patient("Mary","female",25,"single")

def multiply(x,y):
    print(x*y)

multiply(2,6)
multiply(34,60)
multiply(21,16)
multiply(15,3)


# Create user-defined function
# called employees. Display details using parameters
# five employees using the# following parameters fullname,age
# position, salary

def employees(fullname, age, position, salary):
    print(fullname, age, position, salary)

employees("Tatiana Nyokabi",30,"CEO","Ksh.120,000")
employees("Ngor Manas", 28, "Managing Director", "Ksh.100,000")
employees("Irene Njeri", 26, "Manager", "Ksh.80,000")
employees("Margaret Akinyi", 25, "Director", "Ksh.60,000")
employees("Achol Hakim", 24, "Secretary", "Ksh.40,000")


