from functools import reduce

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
print(list(map(abs, [1, -2, 3, 4, -5, -6, 7, 8, -9])))


def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def ji(x, y):
    return x * y


def prod(numbers):
    return reduce(ji, numbers)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def str2float(s):
    s = s.split('.')
    if len(s) == 1:
        return reduce(lambda x, y: x * 10 + y, map(int, s[0]))
    else:
        return reduce(lambda x, y: x * 10 + y, map(int, s[0] + s[1])) / pow(10, len(s[1]))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


def odd(x):
    return x % 2 == 1;


print(list(filter(odd, [1, 2, 3, 4, 5, 6])))


def empty(s):
    return not (s and s.strip())


print(list(filter(empty, ['A', '', '', None, 'C'])))


def is_palindrome(n):
    return str(n)[::-1] == str(n)


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted([36, 5, -12, 9, -21], key=abs, reverse=True))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score, reverse=True)
print(L2)