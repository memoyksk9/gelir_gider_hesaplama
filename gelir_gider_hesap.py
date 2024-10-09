from tkinter import *
from tkinter import messagebox

gelirler = []
giderler = []

def gelir_ekle():
    miktar = float(gelir_miktar.get())
    gelirler.append(miktar)
    messagebox.showinfo("Başarılı", "Gelir eklendi")

def gider_ekle():
    miktar = float(gider_miktar.get())
    giderler.append(miktar)
    messagebox.showinfo("Başarılı", "Gider eklendi")

def raporla():
    toplam_gelir = sum(gelirler)
    toplam_gider = sum(giderler)
    kalan_bakiye = toplam_gelir - toplam_gider
    messagebox.showinfo("Rapor", f"Toplam Gelir: {toplam_gelir}\nToplam Gider: {toplam_gider}\nKalan Bakiye: {kalan_bakiye}")

root = Tk()
root.title("Gelir gider hesaplama")

Label(root, text="Gelir Miktarı").grid(row=0)
gelir_miktar = Entry(root)
gelir_miktar.grid(row=0, column=1)
Button(root, text='Gelir Ekle', command=gelir_ekle).grid(row=1, column=1, sticky=W, pady=4)

Label(root, text="Gider Miktarı").grid(row=2)
gider_miktar = Entry(root)
gider_miktar.grid(row=2, column=1)
Button(root, text='Gider Ekle', command=gider_ekle).grid(row=3, column=1, sticky=W, pady=4)

Button(root, text='Raporla', command=raporla).grid(row=4, column=1, sticky=W, pady=4)

root.mainloop()
