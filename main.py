from openpyxl import Workbook

wb = Workbook()
kertas = wb.active

kertas["A1"] = "Nama"
kertas["B1"] = "Umur"
kertas["A2"] = "Nama"
kertas["B2"] = "Umur"

no = 1
for x in range(100):
    kertas[f"A{no}"] = "Andi"
    kertas[f"B{no}"] = f"{no} Tahun"
    kertas[f"A{no}"] = "Bagus"
    kertas[f"B{no}"] = f"{no} Tahun"
    no += 1

wb.save("data.xlsx")