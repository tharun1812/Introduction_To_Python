names = ["Ana", "Ben", "Chloé", "Dan"]
grades = [18.5, 9.5, 17.0, 11.5]

total = 0
count = 0

for name, grade in zip(names, grades):
    count += 1
    total += grade

    if grade >= 10:
        result = "PASS"
    else:
        result = "FAIL"

    print(f"{count}. {name}: {grade} {result}")

average = total / count

print(f"Average: {average:.2f}")