def power(x, n=2):
    result = 1
    while n > 0:
        n -= 1
        result *= x
    return result


print(power(2))
print(power(5, 3))
print(power(10, 2))


def calc1(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc1([1, 2, 3]))


def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc2(1, 2, 3))
numbers = [1, 2, 3]
print(calc2(*numbers))


def person(name, age, **other):
    print('name:', name, 'age:', age, 'other:', other)


person('Pycharm', 1, city='hz')
other = {'city': 'hz', 'job': 'worker'}
person('Pycharm', 5, **other)


def person(name, age, *, city, job):
    print(name, age, city, job)


person('Pycharm', 24, city='hz', job='worker')


def person(name, age, *args, city, job):
    print(name, age, args, city, job)


args = [5, 5, 5, 5]
person('Pycharm', 24, args, city='hz', job='worker')
person('Pycharm', 24, *args, city='hz', job='worker')


# 顺序： 必选参数、默认参数、可变参数、命名关键字参数和关键字参数

def product(x, *numbers):
    sum = x
    for n in numbers:
        sum *= n
    print(sum)
    return sum


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
