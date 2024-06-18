import os
from cryptography.fernet import Fernet

class password_decryptor():
    def __init__(self, password, ref):
        self.password = password
        self.refkey = ref
        
    def get_pwrd(self):
        # read encrypted pwd and convert into byte
        encpwdbyt = bytes(self.password, 'utf-8')

        # read key and convert into byte
        refKeybyt = bytes(self.refkey, 'utf-8')

        # use the key and encrypt pwd
        keytouse = Fernet(refKeybyt)
        return (keytouse.decrypt(encpwdbyt).decode())