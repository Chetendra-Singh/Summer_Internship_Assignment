num1 = float(input("Enter the first number:"))
num2 = float(input("enter the second number:"))
print("choose one operation from below:")
print("addition","subtraction","multiplication","division","modulus","exponential",sep=",")
a=input("enter the operation you want to perform:")

if a=="addition":
    sum=num1+num2
    print(f"Sum of {num1} and {num2} is:", sum)
elif a=="subtraction":
    sub = num1 - num2
    print(f"Subtraction of {num1} and {num2} is:", sub)
elif a=="multiplication":
    multi = num1*num2
    print(f"Multiplication of {num1} and {num2} is:", multi)
elif a=="division":
    div = num1/num2
    print(f"Divison of {num1} and {num2} is:", div)
elif a=="modulus":
    mod = num1%num2
    print(f"Modulus of {num1} and {num2} is:", mod)
elif a=="exponential":
    exp = num1**num2
    print(f"Exponential of {num1} and {num2} is:", exp)
else:
    print("Wrong Choice,Please Choose a Valid Choice.")
