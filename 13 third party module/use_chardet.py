from urllib.request import urlopen
import chardet

res = urlopen('http://yahoo.co.jp/')
print(res.info())
print(chardet.detect(res.read()))

print(chardet.detect(b'Hello, world!'))
data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))
data = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data))
data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))