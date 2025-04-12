# PARAMETERS (TYPES OF PARAMETERS)
#1 default parameters
def student_info(name,batch="37R",instute="1000k coders"):
    print(name,batch,instute)
student_info("prashanth")   
student_info("ram")


#2-----ARGUMENTS IN FUNCTIONS---- 

#positional agruments
def function(names,age):
    print(names,age)
function("prashanth",23)  # AUTOMATICALLY the name = prashanth and age=21 is considered

# 3 ARBITARY ARGUMENTS
#  keyword  arguments  to overcome the  positional arguments
def person(names,age):
    print(names,age)
person(age=21,names="prashanth")  

# 3.1* asterisk is used  to print unkown no of arguments
def num(*a):
    print(a)
num(1,2,3,4,5,6)

def num(*a):
    print(a[3])
num(1,2,3,8,5,6)

#           `3.2 ** asterisk is used for keyvalue arguments
def names(**a):
    print(a)
names(first_name="amma",last_name=" prashanth" )    


#Return
def greet():
    print("hello")
    return
greet()
#if the function is returningn something then we have to print the function call also
def num(a):
    return 5*a
print(num(5))   # we should use print to get output which is returned value


# 
