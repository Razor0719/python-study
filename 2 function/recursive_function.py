def fact1(n):
    if n == 1:
        return 1
    return n * fact1(n - 1)


print(fact1(10))


# 尾递归优化
def fact2(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact2(10))


def TowersOfHanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        TowersOfHanoi(n - 1, a, c, b)
        TowersOfHanoi(1, a, b, c)
        TowersOfHanoi(n - 1, b, a, c)


print(TowersOfHanoi(3, 'A', 'B', 'C'))
