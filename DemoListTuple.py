# DemoListTuple.py 

lst = ["red", "blue", "green"]

print(len(lst))
print(lst)
lst.append("white")
lst.insert(1, "pink")
print(lst)
print(lst.count("red"))
print(lst.index("blue"))
lst.sort()
print(lst)
lst.reverse()
print(lst)

print("---tuple---")
#함수정의
def times(a,b):
    return a+b, a*b 

#호출
result = times(3,4)
print(result)

print("id: %s, name: %s" % ("kim", "김유신"))

args = (5, 6)
print(times(*args))

print("---형식변환---")
a = set((1,2,3))
print(type(a))
print(a)
b = list(a)
print(b)
b.append(4)
print(b)

print("---set형식---")
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(a.union(b))


