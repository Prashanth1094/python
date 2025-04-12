# # for loop is used in when the iterators are known 1 to 50
# for i in range(1,51,1):
#     print(i,"hello")

# #basic step is 1 by default value
# for i in range(1,51):
#     print(i,"hello")

# # loop without start(index value = 0)  and step because stating and step value is 1
# for i in range(20): # but here start at index by default 0
#     print("hello")

# # decending order
# n= int(input("enter a number "))
# for i in range(n,0,-1):
#     print(i)

# # even odd number
# n=int(input("enter any number "))
# for i in range (1,n+1):
#     if i%2==0:
#         print(i,"even")
# #prime numbers

# num=int(input("Enter a number "))
# fact=0
# for i in  range(1,num+1,1):
#     if num%i==0:
#         fact=fact+1
# if fact == 2:    
#     print(num,"prime number")
# else:
#     print(num," not prime number")  

# # prime numbers with factors     

n= int(input("Enter a number "))
fact=0
print("factors of",n,"are")
for i  in range(1,n+1):
    if n%i==0:
        fact=fact+1
        print(i,end=",")
if fact==2:
    print(i,"prime number")        
else:
    print(i,"not prime number")

# #print the tables from 1-5 with multiplying of even numbers

# n=int(input("enter any number"))
# for i in range(1,n+1):
#     for j in range(2,21,2):
#         print(i,"X",j,"=",i*j)
   

                