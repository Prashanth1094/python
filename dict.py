# dict={"name":"prashanth","age":21,"skills":["python","java","Django"]}
# print(dict["skills"][2])
# print(len(dict))
# #get()
# print(dict.get("skills"))
# print(dict.keys())#keys() method
# print(dict.values()) #values()
# print(dict.items()) #items()
# dict["age"]=23# change
# print(dict)
# dict.update({"name":"prashanthamma"})#update 
# print(dict)
# #adding
# dict["year"]=2003#added 
# print(dict)
# dict.pop("year")
# del dict["age"]
# print(dict)

# dict={"names":"prashanth","age":21,"year":2003,"lang":"tel"}
# for i in dict:
#     print(dict[i])



#Write a program to merge two dictionaries.
dict1={"name":"prashanth","age":23}
dict2={"n":"qwerty","a":20}
dict1.update(dict2)
print(dict1)      

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict1.update(dict2)
print(dict1)
