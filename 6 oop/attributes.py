class Student(object):
    count = 0 # 类属性

    def __init__(self, name):
        self.name = name
        Student.count +=1

if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

s = Student('Bob')
s.score = 90 # 实例属性
print(s.score)