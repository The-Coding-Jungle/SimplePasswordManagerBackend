from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256, SHA512
import base64

bs = AES.block_size

#
# @param key: password in python string type
# @return: SHA-512 hash output in python string type.
# 
def hash(key):
    sha512 = SHA512.new(key.encode())
    return sha512.hexdigest()

#
# @param key: password in python string type.
# @return: SHA-256 in byte string type.
# 
def hashEnc(key):
    sha256 = SHA256.new(key.encode())
    return sha256.digest()

# Mainly used by encrypt function.
def pad(s):
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

# Mainly used by decrypt function.
def unpad(s):
    return s[:-ord(s[len(s)-1:])]

#
# @param key: SHA-256 byte string of primary password.
# @param raw: Data to be encrypted.
# @return: Encrypted data.
# Encryption used: AES-256. 
# 
def encrypt(raw, key):
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode())).decode()

#
# @param key: SHA-256 byte string of primary password.
# @param enc: Encrypted data.
# @return: Decrypted data.
#
def decrypt(enc, key):
    enc = base64.b64decode(enc.encode())
    iv = enc[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    