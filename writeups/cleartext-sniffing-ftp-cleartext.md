# Cleartext Sniffing — FTP Cleartext

**Kategori:** Network Forensics
**File:** traffic.pcap

## Deskripsi

Pukul 18.05 WIB, sistem monitoring SOC membunyikan alarm anomali dari segmen jaringan laboratorium lama. Sebuah workstation mencurigakan terdeteksi aktif menghubungi beberapa server internal lama. Analis sempat menyalakan port mirroring dan merekam lalu lintas paket ke traffic.pcap.

## Analisis

File PCAP memuat lalu lintas TCP, HTTP, dan FTP. Request FTP tidak dimasking, sehingga kredensial dan token terlihat dalam bentuk ASCII.

Langkah analisis:
- Buka traffic.pcap di Wireshark.
- Filter FTP `ftp` atau `ftp.request.command == "PASS"`
- Perhatikan baris `FTP Request: PASS ....`
- Flag terlihat cleartext pada request tersebut.

## Flag
> NFXCTF{cl34rt3xt_pr0t0c0ls_l34k_s3cr3ts}