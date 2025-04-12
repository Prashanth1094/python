# # # n="my name is prashanth"
# # # a=n.split(" ")
# # # for i in range(len(a)):
# # #     if a[i]=="name":
# # #         print(len(a[i]))


# # #to count vowels and consonents
# # name="amma prashanth"
# # name=name.lower()
# # v_count=0
# # c_count=0
# # for i in range(0,len(name)):
# #     if name[i]=="a"or name[i]=="e" or name[i]=="i"or name[i]=="o" or name[i]=="u":
# #         v_count+=1
# #     else:    
# #         c_count+=1
# # print("no of vowels",v_count)        
# # print("no of consonents",c_count)   

# # #or
# # a="amma prashanth python"
# # vowels="aeiouAEIOU"
# # v_count=0
# # c_count=0
# # for i in range(len(a)):
# #     if a[i] in vowels:
# #         v_count+=1
# #     else:
# #         c_count+=1
# # print("no of vowels",v_count)        
# # print("no of consonents",c_count)      

# # #code for not print duplicates

# # code="python is a high level language and python oops concepted language"
# # m=code.split(" ")
# # for i in range(len(m)):
# #     a=m[i]
# #     if m.count(a)==1:
# #         print(m[i])

# # a="hello"
# # b=[]
# # for i in range(len(a)):
# #     b.append(a[i])
# # print(b)


# # #to print diplicate most occurence
# # name="python is programming language and python is oops baased language"
# # c=name.split(" ")
# # for i in range(len(c)):
# #     p=c[i]
# #     if c.count(p)>1:
# #         print(p)

# # Take  a paragraph check the count of words, if count is more than 100, print valid ; else invalid
# name="hello everyone good after Hello everyone, good afternoon! My name is Amma Prashanth. I hail from Warangal and am currently pursuing my B.Tech final year in Electronics and Communication Engineering. Coming to my technical skills, I have experience in Python and HTML. During my academics, I have worked on projects, including 'Home Automation using ESP32 with Blynk Application.' The main aim of my project is to save power and improve energy efficiency.Hello everyone, good afternoon! My name is Amma Prashanth. I hail from Warangal and am currently pursuing my B.Tech final year in Electronics and Communication Engineering. Coming to my technical skills, I have experience in Python and HTML. During my academics, I have worked on projects, including Home Automation using ESP32 with Blynk Application. The main aim of my project is to save power and improve energy efficiency.Hello everyone, good afternoon! My name is Amma Prashanth. I hail from Warangal and am currently pursuing my B.Tech final year in Electronics and Communication Engineering. Coming to my technical skills, I have experience in Python and HTML. During my academics, I have worked on projects, including Home Automation using ESP32 with Blynk Application. The main aim of my project is to save power and improve energy efficiency."
# c=name.split(" ")
# for i in range(len(c)):
#     if c.count(c[i])==100:
#         print("valid")
#         break
#     else:
#       print("not valid")
#       break
# #Task2: take a input with both upper and lower cases characters count the no.of  uppercases and lower cases without using any methods
# a="abcdefABCDEFm"
# upper=0
# lower=0
# for char in a:
#    if "A" <= char <= "Z":
#       upper+=1
#    else:
#     lower+=1
# print("uppercase",upper)    
# print("lowercase",lower)


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