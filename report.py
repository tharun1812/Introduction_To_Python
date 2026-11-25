# Step 1: Student class

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def best_grade(self):
        return max(self.grades)


# Step 2: Read and parse the file safely

def read_rows(path):
    rows = []

    with open(path, "r") as file:
        lines = file.readlines()[1:]

        for line in lines:
            line = line.strip()

            if line == "":
                continue

            try:
                name, math, physics, english = line.split(",")

                grades = [int(math), int(physics), int(english)]

                rows.append((name, grades))

            except ValueError:
                print(f"Skipped line: {line}")

    return rows


# Step 3: Statistics functions

def class_average(students):
    return sum(student.average() for student in students) / len(students)


def top_student(students):
    return max(students, key=lambda student: student.average())


def subject_average(students, i):
    return sum(student.grades[i] for student in students) / len(students)


# Step 4: Comprehensions

def show_comprehensions(students):
    passed = [s.name for s in students if s.average() >= 12]

    averages = {s.name: round(s.average(), 1) for s in students}

    low_grade = {s.name for s in students if min(s.grades) < 10}

    ranking = sorted(
        students,
        key=lambda s: s.average(),
        reverse=True
    )

    print("Passed:", passed)
    print("Averages:", averages)
    print("Has a grade < 10:", sorted(low_grade))
    print("Ranking:", [s.name for s in ranking])


# Step 5: Write the report

def write_report(students, path):
    with open(path, "w") as file:
        file.write(f"REPORT ({len(students)} students)\n")

        for student in students:
            file.write(
                f"{student.name:<10} "
                f"{student.grades[0]:>2} "
                f"{student.grades[1]:>2} "
                f"{student.grades[2]:>2} "
                f"{student.average():.1f}\n"
            )

        file.write(f"\nClass average: {class_average(students):.2f}\n")

        best = top_student(students)
        file.write(f"Top student: {best.name}\n")


# Main part

rows = read_rows("students.txt")

students = [Student(n, g) for n, g in rows]

for student in students:
    print(f"{student.name} {student.average():.1f} {student.best_grade()}")

print(f"Class average: {class_average(students):.2f}")
print(f"Top: {top_student(students).name}")
print(f"Math average: {subject_average(students, 0):.2f}")

show_comprehensions(students)

write_report(students, "report.txt")

print("Report saved")