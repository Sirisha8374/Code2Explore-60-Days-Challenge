# Python Code2Xplore – 60 Day Challenge 🚀

This repository contains my solutions for the **Python Code2Xplore 60 Day Challenge**.

The objective of this challenge is to improve **Python programming skills, problem-solving ability, and consistency** by solving one coding challenge every day for 60 days.

Each day focuses on **real-world inspired problems**, input validation, logical thinking, and implementing personalized program logic.

---

## 📊 Progress

**Completed:** 8 / 60 Days
Note: It's skipped

I update this repository **daily** by adding the solution for the new challenge and updating this README.

---

# 📅 Challenge Log

| Day | Challenge Title | Description | Solution |
|-----|-----------------|-------------|----------|
| Day 01 | User Profile Validation System | Build a validation system that verifies full name, email, mobile number, and age based on strict conditions to determine if a user profile is valid. | [Challenge1.py](Day%201/Challenge1.py) |
| Day 02 | University Smart Registration System | Validate student registration details including Student ID format, university email, password rules, and referral code before approving the account. | [challenge2.py](Day%202/challenge2.py) |
| Day 03 | Student Result Analyzer | Analyze multiple student marks, categorize performance levels, apply personalized bonus logic based on name length, and generate a final performance summary. | [challenge3.py](Day%203/challenge3.py) |
| Day 04 | Student Login Risk Analyzer | Process activity scores, categorize them into risk levels (low, medium, high, critical), apply personalized filtering based on name length, and generate a security report. | [challenge4.py](Day%204/challenge4.py) |
| Day 05 | Emergency Resource Request Analyzer | Categorize emergency resource requests into demand levels, apply personalized filtering using a Personalized Logic Index (PLI) derived from registration number digits, and generate a dispatch report. | [challenge5.py](Day%205/challenge5.py) |
| Day 06 | Smart Transaction Risk Detector | A Python program that analyzes daily transactions to detect suspicious spending patterns. It classifies transactions and determines the overall risk level based on frequency, total amount, and high-value activity. | [challenge6.py](Day%206/challenge6.py) |
| Day 08 | Multi-Dimensional Academic Intelligence System | A Python-based system that analyzes student performance using multiple factors like marks, attendance, and assignment scores. It classifies students, performs statistical analysis, and generates overall academic insights. | [challenge8.py](Day%208/challenge8.py) |
---

# 🧠 Concepts Practiced

Throughout this challenge, the following **Python concepts** are practiced:

* User input handling
* String manipulation
* Conditional statements
* Boolean logic
* List operations
* List comprehension
* Looping techniques
* Data validation
* Personalized program logic
* Structured problem solving

---

# 📂 Repository Structure

```
Python-Code2Xplore-60-Day-Challenge
│
├── Day-01
│   └ challenge1.py
│
├── Day-02
│   └ challenge2.py
│
├── Day-03
│   └ challenge3.py
│
├── Day-04
│   └ challenge4.py
│
├── Day-05
│   └ challenge5.py
|   └ test-cases5.txt
|
├── Day-06
│   └ challenge6.py
|   └ test-cases6.txt
├── Day-08
│   └ challenge8.py
|   └ test_cases8.txt
|
└── README.md
```

Each folder contains the **Python implementation for that specific day's challenge**.

---

# 🎯 Key Learning Outcomes

Through this challenge I am continuously improving:

* Writing structured Python programs
* Designing logical validation systems
* Processing and analyzing input data
* Breaking complex problems into smaller logical steps
* Implementing personalized program logic
* Maintaining a clean and organized GitHub repository

---

# 🧠 Logic Used in Each Challenge

### 🔹 Day 01 – User Profile Validation System

* Collected user inputs: name, email, mobile number, and age
* Validated name:

  * Contains at least one space (minimum two words)
  * Does not start or end with a space
* Validated email:

  * Contains `@` and `.`
  * `@` is not the first character
