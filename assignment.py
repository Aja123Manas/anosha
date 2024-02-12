# A simple calculator that performs all the operations
a = int(input("Enter firstnumber:"))
b = int(input("Enter secondnumber:"))
operator = input("Enter operator:")
if operator == "+":
    print("result is",a + b)


if operator == "-":
    print("result is",a - b)

if operator == "*":
    print("result is",a * b)

if operator == "/":
    print("result is",a / b)

else:
    print("Invalid value")


