# pip install numpy
import numpy as np

name = np.array(["Ram", "Raj", "Ramya", "Gopal", "Thangadurai"])
gender = np.array(["Male", "Male", "Female", "Male", "Male"])
age = np.array([24, 25, 25, 24, 23])
exam = np.array([46, 47, 42, 40, 30])
employee = np.array((name, gender, age, exam))
print(employee)

print(np.min(exam))
print(np.max(exam))

min_val = np.min(exam)
max_val = np.max(exam)
scaled_arr = (exam - min_val) / (max_val - min_val)
print(scaled_arr)


print("Mean", np.mean(exam))
print("Median", np.median(exam))
print("Standard Deviation", np.std(exam))
