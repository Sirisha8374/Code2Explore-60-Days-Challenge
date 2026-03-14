studID = input("Enter your student ID: ")
email = input("Enter your email ID: ")
password = input("Enter your password: ")
referralCode = input("Enter Referral Code: ")
LenOfStudID = len(studID)
LenOfEmail = len(email)
LenOfPassword = len(password)
LenOfCode = len(referralCode)

validStudID = False
if LenOfStudID == 7 and studID[0:3] == "CSE" and studID[3] == '-' and studID[4].isdigit() and studID[5].isdigit() and studID[6].isdigit():
    validStudID = True

validEmail = False
if email.count('@') >= 1 and email[0] != '@' and email[LenOfEmail-1] != '@' and email[LenOfEmail-4:LenOfEmail] == ".edu":
    validEmail = True

validPassword = False
if LenOfPassword >= 8 and (password[0] >= 'A' and password[0] <= 'Z') and password.count('0')+password.count('1')+password.count('2')+password.count('3')+password.count('4')+password.count('5')+password.count('6')+password.count('7')+password.count('8')+password.count('9') >= 1:
    validPassword = True

validCode = False
if referralCode[0:3] == "REF" and referralCode[3].isdigit() and referralCode[4].isdigit() and referralCode[LenOfCode-1] == "@":
    validCode = True

if validStudID and validEmail and validPassword and validCode:
    print("APPROVED")
else:
    print("REJECTED")