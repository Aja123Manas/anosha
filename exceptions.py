try:
    print(x)
except:
 print("NameError occurred")
finally:
    print("success")

try:
    num1 = 20
    num2 = 10
    print(num1 / num2)
except:
    print("ZeroDivisionError occurred")
finally:
    print("success")

# User-defined function
try:
    def sum(first, second):
        return first + second
except:
    print("Exception occurred")

print(sum(10,20))