import requests
from bs4 import BeautifulSoup
from tkinter import *

URL = 'http://bilgisayar.kocaeli.edu.tr/duyurular.php'  # KOÜ deki herhangi bir bölüm yada fakültenin duyuru
# sayfasının linki yapıştırılabilir.
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.findAll("div", {"class": "col-md-6"})
entryler = soup.findAll("dl")

results = str(results)
results = results.replace(' ', 'é')

satirlar_baslik = re.findall('>\S+</h2>', results)
satirlar_tarih = re.findall('o\">\S+</span>', results)

basliklar = []
tarihler = []
sahipler = []
aciklamalar = []
ekler = []

for i in satirlar_baslik:  # bölüm sayfasındaki tüm duyuruların başlıklarını çeker
    i = i.replace('>', '')
    i = i.replace('</h2', '')
    i = i.replace('é', ' ')
    basliklar.append(str(i))
for i in satirlar_tarih:  # bölüm sayfasındaki tüm duyuruların giriş tarihlerini çeker
    i = i.replace('o\">', '')
    i = i.replace('é', ' ')
    i = i.split("<")
    tarihler.append(str(i[0]))
    sahipler.append(str(i[2].replace('span>', '')))

for dlitem in entryler:  # bölüm sayfasındaki tüm duyuruları popuplarını çeker ve gerekli listelerde tutar
    dds = dlitem.find_all('dd')
    aciklama = str(dds[1])
    aciklama = aciklama.replace('<dd>', '')
    aciklama = aciklama.replace('</dd>', '')
    aciklamalar.append(aciklama)
    if len(dds) == 3:
        ek = re.findall('href=\"\S+\"', str(dds[2]))
        if len(ek) == 0:
            ek = str(dds[2])
            ek = ek.replace('<dd>', '')
            ek = ek.replace('</dd>', '')
        else:
            ek = str(ek[0])
            ek = ek.replace('href=\"', '')
            ek = ek[:-1]
            if ek.startswith("http"):
                ek = ek
            else:
                ek = "bilgisayar.kocaeli.edu.tr/" + ek
        ekler.append(ek)
    elif len(dds) == 4:
        ek = re.findall('href=\"\S+\"', str(dds[3]))
        ek1 = re.findall('href=\"\S+\"', str(dds[2]))
        if len(ek) == 0:
            ek = str(dds[3])
            ek = ek.replace('<dd>', '')
            ek = ek.replace('</dd>', '')
            ek1 = str(dds[2])
            ek1 = ek1.replace('<dd>', '')
            ek1 = ek1.replace('</dd>', '')
        else:
            ek = str(ek[0])
            ek = ek.replace('href=\"', '')
            ek = ek[:-1]
            ek1 = str(ek1[0])
            ek1 = ek1.replace('href=\"', '')
            ek1 = ek1[:-1]
            if ek.startswith("http"):
                ek = ek
            else:
                ek = "bilgisayar.kocaeli.edu.tr/" + ek
            if ek1.startswith("http"):
                ek1 = ek1
            else:
                ek1 = "bilgisayar.kocaeli.edu.tr/" + ek1
        ekler.append(ek + "\n" + ek1)
    else:
        ekler.append("")
# bu kısımdan sonrası elde edilen verileri grafiksel olarak listelemeye yarar.
pencere = Tk()
pencere.title("KOÜ Bilgisayar Mühendisliği Duyurular")


def link_ekle(ekran, ek_tmp, uzunluk):
    frame1 = Frame(ekran)
    link = Entry(ekran, width=uzunluk)
    if "\n" in ek_tmp:  # eğer duyuruda birden fazla ek bulunuyorsa bu işlem yapılır ve çoklu entry içeren bir frame
        # döndürülür
        ekler_tmp = ek_tmp.split("\n")
        link = Entry(frame1, width=uzunluk)
        link.insert(0, ekler_tmp[0])
        link.grid(row=1, column=1)
        link1 = Entry(frame1, width=uzunluk)
        link1.insert(0, ekler_tmp[1])
        link1.grid(row=2, column=1)
        return frame1
    else:
        link.insert(0, ek_tmp)
    return link


def duyuru_mbox(duyuru_sahip, duyuru_govde, duyuru_ek):  # duyuruya tıklayınca çıkan popup
    top = Toplevel(pencere)
    width = 500
    height = int(len(duyuru_govde) * 0.8 / 1.7)
    if duyuru_ek != "":
        height += 80
    top.geometry(str(width) + "x" + str(height))
    top.title(duyuru_sahip)
    msg = Message(top, text=duyuru_govde, width=400, justify='left')
    msg.pack()
    if duyuru_ek != "":
        button = Button(top, text="Ekler", command=link_ekle(top, duyuru_ek, width).pack)
        button.pack()


for i in range(len(basliklar)):
    a = Button(pencere, text=basliklar[i] + "  " + tarihler[i],
               command=lambda c=i: duyuru_mbox(sahipler[c], aciklamalar[c], ekler[c]))
    a.pack()

pencere.mainloop()
