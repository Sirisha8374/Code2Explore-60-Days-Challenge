import random
import math
import numpy as np
import pandas as pd

def generate_data(n):
    students = []
    for i in range(1, n+1):
        marks = random.randint(0, 100)
        attendance = random.randint(0, 100)
        assignment = random.randint(0, 50)
        students.append((i, marks, attendance, assignment))
    return students

def classify_students(dataF):
    categories = {}
    for _, row in dataF.iterrows():
        sid = int(row['student_id'])
        marks = row['marks']
        attendance = row['attendance']

        if marks < 40 or attendance < 50:
            categories[sid] = "At Risk"
        elif marks > 90 and attendance > 80:
            categories[sid] = "Top Performer"
        elif 71 <= marks <= 90:
            categories[sid] = "Good"
        elif 40 <= marks <= 70:
            categories[sid] = "Average"

    return categories

def analyse_data(dataF):
    marks_array = dataF['marks'].to_numpy()

    mean = sum(marks_array)/len(marks_array)
    median = np.median(marks_array)
    std = np.std(marks_array)
    correlation = np.corrcoef(dataF['marks'], dataF['attendance'])[0][1]
    min_m = min(marks_array)
    max_m = max(marks_array)
    if max_m != min_m:
        dataF['normalized_marks'] = [(x-min_m)/(max_m - min_m) for x in marks_array]
    else:
        dataF['normalized_marks'] = [0 for _ in marks_array]
    summary = (float(mean), float(std), int(max_m))
    return mean, median, std, correlation, summary


n = int(input("Enter number of students: "))
data = generate_data(n)
dataF = pd.DataFrame(data, columns = [
    'student_id', 'marks', 'attendance', 'assignment'
])

dataF['performance_index'] = dataF.apply(
    lambda row: (row['marks']*0.6 + row['assignment']*0.4)*math.log(row['attendance']+1), axis = 1
)
categories = classify_students(dataF)

mean, median, std, corr, summary = analyse_data(dataF)
consistency = std < 15
attendance_risk = len(dataF[dataF['attendance'] < 50])> 3
top_performers = list(categories.values()).count("Top Performer") >= 2

if consistency and not attendance_risk:
    insight = "Stable Academic System"
elif top_performers:
    insight = "Moderate Performance"
else:
    insight = "Critical Attention Required"

print("\n------- Student Data -------")
print(dataF)
print("\n------- Category -------")
for k, v in categories.items():
    print(f"Student {k}: {v}")
print("\n------- Statistics -------")
print(f"Average Marks: {mean}")
print(f"Median Marks: {median}")
print(f"Standard Deviation: {std}")
print(f"Correlation: {corr}")
print("\n------- Summary -------")
print(f"(Mean, std Dev, Max Marks) = {summary}")
print("\n------- Final insight -------")
print(insight)