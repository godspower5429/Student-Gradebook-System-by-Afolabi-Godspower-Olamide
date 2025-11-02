# CSC 825
# NAME: AFOLABI GODSPOWER OLAMIDE

from abc import ABC, abstractmethod

# Abstraction
class Student(ABC):
    def __init__(self, name):
        self._name = name  # Encapsulation: protected attribute
        self._grades = {}  # subject: grade

    def add_grade(self, subject, grade):
        self._grades[subject] = grade
        print(f"{self._name} - {subject}: Grade recorded as {grade}")

    def average(self):
        if not self._grades:
            return 0
        return sum(self._grades.values()) / len(self._grades)

    @abstractmethod
    def has_passed(self):
        pass

    def show_report(self):
        print(f"\nReport for {self._name}:")
        for subject, grade in self._grades.items():
            print(f"{subject}: {grade}")
        print(f"Average: {self.average():.2f}")
        print("Status: " + ("PASS" if self.has_passed() else "FAIL"))

# Inheritance and Polymorphism: Undergraduate and Postgraduate have different pass marks
class Undergraduate(Student):
    def has_passed(self):
        return self.average() >= 50

class Postgraduate(Student):
    def has_passed(self):
        return self.average() >= 60

# Gradebook system
class Gradebook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student added: {student._name} ({student.__class__.__name__})")

    def show_all_reports(self):
        for student in self.students:
            student.show_report()

# Example usage
if __name__ == "__main__":
    gradebook = Gradebook()

    # Students
    chinedu = Undergraduate("Chinedu")
    adesuwa = Postgraduate("Adesuwa")
    gradebook.add_student(chinedu)
    gradebook.add_student(adesuwa)

    # Record grades
    chinedu.add_grade("Mathematics", 72)
    chinedu.add_grade("English", 65)
    adesuwa.add_grade("Mathematics", 62)
    adesuwa.add_grade("English", 58)

    # Show reports
    gradebook.show_all_reports()
