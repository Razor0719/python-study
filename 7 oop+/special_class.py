class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student (name: %s)' % self.name

    __repr__ = __str__

    def __getattr__(self, item):
        if item == 'score':
            return 100
        if item == 'age':
            return lambda: 20  # 返回函数
        raise AttributeError('no attribute %s' % item)

    def __call__(self, *args, **kwargs):
        print("my name is: %s" % self.name)


print(Student('Bob'))
s = Student('Martin')
print(s.name)
print(s.score)
print(s.age())
s()
print(callable(Student))
print('----------------')


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 20:
            raise StopIteration
        return self.a

    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        elif isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


for x in Fib():
    print(x)
print('----------------')
f = Fib()
print(f[2])
print(f[4])
print(f[0:5])
print('----------------')


# 链式调用
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, param=''):
        return Chain('%s/%s' % (self._path, param))

    def __str__(self):
        return self._path

    __repr__ = __str__

root_path = '/api/v1'
print(Chain(root_path).match)
print(Chain(root_path).user(12).age)
print(Chain(root_path))

