
from hashlib import sha256

x = "123"
y = "123"

xhex = sha256(x.encode('utf-8')).hexdigest()
yhex = sha256(y.encode('utf-8')).hexdigest()

print(xhex)
print(yhex)