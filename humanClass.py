from universityClass import University
class Human(University):
    def __init__(self):
        super().__init__()  # This is used to initilize the parent class

        print("Derived class initialized")

    def getUniversityName(self):
        print(self.universityName())

deriverClass = Human()
print(deriverClass.getUniversityName())