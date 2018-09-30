from wsgiref.simple_server import make_server
from wsgi_app import application

httpd = make_server('', 1996, application)
print('Serving HTTP on port 1996...')
# 开始监听HTTP请求:
httpd.serve_forever()