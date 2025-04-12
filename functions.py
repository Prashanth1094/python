# # Write a function that takes two numbers as input and performs addition.
# def numbers():
#     a=int(input("enter any number: "))
#     b=int(input("enter any number:"))
#     print(a+b)
# numbers()

# #Create a function that accepts a name and displays a personalized greeting
# def name(a):
#     print("hi" , a)
#     print("welcome")
# name("prashanth") 

# #Write a function to calculate the square of a given number and show the result.

# def square(num):
#     result=num ** 2
#     print("the square of the num is result",result)
# square(5)

# #Write a function to multiply two numbers and display the result
# def mul(a,b):
#     result=a*b
#     print("multiplication of two numbers = ",result)
# mul(5,6)    

# #Create a function that takes a string as input and prints the length of the string
# def string():
#     a=input("enter any string  ")
#     lenght=len(a)
#     print("lenght of the string  ",lenght)
# string()    


# def sample(a,b):
#     sum=a+b
#     return sum
# print(sample(1,555))

num=int(input("enter any number"))
def even_odd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
print(even_odd(num))


#Task: perform basic mathematical operations (+,-,,/,//,%,*) using def function and lambda functions

num1=int(input("enter any number"))
num2=int(input("enter any number"))
def operations(num1,num2):
    add=num1+num2
    sub=num1-num2
    div=num1/num2
    floor_div=num1//num2
    mod_div=num1%num2
    mul=num1*num2
    return add,sub,mul,div,floor_div,mod_div,mul
results=operations(num1,num2)
print("Addition:",{results[0]})
print("Subtraction:", {results[1]})
print("Division:", {results[2]})
print("Floor Division:", {results[3]})
print("Modulo:",{results[4]})
print("Multiplication:", {results[5]})

x=int(input("enter any number"))
y=int(input("enter any number"))
add=lambda X,y:x+y
sub=lambda x,y:x-y
mul=lambda x,y:x*y
div=lambda x,y:x%y
print("ADDITION",add(x,y))
print("SUBTRACTION",sub(x,y))
print("MULTIPLICATION",mul(x,y))
print("DIVISION",div(x,y))











