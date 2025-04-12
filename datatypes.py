#non pemitive datatypes

#List []
a=[1,4,3,6,2,7,90,True,False] # list is a orderd collections which can be mutable
print(a)
a[2]= "hi"# hi is inserted at index 2
print(a)
print(type(a))


# Tuples ()
b=(5,8,6,9,2,4)  # orderd and immmutable
print(type(b))
#  print(tuples[3]="hi") hi is not inserted
print(b)

# Sets
dict={"moble_names":"iphone","fruits":"apples"} #collections of multiple properties (pair values)
print(dict)

set={2,4,6,8,1,3,4} # stores unorderd values and not allow dublicates o/p is not same as input
print(set)

w={1,3,5,7,"hi",True,False} #ony fasle can print and true is not printed in sets because here the 1 element is there  so 1 means true and 0 = fasle
print(w)
w1={True,56,3,5,6,False}
print(w1)


# Frozenset
y=frozenset([1,0,4,6,7,9,3,2,True,False,True,"hi"])    # true  and false cannot  be printed beause we already used 0 and 1
print(y)
a=([1,5,22,2,34,4432,2121]) # here it donesnot shows the set structure in output
print(a)