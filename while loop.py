num=int(input("enter a number"))
count=0
while num>=100:
      count+=1
      num=num+1
print(count)      


# Task 1 : Find the second prime of the given number ?By using the continue control statement

# num = int(input("Enter a number: "))
# prime_not_found = True

# while prime_not_found:
#     num += 1
#     fact = 0
#     for i in range(1, num + 2):  # Removed the unnecessary 1 as the step
#         if num % i == 0:
#             fact += 1
#     if fact == 2:  # A prime number has exactly two factors (1 and itself)
#         prime_not_found = False
#         print(num, "is next prime")
        



# #By using break control statement
# #Task 2 : Break the loop if  Condition matches with the give number?        
# a=int(input("enter a number between 0 to 100 "))
# for i in range(50):
#         print(i)
#         if i==a:
#          break


# #Task 3 : print the numbers from 1 to 100, but it should not print multiples of 3? By using the continue control statement

for i in range(1,101):
      if i%3 == 0:
          continue
      print(i)  


           


