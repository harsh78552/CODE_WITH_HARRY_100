def func1():
    try:
        l = [1, 2, 3, 4, 5]
        i = int(input("enter your index: "))
        print(l[i])
        return 1
    except:
        print("some error occurred.")
        return 0
    finally:
        print("I am always executed")


x = func1()
print("At the indexing value this number present:", x)
