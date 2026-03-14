n = int(input("Enter number of students: "))
marks = [0]*n
print("Enter each student marks: ")
for i in range(n):
    marks[i] = int(input((f"Enter student {i+1} marks: ")))
print("Marks: ", marks)

name = "Sirisha"
length = len(name)  #length = 7

start = length*10   #start = 70
end = start + 9     #end = 70+9 = 70, that is checking in the range 70-79

valid = 0
failed = 0
for i in range(n):
    x = marks[i]
    if x >= start and x <= end:
        if x+5 <= 100:
            x = x+5

    if x >= 90 and x <= 100:
        print(f"{x} -> Excellent")
        valid = valid+1
    elif x >=75 and x <= 89:
        print(f"{x} -> Very good")
        valid = valid + 1
    elif x >= 60 and x <= 74:
        print(f"{x} -> Good")
        valid = valid + 1
    elif x >= 40 and x <= 59:
        print(f"{x} -> Average")
        valid = valid + 1
    elif x >= 0 and x <= 39:
        print(f"{x} -> Fail")
        valid = valid + 1
        failed = failed + 1
    else:
        print(f"{x} -> Invalid")
print("Final Summary:")
print("Total valid students: ", valid)
print("Total failed students: ", failed)

