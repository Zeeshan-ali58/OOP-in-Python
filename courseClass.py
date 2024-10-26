from universityClass import University
class Course(University):
    def __init__(self):
        super().__init__()
        self.arrCourses = []

    def setCourses(self, courses):
        self.arrCourses = courses

    def getCourses(self):
        return self.arrCourses

    def myUniversity(self):
        return self.universityName()


objCourse = Course()
objCourse.setCourses(["Chemistry", "Physiscs", "Math"])
print(objCourse.myUniversity())
print("The list of courses being teached in this university are" ,objCourse.getCourses())