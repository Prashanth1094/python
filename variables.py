# a=4
# print(id(a))
# print(a)
# z=4.5
# print(id(z))
# print(z)
# q="qwerty"
# print(q)
# s=True
# print(id(s))
# print(s)
# w=2
# w=4 # 2 is muted it will go to garbage value
# print(w)

num=123456786886
while num!=0:
    last_digit=num%10
    fact=0
    for i in range(1,last_digit+1):
        if last_digit%i==0:
            fact+=1
    if fact==2:
        print(last_digit,"prime")
    num=num//10  

# num = 123456786886
# while num != 0:
#     last_digit = num % 10
#     fact = 0
#     for i in range(1, last_digit + 1):
#         if last_digit % i == 0:
#             fact += 1
#     if fact == 2:
#         print(last_digit, "is prime")
    
#     num = num // 10  # Remove the last digit
