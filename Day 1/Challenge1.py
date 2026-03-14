name = input("Enter your Full name: ")
email = input("Enter your email: ")
mobile = input("Enter your mobile number: ")
age = int(input("Enter your age: "))
nameLength = len(name)
mobileLength = len(mobile)
validName = False
if name.count(" ") >= 1 and name[0] != " " and name[nameLength-1] != " ":
    validName = True
validEmail = False
if email.count("@") >= 1 and email.count(".") >= 1 and email[0] != "@":
    validEmail = True
validMobile = False
if mobileLength == 10 and mobile.isdigit() == True and mobile[0] != "0":
    validMobile = True
validAge = False
if age >= 18 and age <= 60:
    validAge= True

if validName and validEmail and validMobile and validAge:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")