import types

print(type(123))
print(type('strssss'))
print(type(None))
print(type(abs))


def f():
    pass


print(type(f) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)

print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

print(dir('123'))


class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print('hasattr(obj, \'x\') =', hasattr(obj, 'x'))
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))
print('getattr(obj, \'y\') =', getattr(obj, 'y'))
print('obj.y =', obj.y)

print('getattr(obj, \'z\') =', getattr(obj, 'z', 404))

f = getattr(obj, 'power')
print(f)
print(f())