* Validated mobile number:

  * Exactly 10 digits
  * Contains only numbers using `isdigit()`
  * Does not start with `0`
* Validated age:

  * Must be between 18 and 60
* Final result:

  * If all validations pass → **VALID**
  * Else → **INVALID**

---

### 🔹 Day 02 – University Smart Registration System

* Took inputs: student ID, email, password, referral code
* Validated student ID:

  * Starts with `CSE`
  * 4th character is `-`
  * Last 3 characters are digits
* Validated email:

  * Contains `@` and `.`
  * `@` not at start/end
  * Ends with `.edu`
* Validated password:

  * Minimum 8 characters
  * First character uppercase
  * Contains at least one digit
* Validated referral code:

  * Starts with `REF`
  * Followed by 2 digits
  * Ends with `@`
* Final result:

  * All conditions true → **APPROVED**
  * Else → **REJECTED**

---

### 🔹 Day 03 – Student Result Analyzer

* Took multiple student marks as input
* Categorized marks:

  * 90–100 → Excellent
  * 75–89 → Very Good
  * 60–74 → Good
  * 40–59 → Average
  * 0–39 → Fail
  * Others → Invalid
* Applied personalization:

  * Based on name length
  * If marks fall in `(length × 10)` range → add bonus (+5)
* Generated summary:

  * Total valid students
  * Total failed students

---

### 🔹 Day 04 – Student Login Risk Analyzer

* Stored activity scores in a list
* Ignored negative values (invalid entries)
* Categorized valid scores:

  * 0–30 → Low
  * 31–60 → Medium
  * 61–100 → High
  * > 100 → Critical
* Applied personalization:

  * Even name length → remove low-risk scores
  * Odd name length → remove critical scores
* Final output:

  * Filtered categories
  * Count of valid, ignored, and removed entries

---

### 🔹 Day 05 – Emergency Resource Request Analyzer

* Stored resource requests in a list
* Categorized requests:

  * Low / Moderate / High / Invalid
* Counted valid requests (≥ 0)
* Applied personalization:

  * Extract last 5 digits of registration number
  * Calculate **PLI (Personalized Logic Index)**
  * Remove one category based on PLI
* Final output:

  * Filtered dispatch report
  * Removed count

---

### 🔹 Day 06 – Smart Transaction Risk Detector

* Took number of transactions and stored amounts in a list
* Categorized transactions:

  * Normal / Large / High-risk / Invalid
* Used list comprehension to:

  * Filter valid transactions
  * Calculate total amount and count
* Applied pattern detection:

  * Frequent transactions (>5)
  * High total spending (>5000)
  * ≥3 high-risk transactions
* Final logic:

  * Combined all conditions to determine overall risk level

---

🔹 Day 08 – Multi-Dimensional Academic Intelligence System

* Generated student data using random module:
   * Marks (0–100)
   * Attendance (0–100)
   * Assignment scores (0–50)
* Stored data using:
   * List of tuples → converted into Pandas DataFrame
* Applied classification logic:
   * At Risk → marks < 40 OR attendance < 50
   * Average → marks between 40–70
   * Good → marks between 71–90
   * Top Performer → marks > 90 AND attendance > 80
* Performed statistical analysis using NumPy:
   * Mean (calculated manually)
   * Median
   * Standard deviation
   * Correlation between marks and attendance
* Applied normalization:
   * Converted marks into range 0–1 using formula
* Created custom metric:
   * performance_index = (marks × 0.6 + assignment × 0.4) × log(attendance + 1)
* Applied pattern detection:
   * Consistency → based on standard deviation
   * Attendance risk → number of students with attendance < 50
   * High achievement → number of top performers
* Generated final system insight:
   * Stable Academic System
   * Moderate Performance
   * Critical Attention Required
* Displayed structured output:
   * DataFrame table
   * Category-wise classification
   * Statistical summary
   * Final conclusion



