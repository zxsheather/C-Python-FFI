import ctypes

libc = ctypes.cdll.LoadLibrary("./liblib.so")

libc.hello()

print (libc.add(1,2))