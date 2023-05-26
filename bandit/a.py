import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def aes_cbc_pkcs7_decrypt(key: bytes, encrypted: bytes, iv: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted)
    return unpad(decrypted, AES.block_size)

# G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPKguXmS6pmX2wGeLKRriiD6QcCYxLrNxe2TV1ZOUQXdfmTQ3MhoJTaSrfy9N5bRv4o%3D
# 원본 문자열에서 URL 인코딩된 부분을 디코딩한 결과입니다.
encrypted_str = "G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKguXmS6pmX2wGeLKRriiD6QcCYxLrNxe2TV1ZOUQXdfmTQ3MhoJTaSrfy9N5bRv4o="

encrypted_data = base64.urlsafe_b64decode(encrypted_str)
key = b"0123456789abcdef"  # 암호화에 사용된 키를 입력하세요
iv = b"fedcba9876543210"  # 암호화에 사용된 IV를 입력하세요

decrypted_data = aes_cbc_pkcs7_decrypt(key, encrypted_data, iv)
decrypted_str = decrypted_data.decode("utf-8")

print("Decrypted string: ", decrypted_str)
