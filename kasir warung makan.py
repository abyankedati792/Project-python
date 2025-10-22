print("========================== Warung Makan Prasmanan ==========================")
pembeli = input("Masukkan Nama Pembeli: ")
print('Nama Pembeli:', pembeli)

def pilih_makanan():
    global total_makanan, porsi, nama_makanan
    print("\n============= MENU MAKANAN =============")
    print("1. Nasi Goreng     : Rp 15.000")
    print("2. Mie Ayam        : Rp 12.000")
    print("3. Sate Ayam       : Rp 20.000")
    print("4. Soto Ayam       : Rp 18.000")
    print("5. Bakso           : Rp 14.000")
    print("6. Nasi Uduk       : Rp 16.000")
    print("7. Nasi Campur     : Rp 22.000")
    print("8. Nasi Pecel      : Rp 6.000")
    print("9. Nasi Padang     : Rp 25.000")
    print("10. Ayam Goreng    : Rp 19.000")
    print("11. Ikan Bakar     : Rp 30.000")
    print("12. Gulai Kambing  : Rp 35.000")
    print("13. Rendang        : Rp 40.000")
    print("14. Sop Buntut     : Rp 45.000")
    print("15. Ayam Bakar     : Rp 28.000")
    print("16. Tahu Tempe     : Rp 8.000")
    print("17. Pecel Lele     : Rp 12.000")
    print("18. Gado-Gado      : Rp 10.000")
    print("19. Lontong Sayur  : Rp 9.000")
    print("20. Capcay         : Rp 15.000")
    print("21. Nasi Kuning    : Rp 14.000")

    nomor = int(input("Pilih Menu Makanan (1-21): "))
    porsi = int(input("Masukkan Jumlah Porsi: "))

    daftar_harga = {
        1: ("Nasi Goreng", 15000),
        2: ("Mie Ayam", 12000),
        3: ("Sate Ayam", 20000),
        4: ("Soto Ayam", 18000),
        5: ("Bakso", 14000),
        6: ("Nasi Uduk", 16000),
        7: ("Nasi Campur", 22000),
        8: ("Nasi Pecel", 6000),
        9: ("Nasi Padang", 25000),
        10: ("Ayam Goreng", 19000),
        11: ("Ikan Bakar", 30000),
        12: ("Gulai Kambing", 35000),
        13: ("Rendang", 40000),
        14: ("Sop Buntut", 45000),
        15: ("Ayam Bakar", 28000),
        16: ("Tahu Tempe", 8000),
        17: ("Pecel Lele", 12000),
        18: ("Gado-Gado", 10000),
        19: ("Lontong Sayur", 9000),
        20: ("Capcay", 15000),
        21: ("Nasi Kuning", 14000)
    }

    if nomor in daftar_harga:
        nama_makanan, harga = daftar_harga[nomor]
        total_makanan = harga * porsi
        print(f"{nama_makanan} x {porsi} = Rp {total_makanan}")
    else:
        print("Pilihan tidak ada di daftar menu. Silakan pilih kembali!")
        pilih_makanan()

def pilih_minuman():
    global total_minuman, gelas, nama_minuman
    print("\n============= MENU MINUMAN =============")
    print("1. Es Teh         : Rp 3.000")
    print("2. Es Jeruk       : Rp 3.000")
    print("3. Es Campur      : Rp 10.000")
    print("4. Jus Alpukat    : Rp 12.000")
    print("5. Jus Mangga     : Rp 15.000")
    print("6. Air Mineral    : Rp 5.000")
    print("7. Kopi           : Rp 2.000")
    print("8. Teh Panas      : Rp 3.000")
    print("9. Wedang Jahe    : Rp 5.000")
    print("10. Wedang Tomat  : Rp 5.000")

    nomor = int(input("Pilih Menu Minuman (1-10): "))
    gelas = int(input("Masukkan Jumlah Gelas: "))

    daftar_minuman = {
        1: ("Es Teh", 3000),
        2: ("Es Jeruk", 3000),
        3: ("Es Campur", 10000),
        4: ("Jus Alpukat", 12000),
        5: ("Jus Mangga", 15000),
        6: ("Air Mineral", 5000),
        7: ("Kopi", 2000),
        8: ("Teh Panas", 3000),
        9: ("Wedang Jahe", 5000),
        10: ("Wedang Tomat", 5000)
    }

    if nomor in daftar_minuman:
        nama_minuman, harga = daftar_minuman[nomor]
        total_minuman = harga * gelas
        print(f"{nama_minuman} x {gelas} = Rp {total_minuman}")
    else:
        print("Pilihan tidak ada di daftar menu. Silakan pilih kembali!")
        pilih_minuman()

pilih_makanan()
pilih_minuman()

total_semua = total_makanan + total_minuman
print("\nTotal yang harus dibayar: Rp", total_semua)

uang = int(input("Uang Tunai Pembeli: Rp "))
kembalian = uang - total_semua

print("\n==================== STRUK BELI ====================")
print("Nama\t\t: ", pembeli)
print(f"Beli\t\t: {porsi} {nama_makanan} (Rp {total_makanan})")
print(f"\t\t  {gelas} {nama_minuman} (Rp {total_minuman})")
print("Tagihan\t\t: Rp", total_semua)
print("Dibayar\t\t: Rp", uang)
print("Kembalian\t: Rp", kembalian)
print("====================================================")
