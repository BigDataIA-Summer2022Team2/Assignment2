import os
import requests

if os.path.exists("key.txt"):
    os.remove("key.txt")
    os.system("openssl rand -hex 32 >> key.txt")
    f = open("key.txt", "r")
    key = f.read()
    print(key)
    f.close()
else:
    os.system("openssl rand -hex 32 >> key.txt")
    f = open("key.txt", "r")
    key = f.read()
    print(key)
    f.close()





