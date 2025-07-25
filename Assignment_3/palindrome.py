# check the no. is palindrome or not

# input no.
num=int(input("Enter Number:"))
original=num
rem=0

while  num!=0:
    mod=num%10
    rem=rem*10+mod
    num=num//10

# condition check
if original==rem:
    print("Given Number is Palindrome")
else:
    print("Given Number is not a Palindrome")
