import functools

int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('110101'))
int8 = functools.partial(int, base=8)
print(int8('66672'))
print(int8('23557'))

max10 = functools.partial(max, 10)
print(max10(1,4,9))
print(max10(1,2,3,4,11,12))