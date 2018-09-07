from contextlib import closing, contextmanager
from urllib.request import urlopen


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query %s' % self.name)


@contextmanager
def create_query(name):
    print('start')
    q = Query(name)
    yield q
    print('end')


with create_query('hello') as q:
    q.query()


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("hello")
    print("world")

# 代码的执行顺序是：
#
# with语句首先执行yield之前的语句，因此打印出<h1>；
# yield调用会执行with语句内部的所有语句，因此打印出hello和world；
# 最后执行yield之后的语句，打印出</h1>。

with closing(urlopen('http://www.baidu.com')) as page:
    for l in page:
        print(l)
