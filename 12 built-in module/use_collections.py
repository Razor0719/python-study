from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

Point = namedtuple('Point', ['x', 'y'])
Circle = namedtuple('Circle', ['x', 'y', 'r'])
p = Point(1, 2)
print(p.x, p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))

q = deque([1, 2, 3])
q.append('x')
q.appendleft('y')
print(q)

d = defaultdict(lambda :'N/A')
d['x'] = 'abc'
print(d['x'])
print(d['y'])

d = dict([('a',1),('b',2),('d',4),('c',3)])
print(d)
od = OrderedDict([('a',1),('b',2),('d',4),('c',3)])
print(od)

c = Counter()
for ch in 'pythonPyhton':
    c[ch] += 1
print(c)

