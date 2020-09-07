monday_temperatures = [9.1,8.8,7.5]
students_grades = {"Marry": 9.1, "Sim": 8.8, "Jim": 7.5}

mysum = sum(students_grades.values())
length = len(students_grades)
mean = mysum/length

print(mean)
print(students_grades.values())
print(students_grades.keys())