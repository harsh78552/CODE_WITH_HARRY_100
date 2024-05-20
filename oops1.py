class Person:  # <----- CLASS
    name = "Harry"
    occupation = "ML-Engineer"
    networth = 100

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()  # <------ OBJECT
a.name = "Harsh"
a.occupation = "AI-Engineer"
# print(a.name)
b = Person()
b.name = "Harshita"
b.occupation = "Govt. Teacher"
a.info()  # <------- METHOD
b.info()

# Self----> wo object jiske liye method call kiya ja raha hai
