menu ={
    "Fried Chicken" : 15000,
    "Burger Queen" : 25000,
    "Pizza Hut" : 30000,
    "Nasi Goreng" : 20000,
    "Mie Ayam" : 12000,
    "Es Teh Manis" : 5000,
    "Jus Alpukat" : 10000,
    "Air Mineral" : 3000,
    "Jasmine Tea" : 5000,
    "Ice Coca-Cola" : 12000,
    "Ice Lemon Tea" : 10000,
    "Ice Milo" : 15000,
    "Ice Coffee" : 15000,
    "Ice Chocolate" : 15000,
    "Chocolate Cake" : 25000,
    "Cheesecake" : 30000,
    "Fruit Salad" : 15000,
    "Tiramisu" : 35000,
    "Banana Split" : 25000,
    "Apple Pie" : 20000,
    "Brownies" : 15000,
}
print("======================== Daftar Menu ========================")
for i in menu:
    print("Daftar Menu : ", i, "\t Harga : ",menu[i])
print("Pembelian diatas 100.000 mendapatkan diskon 15%")
print("================================================")
beli = input("Pilih Menu : ")
jumlah = int(input("Jumlah Pesanan : "))
bayar = jumlah * menu[beli]

if bayar > 100000:
    diskon = bayar*15/100
    total = bayar - diskon
else:
    total = bayar

print("======================== Detail Pembayaran ========================")
print("Menu yang dipesan          : ", beli)
print("Jumlah Pesanan             : ", jumlah)
print("Total Bayar                : ", bayar)
print("Total yang harus dibayar   : ", total)