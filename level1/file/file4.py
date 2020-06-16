"""
Read csv file.
"""
import pandas as pd

students = pd.read_csv("./data/students.csv")
print(students)