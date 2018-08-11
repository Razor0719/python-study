from collections import Iterable, Iterator

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))
print('------')
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance(100, Iterable))
print('------')
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))
print('------')
s=iter('abcde')
while True:
    try:
        x=next(s)
        print(x)
    except StopIteration:
        print('end')
        break
