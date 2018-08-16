f=lambda x:x*x
print(f,f(5))

def test(x,y):
    return lambda :x*x+y*y
print(test,test(1,2))


def is_odd(n):
    return n % 2 == 1

L1 = list(filter(is_odd, range(1, 20)))
print(L1)
L2 = list(filter(lambda x:x%2==1, range(1,20)))
print(L2)