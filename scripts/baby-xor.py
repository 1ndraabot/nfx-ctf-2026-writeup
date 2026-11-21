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