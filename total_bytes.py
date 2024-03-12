import sys

def total_bytes(obj): 
  return sys.getsizeof(obj)

print(total_bytes("hello"))