import os
import sys
def search_any_file(filename):
	pths=''
	pth=os.popen("wmic logicaldisk get caption").read()
	disks = pth.split("\n\n")
	for y in range(1,len(disks)):
		disks[y]=disks[y].strip()
		pths+=os.popen("dir "+disks[y]+"\\"+filename+".* /b/s").read()
	paths = pths.split("\n")
	return paths
y=search_any_file('"sss aaa"')
for z in range(len(y[:-1])):
	print(z," = ",y[z])
inpt=int(input("Enter number of path to open file\n"))
os.startfile('"{pth}"'.format(pth=y[inpt]))