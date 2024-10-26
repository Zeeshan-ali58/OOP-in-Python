# studentClass.py
from humanClass import Human

class Teacher(Human):
    def __init__(self):
        super().__init__()  # Corrected: removed `self` as an argument
        self.arrTeachers = []

    def setTeachers(self, teachers):
        self.arrTeachers = teachers

    def getTeachers(self):
        return self.arrTeachers

    def myUniversity(self):
        self.getUniversityName()  # Call the correct method from the parent class

# Create an instance of Student
objStudent = Teacher()
objStudent.setTeachers(["Shafiq", "Dr. Imtiaz", "Prof. Shahid", "Asst Prof Maqbool"])

# Print the instance to see the __str__ output if needed
print("List of teachers:", objStudent.getTeachers())
