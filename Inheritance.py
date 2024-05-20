class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def ShowDetails(self):
        print(f"The name of Employee : {self.name} and its id is {self.id}")


class Programmer(Employee):
    def ShowLanguage(self):
        print("The default language is python")


Details = Employee("Harsh", "ML-203")
Details.ShowDetails()
Details = Programmer("Harshita", "ML-207")
Details.ShowLanguage()



