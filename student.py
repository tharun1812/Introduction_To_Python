class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
 
    def add_grade(self, g):
        self.grades.append(g)
 
    def compute_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
 
ana = Student("Ana")
for g in [14, 16, 12]:
    ana.add_grade(g)
ben = Student("Ben")
print(ana.name, ana.compute_average())
print(ben.name, ben.compute_average())