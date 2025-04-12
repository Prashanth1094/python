# arthemetic operators
a=1
b=3
print(a+b)  # additions

a=47
b=38
print(a-b) # subtraction

a=38
b=484
print(a*b) # multiplication

a=464
b=3
print(a/b)  # division normal division

a=474
b=47
print(a%b) #  modulus divisionprints only reminder
 
a=636
b=68
print(a//b) # floor division only quotient 

 ##-----------assignment operators-------------------

a=54
a+=3  # a=+3 equals to a+=3 add assignment operator
print(a)

a=567
a-=34  # a-=33 equals to a=-34  sub assignment operators
print(a)

a=647
a*=5 
print(a) ##  multiplications assignment operator

a=647
a/=7 #  division assignment operators
print(a)

a=4748
a%=3   # modulus assignment operators prints only rem
print(a)

a=23525
a//=474 # floor assignment operators ony quotient
print(a)

#--------------------"LOGICAL OPERATORS---------------"  AND OR NOT
  #    AND 
print(True and True) # 1 ,1 =1;  0,1=0;and operations
print(True and False) 
print(0 and 1)
print(0 and 13)  # here first value is 0 so it will go with 0
print(1 and 5435) # here first vale is 1  (non zero) so it will goes with 5435 second value


#------or---
print(True or False)
print(False or True)
print(0 or 536) #  here 536 is printed because first value is a zero so goes with 536  it goes with non zero values
print(1 or 4648)# here it goes with first value 1 (non zero)
print(1 or 0) # goes with 1

#-----not-----
print(not(5>6))
print(not(1565>215))
print(not(not(5>6)))

#------bitwise operators-------

#       #---AND  ==   "&"
print(5&9)  #5=101  , 9=1001 goes with and operation with bitwise
print(55&65)

#  -----OR BITWISE------
print(5|6)
print(56|36)

#  ----NOT----- 
print(~9)
print(~56)


# XOR
a=8  # 8 =1000
b=5  # 5 = 101 hare it is dn with xor operations
print(a^b)

# << left shift
print(45<<2)  #we should convert  45 into -binary and then shift left side with 2 places
print(68<<5)


#--- Right shift------
print(737>>3)  # first we should convert into binary and then shifts right to 3 times value will be decreased
print(757>7)


#---- comparision operators------- prints in true or false like in boolean-------------

#   EQUAL  (=)
a = 6
b = 73
print(a == b)



#---NOT EQUAL---(!=)
a=8
b=37
print(a != b)

#---greater than  (>)
a=66
b=78
print(a>b)

#------less than---- (<)
a=57
b=768
print(a<b)


#-----greater than equal to >=
q=282
u=272
print(q>=u)
a=272
b=252
print(a>=b)

#less than or equal to <=
q=129
w=626
print(q<=w)


#------ membership operators---- (in and not in)  prints(true or false ) ;llike in booleans
a={1,3,4,5,6}
x=6
print(x in a)

a=[1,2,3,5,5]
x=8
print(x in a )

a=[564,3,4,55,3,2,45]
x=38
print(x not in a)

# in dict membership operators
a={"name":"prashanth","num":"123"}
print("name" in a) # only key values are checked


#----IDENTITY OPERATORS----- is and not is 
# IN PREMITIVE DATA TYPE
#----- IS----
x=4
y=4
print(x is y)   # x , y value is same so it is true  

x=234567
y=23456469  # x is not y so here it is false
print(x is y)    

#-- is not---
x=34525255254
y=36373
print(x is not y) # x is not equal to y so TRUE

# NON PREMITIVE DATA TYPE
a=[1,2,3,4,5,6]
b=[1,2,3,4,5,6]
print(a is b)  # false because the memory is not same because of stack and heap
print(id(a))
print(id(b))
