class University:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"
objUnivesity = University("Zeeshan", 45)
print(objUnivesity)