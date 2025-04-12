# n={1,2,3,6,5,4,7,8,9,66,55,18}
# b=int(input("enter a element remove from the list"))
# n.discard(b)
# a1=[n]
# #a1.add(n)
# print(a1)

# # To day topic: sets,frozenset
# Task:
#    1.Practice all Methods 
# 2. Take a set of no,take element from the user remove that element  from existing set  and store in new set.
# Reasearch Topic: Check whether the below methods are working for set or not. i.e. issubset(),issuperset(),isdisjoined()
n = {1, 2, 3, 6, 5, 4, 7, 8, 9, 66, 55, 18}

b = int(input("Enter an element to remove from the set: "))  # Convert input to int
if b in n:

     n.remove(b)  # Removes b if it exists, does nothing if it doesn’t
     print(n)
    #  a1 = [n]  # Store the modified set inside a list

    #  print(a1)


