import ctypes
import sys

if sys.platform.startswith('linux'):
    libc = ctypes.cdll.LoadLibrary("./lib/liblib_x86.so")
else :
    libc = ctypes.cdll.LoadLibrary("./lib/liblib.dll")

libc.hello()

print (libc.add(1,2))