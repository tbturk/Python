import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

import numpy as np
from PIL import ImageTk, Image


def sifrele():
    mesaj = text_mesaj.get()
    print(mesaj)
    filename = askopenfilename()  # secilen resmin dosya yolunu döndürür
    dosya = str(filename).split("/")
    global tip
    tip = "." + dosya[len(dosya) - 1].split(".")[1]
    resim = Image.open(str(filename), 'r')
    width, height = resim.size
    piksel_dizi = np.array(list(resim.getdata()))

    if resim.mode == 'RGB':  # görüntüde saydamlık değeri varsa
        n = 3
        m = 0
    elif resim.mode == 'RGBA':  # görüntüde saydamlık değeri varsa
        n = 4
        m = 1

    toplam_piksel = piksel_dizi.size // n

    mesaj += "$b7urk"
    b_mesaj = ''.join([format(ord(i), "08b") for i in mesaj])
    mesaj_piksel = len(b_mesaj)

    if mesaj_piksel > toplam_piksel:
        print("HATA: Daha büyük boyutlu bir resim yükleyin yada mesajı kısaltın")
    else:
        index = 0
        for p in range(toplam_piksel):
            for q in range(m, n):
                if index < mesaj_piksel:
                    piksel_dizi[p][q] = int(bin(piksel_dizi[p][q])[2:9] + b_mesaj[index], 2)
                    index += 1

        piksel_dizi = piksel_dizi.reshape(height, width, n)
        global sifreli_resim
        sifreli_resim = Image.fromarray(piksel_dizi.astype('uint8'), resim.mode)
        print("Resim başarıyla şifrelendi")


def desifrele():
    filename = askopenfilename()  # secilen resmin dosya yolunu döndürür
    resim = Image.open(str(filename), 'r')
    piksel_dizi = np.array(list(resim.getdata()))

    # görüntüde saydamlık değeri varsa
    n = 3
    m = 0

    if resim.mode == 'RGBA':  # görüntüde saydamlık değeri varsa
        n = 4
        m = 1

    toplam_pixel = piksel_dizi.size // n

    gizli_bitler = ""
    for p in range(toplam_pixel):
        for q in range(m, n):
            gizli_bitler += (bin(piksel_dizi[p][q])[2:][-1])

    gizli_bitler = [gizli_bitler[i:i + 8] for i in range(0, len(gizli_bitler), 8)]

    mesaj = ""
    for i in range(len(gizli_bitler)):
        if mesaj[-5:] == "$b7urk":
            break
        else:
            mesaj += chr(int(gizli_bitler[i], 2))
    print(mesaj)
    if "$b7urk" in mesaj:
        print("Gizli mesaj:", mesaj[:-6])
    else:
        print("Gizli mesaj bulunamadı")


def savefile():
    filename = filedialog.asksaveasfile(mode='w', defaultextension=tip)
    print(tip)
    if not filename:
        return
    sifreli_resim.save(filename)


def resimcek():
    filename = askopenfilename()  # secilen resmin dosya yolunu döndürür
    dosya = str(filename).split("/")
    global tip
    tip = "." + dosya[len(dosya) - 1].split(".")[1]
    print(tip)
    resim = Image.open(str(filename))
    resim.thumbnail((200, 200), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(resim)
    resim = tk.Label(pencere, image=render)
    resim.image = render
    resim.place(x=100, y=40)


pencere = tk.Tk()
pencere.title("LSB Görüntü Şifreleme")
pencere.geometry("900x600")

text_mesaj = tk.Entry(pencere, width=70)
text_mesaj.place(x=0, y=280)

sifre_button_resim_sec = tk.Button(pencere, text="Şifrelenecek resmi seç", command=sifrele)
sifre_button_resim_sec.place(x=140, y=250)

sifre_button_kaydet = tk.Button(pencere, text="Şifrelenmiş mesajı kaydet", command=savefile)
sifre_button_kaydet.place(x=135, y=550)

desifre_button_resim_sec = tk.Button(pencere, text="Şifrelenmiş resmi seç", command=desifrele)
desifre_button_resim_sec.place(x=640, y=250)

desifre_button_kaydet = tk.Button(pencere, text="Mesajı Göster", command=savefile)
desifre_button_kaydet.place(x=657, y=550)

pencere.mainloop()
