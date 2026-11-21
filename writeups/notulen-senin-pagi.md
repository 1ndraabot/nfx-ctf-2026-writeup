# 7. Notulen Senin Pagi — Hidden Text PDF
**Kategori:** Digital Forensics / Steganography

**File:** PDF

## Deskripsi
Sekretaris bilang udah nulis semuanya. Tapi, si Bos bilang gak liat apa-apa.

## Analisis
Pada file PDF, terdapat teks yang diberi warna putih sehingga tidak terlihat secara visual. Teks tetap ada di layer dokumen dan bisa muncul saat melakukan Select All atau copy-paste.

Langkah:
- Buka PDF.
- Tekan Ctrl+A / Select All.
- Copy teks ke editor teks.
- Cari bagian yang tidak terlihat secara visual.
- Flag ditemukan.

Flag:
> NFX{M4kHLuK_T4k_K4s4T_M4T4}