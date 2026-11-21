# 4. Baby Python — Base64 + Reverse String
**Kategori:** Cryptography / Misc

**Teknik:** Base64 decode lalu reverse string

## Deskripsi

Sebuah script Python “mengamankan” flag dengan membalik urutannya lalu meng-encode hasilnya dengan base64. Validator membandingkan input yang dibalik dengan hasil decode base64.

## Source Code
```
#!/usr/bin/env python3
import base64
import sys

_enc = b'fTNmMNHNfdDBuXzNyNyNF9zZDFrX3RwMXJJc19uMGh0eXB7WEZ0'

def main():
    if len(sys.argv) < 2:
        print(f"Pemakaian: {sys.argv[0]} <flag>")
        return 2

    candidate = sys.argv[1].encode()
    if candidate[::-1] == base64.b64decode(_enc):
        print("Correct! Python membaca dari belakang.")
        return 0

    print("Wrong!")
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
```

## Solusi
```
import base64

_enc = b'fTNmMNHNfdDBuXzNyNyNF9zZDFrX3RwMXJJc19uMGh0eXB7WEZ0'
print(base64.b64decode(_enc)[::-1].decode())
```

## Flag
> NFX{pyth0n_scr1pt_k1ds_4r3_n0t_s4f3}