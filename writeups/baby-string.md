# 5. Baby String — Strings di Binary
**Kategori:** Reverse Engineering

**File:** binary ELF 64-bit

## Deskripsi

Diberikan binary ELF 64-bit sederhana yang meminta sebuah flag. Program tidak benar-benar menyembunyikan flag: flag ada di dalam binary sebagai string biasa dan langsung dibandingkan dengan input.

## Analisis & Eksploitasi
- Gunakan strings untuk mengekstrak string yang dapat dibaca:
    ```
    strings -a baby_string | grep -i NFX
    ```
- Atau buka binary di Ghidra / decompiler dan cari string `NFX{...}` di segmen `.rodata`.

## Flag
> NFX{str1ngs_4r3_y0ur_b3st_fr13nd}

