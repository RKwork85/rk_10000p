import platform
import sys
import warnings
import os

print(sys.version_info[1])
if platform.system() != "Windows":
    print('linux')
LOGDIR = os.getenv("LOGDIR", ".")
print(LOGDIR)