# def  double(x):
#     return x*2

"""double = lambda x: x * 2

avg=lambda a,b,c:((a+b+c)/3)
print(double(6))
print(cube(5))
print(avg(2,4,6))"""
cube=lambda x:x**3


"""def cube(x):
    return x**3
print(cube(5))"""

def apply(x,value):
    return 2+x(value)

print(apply(lambda x:x*x,6))
