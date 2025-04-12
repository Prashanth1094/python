#try
#except
#else
#finally

try:
    s1="hello"
    s2=1
    q=s1+s2
except Exception as error:
    print("invaid",error)
else:
    print(q)
finally:
    print("final output")    


# FORMATTED STRINGS  (f)
name="Prashanth"
print(f"my name is {name}")   

def details(name,age,addhress):
    return f"details of name :{name},age is {age},addhress{addhress} "
print(details("prashanth",23,"nagaram"))    