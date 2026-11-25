grades = {
    "Ana": [14, 16, 12],
    "Ben": [9, 11, 8],
    "Chloé": [18, 17, 19],
}

best_name = ""
best_average = 0

for name, student_grades in grades.items():
    average = sum(student_grades) / len(student_grades)

    print(f"{name} {average:.1f}")

    if average > best_average:
        best_average = average
        best_name = name

print(f"Best: {best_name}")