@echo off
set ver=%1
IF "%ver%"=="version" GOTO vers
python C:\Users\PRASAD\Desktop\Vision\vision.py
:vers
echo 0.0.1