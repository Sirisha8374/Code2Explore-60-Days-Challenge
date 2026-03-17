n = int(input("Enter number of transactions made in a day: "))
trans = [0]*n
for i in range(n):
    trans[i] = int(input(f"Enter transaction amount {i+1}: "))

categorize = {
    "normal": [], "large":[], "highRisk":[], "invalid": []
}

for i in trans:
    if i <= 0:
        categorize["invalid"] = categorize["invalid"] + [i]
    elif i >= 1 and i <= 500:
        categorize["normal"] = categorize["normal"] + [i]
    elif i >= 501 and i <= 2000:
        categorize["large"] = categorize["large"] + [i]
    else:
        categorize["highRisk"] = categorize["highRisk"] + [i]

valid = [i for i in trans if i > 0]

no_of_trans = len(trans)
total_trans_amount = sum(valid)

freq = no_of_trans > 5
large_spending = total_trans_amount > 5000
isSuspicious = len(categorize["highRisk"]) >= 3

if isSuspicious or (freq and large_spending):
    risk = "High Risk"
elif freq or large_spending:
    risk = "Moderate Risk"
else:
    risk = "Low Risk"


print("Categorized transactions: ", categorize)
print()
print("Summary:")
print("Total transaction value: ", total_trans_amount)
print("Total number of transactions: ", no_of_trans)
print("Final Risk Level: ", risk)
