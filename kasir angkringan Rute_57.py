MENU = {
    "MAKANAN": {
        "Nasi Ayam Goreng": 12000,
        "Nasi Telur Dadar": 8000,
        "Nasi Tempe Goreng": 7000
    },
    "CEMILAN": {
        "Kentang Goreng": 7000,
        "Tahu Tuna": 7000,
        "Cireng": 7000,
        "Siomay Goreng": 7000,
    },
    "TAMBAHAN": {
        "Nasi": 3000,
        "Sambal": 2000
    },
    "MINUMAN_DINGIN_PANAS": {
        "Teh Tarik": 6000,
        "Susu Tape": 6000,
        "Tape": 5000,
        "Kopi Susu": 5000,
        "Susu Putih/Coklat": 5000,
        "Tomat Susu": 6000,
        "Jahe Susu": 6000,
        "Joshua": 6000,
        "Kukubima Susu": 6000,
        "Tomat": 5000,
        "Lemon Tea": 5000,
        "Lyche Tea": 5000,
        "Apple Tea": 5000,
        "Jahe": 5000,
        "Jus Jambu": 6000,
        "Jus Sirsak": 6000,
        "Kopi": 5000,
        "Jeruk": 4000,
        "Teh Manis": 3000,
        "Soda Gembira": 9000,
        "Kopi Jahe": 5000,
        "Susu Jahe": 5000,
        "Teh Jahe": 5000,
        "Jeruk Jahe": 6000,
        "Teh Manis Panas": 3000,
        "Kopi Gelas": 3000,
        "Kopi Cangkir": 4000,
    },
    "MILKSHAKE": {
        "Blackcurrant": 9000,
        "BubleGum": 9000,
        "Mango": 9000,
        "Taro": 9000,
        "Red Velvet": 9000,
        "Strawberry": 9000,
        "Durian": 9000,
        "Vanilla": 9000
    },
    "CHOCOLATE": {
        "Choco Oreo": 9000,
        "Choco Mint": 9000,
        "Choco Caramel": 9000,
        "Choco Tiramishu": 9000,
        "Choco Avocado": 9000
    },
    "COFFEE": {
        "Cappucino": 9000,
        "Mochacino Coffee": 9000,
        "Caramel Machiato": 9000
    },
    "HOT_LATTE": {
        "Hot Chocolate": 8000,
        "Cappucino Hot": 8000,
        "Matcha Greentea Latte": 9000
    }
}

daftar_harga_lengkap = {}
for kategori, item_list in MENU.items():
    for nama_item, harga in item_list.items():
        kunci = nama_item.lower().strip()
        daftar_harga_lengkap[kunci] = harga

keranjang = {}
total_harga = 0


def tampilkan_menu(menu_dict):
    print("\n" + "=" * 45)
    print(f"{'MENU ANGKRINGAN RUTE 57':^45}")
    print("=" * 45)
    for kategori, item_list in menu_dict.items():
        print(f"\n--- {kategori.replace('_', ' ').upper()} ---")
        for i, (item, harga) in enumerate(item_list.items(), 1):
            print(f"{i:2}. {item:<28} Rp {harga:>6,}".replace(",", "."))
    print("=" * 45)


def proses_pemesanan():
    global total_harga

    tampilkan_menu(MENU)
    print("\n--- MULAI PEMESANAN ---")

    while True:
        pesanan = input("Masukkan nama item (atau ketik 'selesai'): ").strip().lower()
        if pesanan == "selesai":
            break

        if pesanan in daftar_harga_lengkap:
            try:
                jumlah = int(input(f"Berapa porsi/gelas {pesanan.title()}? "))
                if jumlah <= 0:
                    print("Jumlah harus lebih dari 0.")
                    continue

                harga_satuan = daftar_harga_lengkap[pesanan]
                subtotal = harga_satuan * jumlah

                if pesanan.title() in keranjang:
                    keranjang[pesanan.title()]["jumlah"] += jumlah
                    keranjang[pesanan.title()]["subtotal"] += subtotal
                else:
                    keranjang[pesanan.title()] = {
                        "harga": harga_satuan,
                        "jumlah": jumlah,
                        "subtotal": subtotal
                    }

                total_harga += subtotal
                print(f"-> {jumlah}x {pesanan.title()} ditambahkan (Subtotal Rp {subtotal:,.0f})".replace(",", "."))

            except ValueError:
                print("Masukkan angka yang valid untuk jumlah.")
        else:
            print("Item tidak ditemukan. Pastikan ejaan sesuai dengan menu!")

    print("\n" + "=" * 45)
    print(f"{'S T R U K   A N G K R I N G A N  RUTE 57':^45}")
    print("=" * 45)

    if not keranjang:
        print("Keranjang kosong. Tidak ada pesanan.")
        return

    print(f"{'Item':<20} {'Qty':>5} {'Harga':>10} {'Subtotal':>10}")
    print("-" * 45)
    for item, data in keranjang.items():
        print(f"{item:<20} {data['jumlah']:>5} Rp {data['harga']:>7,} Rp {data['subtotal']:>7,}".replace(",", "."))
    print("-" * 45)
    print(f"{'TOTAL HARGA:':<35} Rp {total_harga:>7,}".replace(",", "."))

    while True:
        try:
            uang_bayar = int(input("\nMasukkan Uang Tunai Pembeli: Rp "))
            if uang_bayar < total_harga:
                print(f"Uang kurang! Masih kurang Rp {total_harga - uang_bayar:,.0f}".replace(",", "."))
            else:
                kembalian = uang_bayar - total_harga
                print("\n" + "=" * 45)
                print(f"{'TOTAL PEMBAYARAN':<25} : Rp {total_harga:,.0f}".replace(",", "."))
                print(f"{'UANG TUNAI PEMBELI':<25} : Rp {uang_bayar:,.0f}".replace(",", "."))
                print(f"{'KEMBALIAN':<25} : Rp {kembalian:,.0f}".replace(",", "."))
                print("=" * 45)
                print(f"{'TERIMA KASIH TELAH BERKUNJUNG!':^45}")
                print("=" * 45)
                break
        except ValueError:
            print("Masukkan angka yang valid untuk uang tunai.")


if __name__ == "__main__":
    proses_pemesanan()
