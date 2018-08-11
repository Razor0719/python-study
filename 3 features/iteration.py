from typing import Iterable

d = {'a': 1, "b": 2, "c": 3}
for key in d:
    print(key, ':', d[key])

for key, value in d.items():
    print(key, ':', value)

s = 'abcd'
for char in s:
    print(char)

for i, value in enumerate([1, 2, 3, 'a', 'b', 'c']):
    print(i, value)
for i,x in enumerate([(1, 'A'), (2, 'B'), ('C', 3), ('D', 4)]):
    print(i, x)
for x,y in [(1, 'A'), (2, 'B'), ('C', 3), ('D', 4)]:
    print(x,y)

def findMinAndMax(L):
    if isinstance(L, Iterable) and len(L) > 0 :
        min = L[0]
        max = L[0]
        for x in L:
            if x<min : min =x
            if x>max : max =x
        return (min,max)
    else:
        return (None,None)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')