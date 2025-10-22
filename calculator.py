from tkinter import *
import tkinter.font as font
import math

root = Tk()
root.title("CALCULATOR")
root.geometry("310x400")
root["bg"] = "#d1d1d1"

myfont = font.Font(size=15)

e = Entry(root, width=25, borderwidth=0, bg="#d1d1d1")
e["font"] = myfont
e.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

def angka(nilai):
    sebelum = e.get()
    e.delete(0, END)
    e.insert(0, str(sebelum) + str(nilai))

def tambah():
    global n_awal, mtk
    n_awal = int(e.get())
    mtk = "penjumlahan"
    e.delete(0, END)

def kurang():
    global n_awal, mtk
    n_awal = int(e.get())
    mtk = "pengurangan"
    e.delete(0, END)

def kali():
    global n_awal, mtk
    n_awal = int(e.get())
    mtk = "perkalian"
    e.delete(0, END)

def bagi():
    global n_awal, mtk
    n_awal = int(e.get())
    mtk = "pembagian"
    e.delete(0, END)

def pangkat():
    n_awal = int(e.get())
    e.delete(0, END)
    e.insert(0, n_awal ** 2)

def akar():
    n_awal = int(e.get())
    e.delete(0, END)
    e.insert(0, math.sqrt(n_awal))

def sisabagi():
    global n_awal, mtk
    n_awal = int(e.get())
    mtk = "sisabagi"
    e.delete(0, END)

def hapus():
    e.delete(0, END)

def samadengan():
    nomor_akhir = e.get()
    e.delete(0, END)
    try:
        if mtk == "penjumlahan":
            e.insert(0, n_awal + int(nomor_akhir))
        elif mtk == "pengurangan":
            e.insert(0, n_awal - int(nomor_akhir))
        elif mtk == "perkalian":
            e.insert(0, n_awal * int(nomor_akhir))
        elif mtk == "pembagian":
            e.insert(0, n_awal / int(nomor_akhir))
        elif mtk == "sisabagi":
            e.insert(0, n_awal % int(nomor_akhir))
    except ZeroDivisionError:
        e.insert(0, "Error: Bagi 0!")


btns = {}
for i in range(10):
    btns[i] = Button(root, text=str(i), padx=30, pady=20, bg="#3d3d3d", fg="white", command=lambda i=i: angka(i))


tam = Button(root, text="+", bg="#878787", fg="white", padx=30, pady=20, command=tambah)
kur = Button(root, text="-", bg="#878787", fg="white", padx=30, pady=20, command=kurang)
kal = Button(root, text="x", bg="#878787", fg="white", padx=30, pady=20, command=kali)
bag = Button(root, text="/", bg="#878787", fg="white", padx=30, pady=20, command=bagi)
pang = Button(root, text="x²", bg="#878787", fg="white", padx=30, pady=20, command=pangkat)
ak2 = Button(root, text="√", bg="#878787", fg="white", padx=30, pady=20, command=akar)
sisa = Button(root, text="%", bg="#878787", fg="white", padx=30, pady=20, command=sisabagi)
hap = Button(root, text="C", bg="#878787", fg="white", padx=30, pady=20, command=hapus)
sama = Button(root, text="=", bg="skyblue", padx=50, pady=20, command=samadengan)


btns[7].grid(row=1, column=0, pady=2)
btns[8].grid(row=1, column=1, pady=2)
btns[9].grid(row=1, column=2, pady=2)
btns[4].grid(row=2, column=0, pady=2)
btns[5].grid(row=2, column=1, pady=2)
btns[6].grid(row=2, column=2, pady=2)
btns[1].grid(row=3, column=0, pady=2)
btns[2].grid(row=3, column=1, pady=2)
btns[3].grid(row=3, column=2, pady=2)
btns[0].grid(row=4, column=1, pady=2)

tam.grid(row=1, column=3, pady=2)
kur.grid(row=2, column=3, pady=2)
kal.grid(row=3, column=3, pady=2)
bag.grid(row=4, column=3, pady=2)
hap.grid(row=4, column=0, pady=2)
sama.grid(row=5, column=2, pady=2, columnspan=2)
ak2.grid(row=5, column=0, pady=2)
sisa.grid(row=4, column=2, pady=2)
pang.grid(row=5, column=1, pady=2)

root.mainloop()
