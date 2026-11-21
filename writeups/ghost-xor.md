# 3. Ghost XOR — Known XOR Key
**Kategori:** Cryptography

**Teknik:** XOR berulang dengan kunci 4 karakter

## Deskripsi

Pesan rahasia dienkripsi menggunakan operasi XOR berulang dengan kunci rahasia sepanjang 4 karakter. Source code challenge meninggalkan KEY = b"LOCK" dan ciphertext_hex.

## Source Code
```
def xor(data: bytes, key: bytes) -> bytes:
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

KEY = b"LOCK"
ciphertext_hex = "02091b08180938337c3d1c7a3f10303e3c7c31147f7b3032133d72"
ciphertext = bytes.fromhex(ciphertext_hex)
flag = xor(ciphertext, KEY)
print(flag.decode())
```

## Solusi
```
def xor(data: bytes, key: bytes) -> bytes:
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

KEY = b"LOCK"
ciphertext = bytes.fromhex(
    "02091b08180938337c3d1c7a3f10303e3c7c31147f7b3032133d72"
)

print(xor(ciphertext, KEY).decode(errors="ignore"))
```

## Flag
> NFXCTF{x0r_1s_sup3r_34sy_r1ght_a8f9c2}