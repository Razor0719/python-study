try:
    f = open('file&director.py', 'r')
    print(f.read())
finally:
    if f:
        f.close()
print('------')
with open('file&director.py', 'r', encoding='utf-8') as f:
    print(f.read())
print('------')
f = open('file&director.py', 'r', encoding='utf-8', errors='ignore')
for line in f.readlines():
    print(line.strip())