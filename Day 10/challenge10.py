import random
import math
import numpy as np
import pandas as pd
import copy

def generate_data(n):
    data = []
    for i in range(n):
        student = {
            "id": i+1,
            "marks": random.randint(40, 100),
            "attendance": random.randint(50, 100),
            "scores": [random.randint(10, 25), random.randint(10, 25)]
        }
        data.append(student)
    return data

def mutate_data(data, roll_no):
    mod = roll_no % 3
    if mod == 0:
        mod = 1

    for i in range(len(data)):
        if i % mod == 0:
            data[i]["marks"] += math.sqrt(data[i]["marks"])
            data[i]["scores"][0] += 5
            data[i]["attendance"] -= 5
    return data

def analyze(dataf):
    marks = dataf["marks"].to_numpy()
    mean = sum(marks)/len(marks)
    median = np.median(marks)
    std = np.std(marks)
    return mean, median, std

def calculate_drift(original, modified):
    return abs(original-modified)

n = random.randint(10, 15)
data = generate_data(n)

roll_no = int(input("Enter roll number: "))

shallow = data.copy()
deep = copy.deepcopy(data)

#convert original to DataFrame
df_original = pd.DataFrame(data)
orig_mean, orig_median, orig_std = analyze(df_original)

mutate_data(shallow, roll_no)
mutate_data(deep, roll_no)

df_shallow = pd.DataFrame(shallow)
df_deep = pd.DataFrame(deep)

mean_shallow, _, std_shallow = analyze(df_shallow)
mean_deep, _, std_deep = analyze(df_deep)

drift_shallow = calculate_drift(orig_mean, mean_shallow)
drift_deep = calculate_drift(orig_mean, mean_deep)

original_after = pd.DataFrame(data)
copy_failure = data != deep

threshold = 5

if copy_failure:
    result = "Copy Failure Detected"
elif drift_shallow > threshold:
    result = "Critical Drift"
elif drift_shallow > 2:
    result = "Minor Drift"
else:
    result = "Stable Data"


print("\n===== Original DataFrame =====")
print(df_original)

print("\n===== Shallow Copy =====")
print(df_shallow)

print("\n===== Deep Copy =====")
print(df_deep)

print("\n===== Analysis =====")
print("Original Mean: ", float(orig_mean))
print("Shallow Mean: ", float(mean_shallow))
print("Deep Mean: ", float(mean_deep))

print("\nDrift (Shallow): ", float(drift_shallow))
print("Drift (Deep): ", float(drift_deep))

if copy_failure:
    print("\nShallow copy affected original data!")
else:
    print("\nOriginal data remained unchanged.")

summary = (float(orig_mean), float(drift_shallow), float(orig_std))
print("\nSummary (mean, drift, std_dev):", summary)

print("\n===== Final result =====")
print(result)

