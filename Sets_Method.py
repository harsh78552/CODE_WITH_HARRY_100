# S1 = {1, 2, 3, 4, 5}
# S2 = {6, 7, 8, 9, 10,}
# print(S1.union(S2))
# print(S1.intersection(S2))
# S2.update(S1)
# print(S2)
city1 = {"Delhi", "Goa", "Mumbai", "Bihar", "Kolkata"}
City5 = set()
for item in city1:
    City5.add(item)
print(City5)

# city2 = {"Bangalore", "Jodhpur", "Mumbai", "Goa", "Assam"}
city3 = {"Bengal", "Kerala", "Sikkim", "Manipur", "Mizoram"}
city4 = {"Delhi", "Mumbai", "Goa"}
# print(city2.intersection_update(city1))
# print(city1.symmetric_difference(city2))
# print(city1.isdisjoint(city3))
# print(city1.issuperset(city4))
# print(city4.issubset(city1))
# print(city4.remove("Goa"))
# print(city4.discard("Goi"))
"""print(city4.pop())
item = city4.pop()
print(item)
print(city4)"""

"""del city1
print(city1) -----> it generates error"""

if "Goa" in City5:
    print("Goa is present")
else:
    print("Goa is not present")
