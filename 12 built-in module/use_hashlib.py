import hashlib

md51 = hashlib.md5()
md51.update('use md5'.encode('utf-8'))
print(md51.hexdigest())
md52 = hashlib.md5()
md52.update('use '.encode('utf-8'))
md52.update('md5'.encode('utf-8'))
print(md52.hexdigest())

sha1 = hashlib.sha1()
sha1.update('use'.encode('utf-8'))
sha1.update(' sha1'.encode('utf-8'))
print(sha1.hexdigest())