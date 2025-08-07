# Task 1: Student Grade Analyzer

import numpy as np

grades = np.array([
    [85, 90, 78],   # Student 1
    [88, 92, 80],   # Student 2
    [75, 70, 65],   # Student 3
    [95, 98, 100],  # Student 4
    [60, 72, 68]    # Student 5
])

# 1: Calculate average grade of each student

avg_grades= np.mean(grades, axis=1)
print("Average grades of each student:", avg_grades)


# 2: Find the highest grade in each subject

highest_grades = np.max(grades, axis=0)
print("Highest grades in each subject:", highest_grades)

# 3: Count how many students scored above 85 in Math (column 0)

math_scores = grades[:, 0]
above_marks= np.sum(math_scores > 85)
print("Number of students scoring above 85 in Maths are :", above_marks)

