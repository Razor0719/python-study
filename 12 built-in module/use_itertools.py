import itertools

for n in itertools.count(1):
    print(n)
    if n > 5: break

t = 0
for c in itertools.cycle('AB'):
    print(c)
    t += 1
    if t > 5: break

for s in itertools.repeat('X', 2):
    print(s)

ns = itertools.takewhile(lambda n: n < 10, itertools.count(3))
print(list(ns))

for c in itertools.chain('AB', 'CD'):
    print(c)

for c, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.lower()):
    print(c, list(group))


def pi(n):
    step1 = itertools.count(1, 2)
    step2 = itertools.takewhile(lambda x: x < 2 * n, step1)
    step3 = map(lambda x: (pow(-1, (x-1)/2)) * 4 / x, step2)
    return sum(step3)

print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')