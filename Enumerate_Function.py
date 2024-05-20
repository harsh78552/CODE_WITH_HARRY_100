# Enumerate Function gives index value of List ,tuples  or strings.
marks = [100, 98, 87, 45, 67, 89, 70, 67]

# index = 0
# for mark in marks:
#     print(mark)
#     if index == 2:
#         print("Harsh, awesome!")
#     index += 1

for index, mark in enumerate(marks):
# for index in enumerate(marks):
    print(mark)
    print(index)
    if index == 2:
        print("Harsh , awesome!")
