

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50


student1 = Student("Jan Kowalski", [60, 75, 80, 90, 85, 86, 73, 66])
student2 = Student("Anna Nowak", [23, 30, 20, 45, 13, 53, 43, 67])

result1 = student1.is_passed()
result2 = student2.is_passed()

print(student1.name, "zdal/a", result1)
print(student2.name, "zdal/a", result2)
