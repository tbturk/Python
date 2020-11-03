import numpy as np
from PIL import Image


def sifrele(src, mesaj, sonuc):
    resim = Image.open(src, 'r')
    width, height = resim.size
    piksel_dizi = np.array(list(resim.getdata()))
    
    # görüntüde saydamlık değeri varsa
    n = 3
    m = 0

    if resim.mode == 'RGBA':  # görüntüde saydamlık değeri varsa
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
        sifreli_resim = Image.fromarray(piksel_dizi.astype('uint8'), resim.mode)
        sifreli_resim.save(sonuc)
        print("Resim başarıyla şifrelendi")


def desifrele(src):
    resim = Image.open(src, 'r')
    piksel_dizi = np.piksel_dizi(list(resim.getdata()))
    
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
    if "$b7urk" in mesaj:
        print("Gizli mesaj:", mesaj[:-6])
    else:
        print("Gizli mesaj bulunamadı")
