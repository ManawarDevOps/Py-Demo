import sys

def addition(num1, num2):
    add = num1 + num2
    return add

def substraction(num1, num2):
    sub = num1 - num2
    return sub

def multiplication(num1, num2):
    mul = num1 * num2
    return mul

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])


if operation == "add":
    output = addition(num1, num2)
    print(output)
elif operation == "sub":
      output = substraction(num1, num2)
      print(output)
elif operation == "mul":
      output = multiplication(num1, num2)
      print(output)
else:
    print("Invalid operation")
    
      
