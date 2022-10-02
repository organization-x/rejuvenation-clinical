
from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#------------------------------------------------------------------------------#
def generateKey():
    """
    Purpose: Generating a random encryption key and saving it to a text file
    Parameters: None
    Returns: None
    """

    key = Fernet.generate_key() # generates a random key that can be used.

    print("Unsalted key:", key)

    # It will not run it again. If it runs again, then a new key will generate, and
    # I don't want to deal with that to I just made it a comment.

    password_given = "bestpassword12"
    password = password_given.encode()

    salt = b'\xd1\x08\x1fq\xf0\x04\x03\xd4\x10\xae&G\xebL\x17\x06'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
        )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    with open('.env', 'wb') as file:
        file.write(key) # saves the key to a file to be used to both encrypt and decrypt

    print("Salted key:", key)

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    generateKey()
    with open('.env', 'rb') as f:
        key = f.read()

    with open('test.txt', 'rb') as f:
        data = f.read()

    print("Unencrypted data:", data)

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    print("Encrypted data:", encrypted_data)

    with open('test.txt', 'wb') as f:
        f.write(encrypted_data)

    byte_decrypted = fernet.decrypt(encrypted_data)
    string_decrypted = byte_decrypted.decode()
    print("Byte string:", byte_decrypted)
    print("String:", string_decrypted)
