# NFX CTF — WriteUp Apa Adanya

Kumpulan writeup tantangan CTF dari dokumen **“nfx-WriteUp Apa Adanya-1.pdf”**.  
Repo ini berisi ringkasan analisis, teknik eksploitasi, dan script reproduksi untuk masing-masing tantangan.

> **Disclaimer:** Writeup ini dibuat untuk dokumentasi pembelajaran CTF. Beberapa flag, payload, dan data sensitif ditulis sebagai bukti penyelesaian. Jika repo dipublikasikan, sesuaikan redaksi data sensitif atau jadikan repo private.

## Daftar Isi

- [Ringkasan Tantangan](#ringkasan-tantangan)
- [1. Nexa Supply — XXE](/writeups/nexa-supply.md)
- [2. Cleartext Sniffing — FTP Cleartext](/writeups/cleartext-sniffing-ftp-cleartext.md)
- [3. Ghost XOR — Known XOR Key](/writeups/ghost-xor.md)
- [4. Baby Python — Base64 + Reverse String](/writeups/baby-python.md)
- [5. Baby String — Strings di Binary](/writeups/baby-string.md)
- [6. Baby XOR — Single-byte XOR Brute-force](/writeups/baby-xor.md)
- [7. Notulen Senin Pagi — Hidden Text PDF](/writeups/notulen-senin-pagi.md)

---

## Ringkasan Tantangan

| No | Tantangan | Kategori | Teknik | Flag |
|---:|---|---|---|---|
| 1 | Nexa Supply | Web Security | XXE / XML External Entity Injection | `NFX{xxe_supply_f33d_lb0d_4f13_9d4c}`* |
| 2 | Cleartext Sniffing | Network Forensics | FTP cleartext sniffing | `NFXCTF{cl34rt3xt_pr0t0c0ls_l34k_s3cr3ts}` |
| 3 | Ghost XOR | Cryptography | XOR with repeated 4-byte key | `NFXCTF{x0r_1s_sup3r_34sy_r1ght_a8f9c2}` |
| 4 | Baby Python | Cryptography / Misc | Base64 decode + reverse string | `NFX{pyth0n_scr1pt_k1ds_4r3_n0t_s4f3}` |
| 5 | Baby String | Reverse Engineering | `strings` pada binary ELF | `NFX{str1ngs_4r3_y0ur_b3st_fr13nd}` |
| 6 | Baby XOR | Reverse Engineering | Single-byte XOR brute-force | Lihat script / pola `NFX{x0r_1s_fun_but_n0t_s3cur3}` |
| 7 | Notulen Senin Pagi | Digital Forensics | Hidden white text pada PDF | `NFX{M4kHLuK_T4k_K4s4T_M4T4}` |

---
