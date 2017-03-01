import random
a=random.randint(0, 360)
print(a)
print(a.to_bytes(4, byteorder='big'))
b = a.to_bytes(4, byteorder='big')
print(int.from_bytes(b, byteorder='big'))
