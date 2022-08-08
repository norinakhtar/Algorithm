from random import random
from cryptography.fernet import Fernet

import socket

socket.gethostbyname("")

key = b"VhKc-8e-tBfw8ROv0t69v7xoJV9ER_Js8zLJERn68oI="

crypt = Fernet(key)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8000))

decryptMsg = ""

while True:
    msg = s.recv(1024)
    if len(msg) <= 0:
        break

    decryptMsg = crypt.decrypt(msg)
print()
print(f"The decrypted message is {str(decryptMsg, 'utf8')}")
print()
