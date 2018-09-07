import hmac

message = b'pythonHmac'
key = b'secret'
h1 = hmac.new(key, message, digestmod='md5')
print(h1.hexdigest())
h2 = hmac.new(key, message, digestmod='sha1')
print(h2.hexdigest())
h3 = hmac.new(key, message)
print(h3.hexdigest())