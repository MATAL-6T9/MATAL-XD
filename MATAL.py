import os, sys
os.system("git pull")
try:
    __import__("MATAL").menu()
except Exception as e:
    exit(str(e))
