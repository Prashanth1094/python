

#swapcase()
a="PrashanTH"
print(a.swapcase())

#isalpha()
a="prashanth"
print(a.isalpha())

a="prashanth123"
print(a.isalpha())

p="prashanth " #here there isn a space
print(p.isalpha())

#isdigit()

a="1236548"
print(a.isdigit())


a="123 6548" #space
print(a.isdigit())

a="123nb6548"
print(a.isdigit())

#isalnum  (isalphanum)  to check both  alphabets and numbers or olny one
a="prashanth123"
print(a.isalnum())

a="ahvukj"
print(a.isalnum())

a="dfgh!"
print(a.isalnum())

#center(char,width)
a="prashanth"
print(a.center(20,"*"))

a="prashanth"
print(a.center(20,"-"))

#order()  ASCII value
print(ord("@"))
print(ord("A"))
print(ord("a"))
print(ord("0"))
print(ord("+"))
print(ord("0"))

#chr(int) to give ascii charater value
print(chr(22))

#split() seperator  
a="1,2,3,4,5,6,7,89,9"
print(a.split(","))

a="hello world"
print(a.split(" "))
a="1,1,2,3,6,5,4,7,8,9,85"
print(a.split(","))

#join(iterable)
l=["amma","prashanth"]
print("".join(l))

l=["amma","prashanth"]
print("-".join(l))

l=["amma","prashanth"]
print("*".join(l))
