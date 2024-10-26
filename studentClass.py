# studentClass.py
from humanClass import Human

class Student(Human):
    def __init__(self):
        super().__init__()  # Corrected: removed `self` as an argument
        self.arrStudents = []

    def setStudents(self, students):
        self.arrStudents = students

    def getStudents(self):
        return self.arrStudents

    def myUniversity(self):
        self.getUniversityName()  # Call the correct method from the parent class

# Create an instance of Student
objStudent = Student()
objStudent.setStudents(["zeeshan", "ali", "abdullah", "shan"])

# Print the instance to see the __str__ output if needed
print("List of students:", objStudent.getStudents())
