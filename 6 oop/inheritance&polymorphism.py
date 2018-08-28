class Animal(object):
    def run(self):
        print('running')

    def eat(self):
        print('eating')

    def run_twice(self):
        self.run()
        self.run()


class Dog(Animal):
    def run(self):
        print('dog runing')


class Cat(Animal):
    def run(self):
        print('cat running')


a = Animal()
d = Dog()
c = Cat()

a.run()
d.run()
d.run_twice()
c.run()
c.run_twice()


# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
def run_twice(animal):
    animal.run()
    animal.run()


class Car(object):
    def run(self):
        print('car running')

    def stop(self):
        print('car stop')

run_twice(Car())