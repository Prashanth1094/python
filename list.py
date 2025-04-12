# # # # to search a numberin the list
# # # list=[1,2,3,4,5,6,7,8,9]
# # # dup=[]
# # # num=int(input("Enter the number to be searched in the list: "))
# # # target=6
# # # for i in range(len(list)):
# # #     if list[i]==num:
# # #         dup.append(target)
# # #     else:
# # #         dup.append(list[i])  
# # # print(dup)    

# # # to find the items in  list by index
# # # list=[1,2,3,4,5,6,7,8,9]
# # # b=int(input("enter the values to 0-8 5"))
# # # print(list[b])

# # # to find the items in  list for known elements
# # # a=[1,8,6,9,4,7,5,9,"hello","hi",True,25.6]
# # # for i in range(1,len(a)-1):
# # #     print(a[i])

# # # a=[1,8,6,9,4,7,5,9,"hello","hi",True,25.6]
# # # for i in range(len(a)-1,-14,-1):
# # #     print(a[i])

# # #append()  add item at last
# # a=[1,8,6,9,4,7,5,9,"hello","hi",True,25.6]
# # a.append(40)
# # print(a)

# # #copy we should store in duplicate
# # a=[1,8,6,9,4,7,5,9,"hello","hi",True,25.6]
# # dup=a.copy()
# # print(dup)

# # #count()
# # a=[1,8,6,9,4,7,5,9,"hello","hi",True,25.6]
# # print(a.count(0))
# # print(a.count(9))

# # #extend()
# # a=[1,8,6,9,4,7,5,9,"hello","hi",True,25.6]
# # a.extend([10,20,30,66,55,44,7,8,])
# # print(a)
 
# # #index()
# # a= [1,8,6,9,4,4,5,47,5,9,"hello","hi",True,25.6]
# # print(a.index(4))

# # #1.implement the count method on a list by taking input from user without using actual method.
# # a=[1,2,3,54,6,8,9,0,11,21,12,131,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,23,34,54,6,3,3,2,7,1,44,45,46,47,48,49,50]
# # b=int(input("enter the values 0-50 to count:"))
# # print(a.count(b))




# # # #2.implement the copy method on a list just as the above condition.
# # # a=[1,2,3,54,6,8,9,0,11,216,37,38,39,40,41,42,43,23,34,54,6,3,3,2,7,1,44,45,46,47,48,49,50]
# # # b=a.copy()
# # # print(b)

# # #pop() itremoves the index elements
# # a=[1,2,3,4,5,67,8,9,10]
# # b=a.pop()
# # print(b)

# # b=[1,2,4,56,4,2,1]
# # b.pop(5)
# # print(b)

# # #remove() it remove the element value  from the list
# # a=[1,2,3,4,5,6,7,8,9,10]
# # a.remove(5)
# # print(a)

# # #reverse
# # a=[1,2,3,4,5,6,78]
# # a.reverse()
# # print(a)

# # #sort()
# # a=[1,8,3,5,2,6,9,4,3,66,8,33]
# # a.sort()
# # print(a)

# # #max() , min()
# # a=[1,8,3,5,2,6,9,4,3,66,8,33]
# # b=max(a)
# # c=min(a)
# # print(b)
# # print(c)

# # #11 divisible
# # num=[11,34,44,22,65,77,90]
# # for i in range(0,len(num)):
# #     if num[i]%11==0:
# #         print(num[i])


# # #not divisible by 11

# # num=[11,34,44,22,65,77,90]        
# # for i in range(0,len(num)):
# #     if num[i]%11!=0:
# #         print(num[i])

# #1)Implement the program that to print true when the first and last element in the list was even, else print false.
# n=[1,4,2,4,455,64,634,6346,46,22,23,45,32,2]
# if (n[0]%2==0)and (n[-1]%2==0):
#     print("true")
# else:
#     print("false")    



# #2) implement the program to create a function which performs the count method. Without using any methods.
# def num():
#     n=[1,2,3,54,6,7,8,9,6,4,33,2,2,7]
#     element=7
#     count=0
#     for i in range(0,len(n)):
#         if n[i]==element:
#             count=count+1
#     print(count)
# num()            





#write a program to print the prime numbers in the new list from existing list.
# a=[8,5,69,25,8,4,7,2,13,53]
# prime=[]
# for i in range(0,len(a),1):
#     number=a[i]
#     fact=0
#     for j in range(1,number+1):
#         if number%j==0:
#          fact=fact+1
#     if fact==2:
#         prime.append(number)
# print(prime)


a = [8, 5, 69, 25, 8, 4, 7, 2, 13, 53]
prime = []
non_prime=[]
for num in a:
    fact=0
    for i in range(1,num+1):
        if num%i==0:
            fact=fact+1
    if fact==2:
        prime.append(num)
    else:
        non_prime.append(num)        
print(prime,"prime")
print(non_prime,"non prime")

# for number in a:  # Loop through each number in the list
#     fact = 0  # Reset fact for each number
#     for j in range(1, number + 1):
#         if number % j == 0:
#             fact += 1
#     if fact == 2:  # Prime numbers have exactly 2 factors (1 and itself)
#         prime.append(number)

# print(prime)
