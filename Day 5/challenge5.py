nums = []
n = int(input("Enter number of requests: "))

for i in range(n):
    x = int(input("Enter request value: "))
    nums.append(x)
print("Original Data: ", nums)
lowDemand = []
moderateDemand = []
highDemand = []
invalidRequests = []

validCount = 0
removedCount = 0

for i in nums:
    if i < 0:
        invalidRequests.append(i)
    else:
        validCount += 1
        if i == 0:
            continue
        elif i >= 1 and i <= 20:
            lowDemand.append(i)
        elif i >= 21 and i <= 50:
            moderateDemand.append(i)
        else:
            highDemand.append(i)
print("\nCategorization Before personalization: ")
print("Low Demand: ", lowDemand)
print("Moderate Demand: ", moderateDemand)
print("High Demand: ", highDemand)
print("Invalid Requests: ", invalidRequests)

L = int(input("\nEnter last 5 digits of your registration number: "))
print("Last 5 digits of registration number is ",L)

PLI = L % 3
print("Personalized Logic Index: ",PLI)

if PLI == 0:
    removedCount = len(lowDemand)
    lowDemand = []
elif PLI == 1:
    removedCount = len(moderateDemand)
    moderateDemand = []
else:
    removedCount = len(highDemand)
    highDemand = []

print("\nAfter personalization: ")
print("Low Demand: ", lowDemand)
print("Moderate Demand: ", moderateDemand)
print("High Demand: ", highDemand)
print("Invalid Requests: ", invalidRequests)

print("\nFinal Report:")
print("Total valid requests: ", validCount)
print("Removed Count: ", removedCount)


