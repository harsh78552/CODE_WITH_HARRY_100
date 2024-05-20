# class Math:
#     def __init__(self, num):
#         self.num = num
#
#     def addtonum(self, num1):
#         self.num = self.num + num1
#
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#
# #
# # result = Math.add(1, 3)
# # print(result)
# a1 = Math(5)
# print(a1.num)
# a1.addtonum(6)
# print(a1.num)

class Math:
    def __init__(self, num):
        self.num = num

    def add_to_num(self, num1):
        self.num = self.num + num1

    @staticmethod
    def add(num2, num3):
        return num2 + num3


a1 = Math(7)
a1.add_to_num(5)
print(a1.num)
Math.add(4, 5)
