import os
print(os.name) # 系统类型
# print(os.uname()) #Windows不支持
print(os.environ)
print(os.environ.get('PATH'))
print(os.path.abspath('.'))
print(os.path.join('.', 'testdir'))
os.mkdir('./testdir')
os.rmdir('./testdir')
print(os.path.split('/Users/michael/testdir/file.txt'))
print(os.path.splitext('/path/to/file.txt'))

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
# shutil模块是os的补充
