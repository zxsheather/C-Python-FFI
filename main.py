import ctypes
import platform

arch = platform.machine()
if arch == 'x86_64':
    libc = ctypes.cdll.LoadLibrary("./lib/liblib_x86.so")
else :
    libc = ctypes.cdll.LoadLibrary("./lib/liblib.so")

libc.hello()

print (libc.add(1,2))