temperature = 34
if temperature > 25 :
    print("It is hot")
else:
    print("It is cold")

# A program that determines the largest number among three numbers
num1 = 20
num2 = 35
num3 = 78
if num1 >num2 and num1 >num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 >num3:
    print(num2, "is the largest number")
else:
    print(num3,"is the largest number")

# A program that checks whether a number is even or odd
number = 76

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# A program that checks whether a number is a prime number or not


num = 121
for i in range(2, num):
    if num % i == 0:
        print(num, " is not a prime number")
        break
else:
    print(num, " is a prime number")






