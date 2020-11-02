import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox

URL = 'http://bilgisayar.kocaeli.edu.tr/duyurular.php'
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

for i in satirlar_baslik:
    i = i.replace('>', '')
    i = i.replace('</h2', '')
    i = i.replace('é', ' ')
    basliklar.append(str(i))
for i in satirlar_tarih:
    i = i.replace('o\">', '')
    i = i.replace('é', ' ')
    i = i.split("<")
    tarihler.append(str(i[0]))
    sahipler.append(str(i[2].replace('span>', '')))

for dlitem in entryler:
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
            if (ek.startswith("http")):
                ek = ek
            else:
                ek = "bilgisayar.kocaeli.edu.tr/" + ek

        # print(ek)
        ekler.append(ek)
    else:
        ekler.append("")

pencere = Tk()
pencere.title("KOÜ Bilgisayar Mühendisliği Duyurular")


def duyuru_mbox(duyuru_baslik, duyuru_govde):
    messagebox.showinfo(duyuru_baslik, duyuru_govde)


for i in range(len(basliklar)):
    a = Button(pencere, text=basliklar[i] + "  " + tarihler[i],
               command=lambda c=i: duyuru_mbox(basliklar[c], aciklamalar[c]))
    a.pack()

pencere.mainloop()
