from tabulate import tabulate

buku_tersedia = [
    ("Buku Pemrograman Python", 150000),
    ("Buku Data Science", 200000),
    ("Buku Algoritma dan Struktur Data", 180000),
    ("Buku Web Development", 220000),
    ("Buku Machine Learning", 250000),
    ("Buku Pemrograman Java", 160000),
    ("Buku Database Management", 210000),
    ("Buku Jaringan Komputer", 190000),
    ("Buku Keamanan Siber", 230000),
    ("Buku Pengembangan Aplikasi Mobile", 240000),
]

daftar_belanja = []

def tampilkan_buku():
    print("\nDaftar Buku yang Tersedia:")
    for i, (buku, harga) in enumerate(buku_tersedia, start=1):
        print(f"{i}. {buku} - Rp{harga:,}")

def tambah_buku(pilihan, jumlah):
    if 1 <= pilihan <= len(buku_tersedia):
        buku, harga = buku_tersedia[pilihan - 1]
        total_harga = harga * jumlah
        daftar_belanja.append((buku, jumlah, harga, total_harga))
        print(f"\n{jumlah} x {buku} telah ditambahkan ke keranjang dengan total Rp{total_harga:,}.")
    else:
        print("\nPilihan tidak valid.")

def tampilkan_belanja():
    if daftar_belanja:
        print("\nDaftar Belanja Anda:")
        tabel_belanja = []
        total = 0
        for buku, jumlah, harga, total_harga in daftar_belanja:
            tabel_belanja.append([buku, jumlah, f"Rp{harga:,}", f"Rp{total_harga:,}"])
            total += total_harga

        print(tabulate(tabel_belanja, headers=["Buku", "Jumlah", "Harga Satuan", "Total Harga"], tablefmt="grid"))
        print(f"\nTotal Harga: Rp{total:,}")
        return total
    else:
        print("\nKeranjang belanja kosong.")
        return 0

def cetak_struk(total):
    if total > 0:
        print("\n-------- STRUK PEMBELIAN --------")
        print("Toko Buku Pemrograman")
        print("Alamat: Gang Sukarapih No.10, Kota Bandung")
        print("---------------------------------")

        tabel_belanja = []
        for buku, jumlah, harga, total_harga in daftar_belanja:
            tabel_belanja.append([buku, jumlah, f"Rp{harga:,}", f"Rp{total_harga:,}"])
        
        print(tabulate(tabel_belanja, headers=["Buku", "Jumlah", "Harga Satuan", "Total Harga"], tablefmt="grid"))

        print("---------------------------------")
        print(f"Total Harga: Rp{total:,}")
        print("Terima kasih telah berbelanja!")
        print("---------------------------\n")
    else:
        print("Tidak ada barang yang dibeli, struk tidak dapat dicetak.")

def main():
    print("Selamat datang di Toko Buku Pemrograman!")

    while True:
        print("\n--- Menu ---")
        print("1. Lihat Daftar Buku")
        print("2. Tambah Buku ke Keranjang")
        print("3. Lihat Keranjang Belanja")
        print("4. Pembayaran dan Cetak Struk")
        print("0. Keluar")

        try:
            pilihan = int(input("Pilih opsi: "))

            if pilihan == 0:
                print("Terima kasih telah berbelanja di Toko Buku Pemrograman!")
                break

            elif pilihan == 1:
                tampilkan_buku()

            elif pilihan == 2:
                tampilkan_buku()
                try:
                    pilihan_buku = int(input("\nPilih nomor buku yang ingin dibeli: "))
                    jumlah_buku = int(input("Masukkan jumlah buku yang ingin dibeli: "))
                    tambah_buku(pilihan_buku, jumlah_buku)
                except ValueError:
                    print("\nInput tidak valid! Harap masukkan angka.")

            elif pilihan == 3:
                tampilkan_belanja()

            elif pilihan == 4:
                total = tampilkan_belanja()
                if total > 0:
                    try:
                        uang_bayar = int(input(f"\nMasukkan jumlah uang yang dibayarkan: Rp"))
                        if uang_bayar >= total:
                            kembalian = uang_bayar - total
                            print(f"Pembayaran berhasil! Kembalian Anda: Rp{kembalian:,}")
                            cetak_struk(total)
                        else:
                            print("Uang yang dibayar kurang!")
                    except ValueError:
                        print("Input tidak valid! Harap masukkan angka.")
                else:
                    print("Keranjang masih kosong.")
            else:
                print("Opsi tidak valid!")

        except ValueError:
            print("\nInput tidak valid! Harap masukkan angka.")

if __name__ == "__main__":
    main()
