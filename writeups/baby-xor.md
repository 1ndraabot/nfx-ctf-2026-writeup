# 6. Baby XOR — Single-byte XOR Brute-force
**Kategori:** Reverse Engineering / Cryptography

**File:** `baby_xor`

## Deskripsi

Validator tidak menyimpan flag sebagai plaintext. Setiap byte flag di-XOR dengan satu byte kunci sebelum disimpan ke array. Karena kunci hanya 8 bit, seluruh ruang kunci dapat dicoba dalam waktu singkat.

## Analisis
Gunakan strings dan decompiler seperti Ghidra untuk melihat:
- program menerima argumen input flag melalui command-line,
- terdapat string Wrong!, Correct!, dan usage,
- input pengguna di-XOR dengan single-byte key lalu dibandingkan dengan array ciphertext statis di .rodata.
Karena hanya ada 256 kemungkinan kunci, brute-force single-byte XOR dapat dilakukan secara instan.

## Script Brute Force
```
def solve_xor_binary(filename):
    try:
        with open(filename, "rb") as f:
            content = f.read()

        print(f"Berhasil membaca file {filename}, ukuran: {len(content)} bytes.\n")

        found = False
        for key in range(256):
            decoded_bytes = bytes([b ^ key for b in content])

            if b"NFX{" in decoded_bytes:
                print(f"[+] Kunci ditemukan! (Hex): 0x{key:02x}")
                idx = decoded_bytes.find(b"NFX{")
                flag_candidate = decoded_bytes[idx:idx + 40].split(b"\x00")[0]
                print(
                    f"[+] Kandidat Flag: "
                    f"{flag_candidate.decode('utf-8', errors='ignore')}"
                )
                found = True

        if not found:
            print(
                "[-] Pola 'NFX{' tidak ditemukan dengan kunci 1-byte standar. "
                "Mari periksa struktur biner di Ghidra."
            )

    except FileNotFoundError:
        print(
            f"[-] File {filename} tidak ditemukan. "
            "Pastikan biner ada di direktori yang sama."
        )

solve_xor_binary("baby_xor")
```

## Flag
> NFX{x0r_1s_fun_but_n0t_s3cur3}