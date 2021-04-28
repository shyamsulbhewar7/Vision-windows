@echo off
set ver=%1
set app=%2
if [%ver%]==[] (python C:\Users\POOJA\Desktop\Vision\Vision-windows\Vision\bin\main.py) else (
if "%ver%"=="version" (echo 0.0.3) else (
if "%ver%"=="install" OR "%ver%"=="uninstall" OR "%ver%"=="update" OR "%ver%"=="info" (
python C:\Users\POOJA\Desktop\Vision\Vision-windows\Vision\bin\add-remove.py %ver% %app%
)
	) 
	)
