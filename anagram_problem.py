s1="study"
s2="dusty"
def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False    
    else:
        s1=s1.lower()
        s2=s2.lower()
        s1=sorted(s1)
        s2=sorted(s2)
        if s1==s2:
            return True
        else:
            return False
print(anagram(s1,s2))


# indexind or slicing
l1=[1,2,3,4,5,67,8,9,0]
print(l1[::])
print(l1[2::])
print(l1[1::2])
l2=l1[0:7:1]
print(l2)