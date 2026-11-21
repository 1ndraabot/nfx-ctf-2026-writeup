def xor(data: bytes, key: bytes) -> bytes:
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

KEY = b"LOCK"
ciphertext_hex = "02091b08180938337c3d1c7a3f10303e3c7c31147f7b3032133d72"
ciphertext = bytes.fromhex(ciphertext_hex)
flag = xor(ciphertext, KEY)
print(flag.decode())