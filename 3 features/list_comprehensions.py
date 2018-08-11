import os

print(list(range(1, 5)))
print([x * x for x in range(1, 5)])
print([x * x for x in range(1, 10) if x % 2 == 1])
print(list(a + b for a in 'abc' for b in 'xyz'))

print([folder for folder in os.listdir()])

d = {'a': '1', 'b': '2', 'c': '3', 'd': '4'}
print([key + ':' + value for key, value in d.items()])

L = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L if isinstance(x, str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
