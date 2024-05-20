class Employee:
    def __init__(self):
        self.__name = "harsh"  # ----->Private
        # self._name = "Harsh" ------>Public


a = Employee()
print(a._Employee__name)
print(a.__dir__())
