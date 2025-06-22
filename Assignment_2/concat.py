# input 2 strings and concatenate them and store in another variable
# perform generally used string method


str1=input("Enter First Word:")
str2=input("Enter Second Word:")
combine=str1+str2

print("Combined Word:",combine)
print("Converts all uppercase characters in a string into lowercase:",combine.lower())
print("Converts all lowercase characters in a string into uppercase:",combine.upper())

print("Convert string to title case:",combine.title())
print("Swap the cases of all characters in a string:",combine.swapcase())

print("Convert the first character of a string to uppercase:",combine.capitalize())
print("Converts string to lower case:",combine.casefold())

print("Pad the string with the specified character:",combine.center(60,"-"))
print("Count of 'a' in Word:",combine.count("a"))

print("Check if Word starts with 'p' or not:",combine.startswith("H"))
print("Check if Word ends with 'n' or not:",combine.endswith("N"))

print("Find python in given string from index 5 and find till the end:",combine.find("python",5))
print("Print True if special characters is present in string:",combine.isalnum())

print("Returns True if all characters in the string are alphabets:",combine.isdigit())
print("Returns True if all characters in the string are numeric characters:",combine.isnumeric())

print("Returns True if all characters in the string are whitespace characters:",combine.isspace())
print("Replace a with @ in the String:",combine.replace("a","@"))
