def my_abs1(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs1(-10))


def nop():
    pass


def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs2(111))

import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)


def quadratic(a, b, c):
    s = b * b - 4 * a * c
    if s >= 0:
        x1 = (-b + math.sqrt(s)) / (2 * a)
        x2 = (-b - math.sqrt(s)) / (2 * a)
        return x1, x2
    else:
        return None


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
