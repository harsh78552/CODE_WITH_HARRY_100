class Person:
    """  def __init__(self):
          print("Heyy buddy")  default constructor"""

    """def __init__(self, n, o):
        self.name = n
        self.age = o---> Parametrised Character"""

    def info(self):
        print(f"{self.name} age is {self.age}")


# a = Person()
a = Person("Harsh", 25)
b = Person("Harshita", 20)
# print(a.name, a.age)
a.info()
b.info()
