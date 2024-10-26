from universityClass import University
class Department(University):
    def __init__(self):
        super().__init__()
        self.arrDepartments = []

    def setDepartments(self, departments):
        self.arrDepartments = departments

    def getDepartments(self):
        return self.arrDepartments

    def myUniversity(self):
        return self.universityName()


objCourse = Department()
objCourse.setDepartments(["Chemistry", "Physiscs", "Math", "IT", "Computer Science"])
print(objCourse.myUniversity())
print("The list of departments is" ,objCourse.getDepartments())