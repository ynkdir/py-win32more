
from ctypes import create_unicode_buffer
from Windows.Win32.UI.Shell import wnsprintfW

buf = create_unicode_buffer(1024)
r = wnsprintfW(buf, len(buf), "hello %s %d %p", "world", 42, 0x1234)
print(r, buf.value)

