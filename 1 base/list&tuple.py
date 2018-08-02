classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[-1])
classmates.append('Google')
print(classmates)
classmates.insert(1, 'Martin')
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)
print('----------')

s = ['Apple', 123, True]
s.append(['Watermelon', 2.5, False])
print(s)
print(len(s))
print('----------')

classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
classmates = ('Michael')
print(classmates)
classmates = ('Michael',)
print(classmates)
print('----------')

t = ('a', 'b', ['A', 'B'])
print(t)
t[2].append('C')
print(t)
print('----------')

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])