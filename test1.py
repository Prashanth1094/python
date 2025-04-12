# 1. Write a program to find the average of numbers in a list.
#    Sample Input: [4, 6, 8]       Expected Output: 6.0
list=[4, 6, 8]
sum=0
for i in list:
    sum=sum+i
avg=sum/len(list)    
print(avg)

# 2 Write a program to count how many times a number appears in a list.
list=[1,2,3,4,63,2,1,4,5,2,1,4,5,2,1,4,5,2,1,4,5]
temp=[]
for i in list:
    if i not in temp:
        temp.append(i)
for i in temp:
    count=0
    for j in list:
        if i==j:
            count+=1
    print(f"{i} appears {count} times")   

#3. Write a program to get numbers greater than 5 from a list.
list=[1,2,3,3,4,5,6,7,8,4,208,55,6]
temp=[]
for i in list:
    if i>5:
      temp.append(i)
print("the num greater than 5 are ",temp)


# 4 Write a program to replace all 0s with 1s in a list.
list=[1,2,3,0,1,0,1,0,2,1,0,1,0,2,1,0,1,0,2,1]
temp=[]
for i in list:
    if i==0:
        temp.append(1)
    else:
        temp.append(i)
print(temp)   

# 5 Write a program to print a list in reverse order
list=[1,2,3,4,5,6,7,8,9,0]
rev=list[::-1]
print(rev)

#6. Write a program to merge two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict1.update(dict2)
print(dict1)  

#7. Write a program to create a dictionary from two lists (one for keys and one for values).
list1=["name","age","address"]
list2=["prashatnth",23,"nagaram"]
dict={}
for i in list1:
    for j in list2:
        dict[i]=j
        list2.remove(j)
        break
print(dict)    

#8.Write a program to print all values from a dictionary
dict={"name":"prashanth","age":23,"address":"nagaram"}
for i in dict:
  print(dict[i])
 #9. Write a program to get the length of a dictionary
dict={"name":"prashanth","age":23,"address":"nagaram"} 
print(len(dict))

#10. Write a program to list all items in a dictionary as tuples
dict={"name":"prashanth","age":23,"address":"nagaram"}
temp=[]
for i in dict:
    temp+=((i,dict[i]),)
print(temp)    

#11. Write a program to find the square of a number
def square():
    num=int(input("enter a number"))
    return num*num
print("square is",square())

#12. Write a program to find the sum of digits of a number.
num=int(input("enter a number"))
sum=0
for i in str(num):
    sum+=int(i)
print("the sum of digits are",sum)    

#13. Write a program to find the smallest divisor of a number greater than 1.
num=12
for i in range(2,num+1):
    if num%i==0:
        print("the smallest divisor of a number",i)
        break
#14. Write a program to print the multiplication table of a number up to 10
num=int(input("enter a number"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)

#. Write a program to count the number of even digits in a number.
num=int(input("enter a number"))
count=0
for i in str(num):
    if int(i)%2==0:
        count+=1
print("count the number of even digits",count)      
