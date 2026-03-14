n = int(input("Enter number of activity scores: "))
data = [0]*n
for i in range(n):
    data[i] = int(input(f"Enter score {i+1}: "))

print("Original Data : ",data)

lowList = []
mediumList = []
highList = []
criticalList = []

invalidCount = 0
validCount = 0
removed = 0

for i in data:
    if i < 0:
        invalidCount = invalidCount + 1
    else:
        validCount = validCount + 1
        if i <= 30:
            lowList.append(i)
        elif i <= 60:
            mediumList.append(i)
        elif i <= 100:
            highList.append(i)
        else:
            criticalList.append(i)

print("\nBefore personalized filtering: ")
print("Low Risk: ",lowList)
print("Medium Risk: ", mediumList)
print("High Risk: ", highList)
print("Critical Risk: ", criticalList)

name = (input("\nEnter your name: "))
print("Name: ",name)
d = len(name)
if d%2 == 0:
    removed = len(lowList)
    lowList = []
else:
    removed = len(criticalList)
    criticalList = []

print("\nAfter personalized filtering: ")
print("Low Risk: ", lowList)
print("Medium Risk: ", mediumList)
print("High Risk: ", highList)
print("Critical Risk: ", criticalList)

print("\nFinal Report: ")
print("Total Valid Entries: ", validCount)
print("Ignored Entries: ", invalidCount)
print("Removed due to Personalization: ", removed)
