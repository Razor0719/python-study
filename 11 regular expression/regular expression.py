import re


def match(r, s):
    if re.match(r, s):
        print('right')
    else:
        print('wrong')


r = r'^\d{3}\-\d{3,8}$'
match(r, '010-12345')
match(r, '011 1111')

print('a b   c'.split(' '))
print(re.split(r'\s+', 'a  b   c'))
print(re.split(r'[\s\,\.\;]+', 'a,b.c d  e, .  f;,g ; .h'))

def group(r, s):
    if isinstance(r, str):
        print(re.match(r, s).groups())
    else:
        print(r.match(s).groups())

group(r'^(\d{3})-(\d{3,8})$', '010-12345')

# 贪婪匹配
group(r'^(\d+)(0*)$', '102300')
group(r'^(\d+?)(0*)$', '102300')

# 预编译
re1 = re.compile('^(\d{3})-(\d{3,8})$')
group(re1, '010-1231231')
group(re1, '010-1111')
