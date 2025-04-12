#.Write a Python program that takes an integer as input and prints whether it is even or odd.

num=int(input("Enter a Number "))
if(num%2==0):
    print("The number is even")
else:
    print("The number is odd")

Write a program that takes two numbers as input and prints the larger number. If they are equal, print "Both numbers are equal".

a=int(input("enter any  number: "))
b=int(input("enter any number: "))
if(a>b):
    print("a is greater number")
elif(a==b):
    print("a equal to b")
else:
    print("b is greater than a")  

  .Write a Python program that asks the user for a number and prints whether it is positive, negative, or zero 
num=int(input("enter any number"))
if(num>0):
    print("it is a positive number")
elif(num==0):
    print("it is a zero")
else:
    print("it is a negative number")        

  Write a program that asks the user for their age. If the age is 18 or above, print "You are eligible to vote", otherwise print "You are not eligible to vote".
age=int(input("enter your age:"))
if(age>=18):
    print("Your are eligibile for vote")
else:
    print("Your are not eligibile for votre")    


Write a program that takes a student's marks (out of 100) and prints:
"Pass" if marks are 40 or more
"Fail" if marks are less than 40
def students(names,marks):
    if (marks>40 and marks<=100):
        print("the student is pass")
    else:    
        print("the student is fail")
prashanth=students("prashanth",50) 
print("prashanth")
# OR
marks = int(input("Enter your marks: "))
if (marks >= 40 and marks <= 100):
    print("Pass")
else:
    print("Fail")
