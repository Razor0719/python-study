print('ABC'.encode('ascii'))
print('ABC'.encode('utf-8'))
print('中文'.encode('utf-8'))
# bytes:b'xxxxx'
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(len('ABC'))
print(len('中文'))
print('----------')

# %d %f %s %x
print('Hello, %s' % 'world')
print('Hello, %s, $%d, please' % ('world', 100))
print('%2d-%02d' % (3, 1))
print('%.2f%%' % 3.1415926)
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
print('----------')

s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('%.1f%%' % r)
