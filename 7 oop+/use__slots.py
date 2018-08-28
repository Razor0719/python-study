from types import MethodType


class Student(object):
    pass


s = Student()
s.name = 'Bob'
print(s.name)


def set_score(self, score):
    self.score = score


# 给实例绑定方法
s.set_score = MethodType(set_score, s)
s.set_score(99)
print(s.score)

# 对另一个实例不起作用
# s2 = Student()
# s2.set_score(99)

# 给类绑定方法
Student.set_score = set_score

s2 = Student()
s2.set_score(10)
print(s2.score)


class Person(object):
    __slots__ = ('name', 'age')


p = Person()
p.name = 'Bob'
p.age = 12


# score未放入slots中，不能被绑定
# p.score = 99

class Teacher(Person):
    pass


# __slots__对继承的子类不起作用
t = Teacher()
t.score = 60
print(t.score)
