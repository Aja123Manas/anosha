# Data Type

number = 67 # int
num = 78.98 # float
greeting = "Hello there" #str
IsPythonInteresting = True #bool



# A variable storing multiple values
languages = ["Python","PHP","Java"] #list
fruits = ("banana","apple","pineapple") #tuple
countries ={"Kenya","China","North America"} #set
# Dictionary
details = {
    "firstname":"Brian",
    "age" : 17,
    "course": "MIT",
    "nationality": "USA"
}
print(details["course"])
print(details["nationality"])
print(number)
print(IsPythonInteresting)
print(countries)



# Determining the data type
print(type(details))
print(type(countries))
print(type(languages))

# Typecasting - converting one datatype to another
print(float(number))
print(int(num))
