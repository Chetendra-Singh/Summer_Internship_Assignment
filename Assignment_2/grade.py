#write a program to take student name,class and marks and
#find total marks and percentage and
#print name,class,percentage and also give grade acc. to marks


# personal details

name=input("enter your name:")
class_name=int(input("enter your class:"))

# subject details
sum = 0
subject_list=[]
marks_list=[]
for i in range(0,5):
        sub=input(f"enter {i+1} subject name:")
        marks=int(input(f"enter {i+1} subject marks:"))
        sum+=marks
        subject_list.append(sub)
        marks_list.append(marks)


#calculation of percentage
result = (sum / 500) * 100

#output
print("...............")
print("Name of Student:",name.upper())

print("Class:",class_name)
print("Percentage:",result)


# Grading
if result >= 60:
    print("Grade A")
elif result >=50:
    print("Grade B")
elif result >=40:
    print("Grade C")
elif result >=33:
    print("Grade D")
else:print("Fail")
