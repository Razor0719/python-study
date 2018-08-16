import functools
import time
from datetime import datetime

def log1(f):
    def wrapper(*args, **kw):
        print('log1 execte1 %s()' % f.__name__)
        return f(*args, **kw)
    return wrapper

def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('log2 %s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('log3 %s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

def now():
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print('--------------------------')
print(now.__name__)
now()

@log1
def now1():
    now()

print(now1.__name__)
now1()

@log2("execute2")
def now2():
    now()

print(now2.__name__)
now2()

@log3("execute3")
def now3():
    now()

print(now3.__name__)
now3()

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        st = time.time()
        f = fn(*args, **kw)
        et = time.time()
        print('%s executed in %s ms' % (fn.__name__, et-st))
        return f
    return wrapper
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')