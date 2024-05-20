List = ["1", "2", "2", "1", "3", "3", "4", "5", "6"]
seen = set()
Pter = []
Pter1 = []

k = 2
for Iter in range(len(List)):
    result = List[Iter]
    if List.count(result) == k:
        Pter.append(result)
# print(Pter)
for num in Pter:
    if num not in seen:
        Pter1.append(num)
        seen.add(num)
# print(Pter1)
i = 1
while i <= len(List):
    print(i)
    # print(List.index("1"))
    i = i + 1
