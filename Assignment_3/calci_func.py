# function for basic math operations like add,subtract,multiply and divide
#and take 2 input from user and print output


print("Enter the operation you want to perform:")
print('''Press
+ for add
- for subtract
* for multiply
/ for divide
''')
opr=input("Enter the operation you want to perform:")

#input number
num1=float(input("Enter First Number:"))
num2=float(input("Enter Second Number:"))

# Function Definition
def calci(num1,num2,opr):
    if opr=="+":
        add=num1+num2
        print(f"Sum of {num1} and {num2}:",add)
    elif opr=="-":
        sub=num1-num2
        print(f"Subtraction of {num1} and {num2}:",sub)
    elif opr=="*":
        multi=num1*num2
        print(f"Multiplication of {num1} and {num2} : {multi}")
    elif opr=="/":
        if num2==0:
            print("Error! number 2 cannot be 0,please change your input")
        else:
            div=num1/num2
            print(f"Division of {num1} and {num2}:",div)
    else:print("Error! please enter a valid operation")

# function call
calci(num1,num2,opr)