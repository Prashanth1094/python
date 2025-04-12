# def loan():
#     UserName=input("Enter a Name ")
#     Gender=input("Enter your Gender ")
#     Age=int(input("Enter an Age "))
#     if(Age>18 or Age<58):
#         print("You are eligible for loan")

#         return
#         Income=int(input("Enter your Income "))
#         if(Income>350000):
#             print("You have  offer")
#             return
#             CIBILScore=int(input("Enter your CIBIL Score ")) 
#             if(CIBILScore>300 or CIBILScore<650):
#                 print("You are is up to 40% to 90% of  income")
#             else:
#                 print("You have no cibil")
#         else:
#             print("You have no offer")
#     else:
#         print("You are age is not eligible for loan")
# loan()        
def check_eligibility(age, income, cibil):
    # Conditions
    if age < 18 or age > 58:
        print("NO LOAN OFFERS AVAILABLE FOR THE PEOPLE WHO'S AGE IS BELOW 18 AND ABOVE 58.")
        exit()
    if income < 350000:
        print("NO OFFERS FOUND")
        exit()
    if cibil < 300 or cibil > 900:
        print("ELIGIBLE FOR LOAN")
        exit()

# Example Usage
name=input("Enter Name: ")
gender=input("Enter your gender")
age = int(input("Enter Age: "))

income = int(input("Enter Annual Income: "))
cibil = int(input("Enter CIBIL Score: "))

check_eligibility(age, income, cibil)
