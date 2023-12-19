import os, sys
os.system("git pull")
try:
    __import__("FUI").FUI()
except Exception as e:
    exit(str(e))
