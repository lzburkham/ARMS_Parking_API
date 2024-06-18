from cryptography.fernet import Fernet
import os

### 1. Enter Password as string
PASSWORD=<INSERT PASSWORD HERE>

### 2. generate key and write it in a file
key = Fernet.generate_key()
with open("refKey.txt", "wb") as f:
    f.write(key)
    
### 3. encrypt the password and write it in a file
refKey = Fernet(key)
mypwdbyt = bytes(PASSWORD, 'utf-8') # convert into byte
encryptedPWD = refKey.encrypt(mypwdbyt)
with open("encryptedPWD.txt", "wb") as f:
    f.write(encryptedPWD)