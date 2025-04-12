# num=123456786886
# while num!=0:
#     last_digit=num%10
#     fact=0
#     for i in range(1,last_digit+1):
#         if last_digit%i==0:
#             fact+=1
#     if fact==2:
#         print(last_digit,"prime")
#     num=num//10  


# num=123456786886
# while num!=0:
#     last_digit=num%10
#     fact=0
#     for i in range(1,last_digit+1):
#         if last_digit%i==0:
#             fact+=1
#     if fact==2:
#         print(last_digit,"prime")
#     num=num//10  



#Armstrong number  ==153=1**3+5**3+3**3

num=153
temp=num
length=0
while temp!=0:
   a=temp%10
   length+=1
sum=0   
temp1=num
while temp1!=0:
   last_digit=temp
   sum=sum+last_digit**length
   temp1//10
print(sum)   


# print the position of the number
num=12347753877  #position 5
print(str(num)[5]) #  by method using string

num=3448653585465
pos=int(input("enter the position"))
length=0
while num!=0:
   digit=num//10
   length+=1
   if length==pos:
      print(pos)

