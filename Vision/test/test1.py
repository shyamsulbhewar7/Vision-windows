import os
import sys
pth=os.popen("dir C:\\{ap}.* /b/s".format(ap='comtypes-1.1.7')).read()
print(pth)
pth=pth[:-1]
os.startfile("{pth}".format(pth=pth))