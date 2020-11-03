from math import cos, asin, sqrt, pi
import tkinter as tk


def distance(lat1, lon1, lat2, lon2):
    carpan = pi / 180
    a = 0.5 - cos((lat2 - lat1) * carpan) / 2 + cos(lat1 * carpan) * cos(lat2 * carpan) * (
            1 - cos((lon2 - lon1) * carpan)) / 2
    return 12742 * asin(sqrt(a))


def cevir_fonk():
    try:
        km = distance(float(text_lat1.get()), float(text_lng1.get()), float(text_lat2.get()), float(text_lng2.get()))
        km = "{:.2f}".format(km)
        text_kilometre.configure(text=str(km) + '  Km')
    except:
        text_kilometre.configure(text="Gerekli Alanları Doldur")


pencere = tk.Tk()
pencere.title("LatLong Çevirici")
pencere.geometry("325x250")

label_loc1 = tk.Label(pencere, text="Lokasyon 1:")
label_loc2 = tk.Label(pencere, text="Lokasyon 2:")
label_lat1 = tk.Label(pencere, text="Latitude:")
label_lng1 = tk.Label(pencere, text="Longitude:")
label_lat2 = tk.Label(pencere, text="Latitude:")
label_lng2 = tk.Label(pencere, text="Longitude:")

label_kilometre = tk.Label(pencere, text="Kilometre:")
text_kilometre = tk.Label(pencere, text=" ")
cevir_btn = tk.Button(pencere, text="Çevir", command=cevir_fonk)

text_lat1 = tk.Entry(pencere, width=12)
text_lng1 = tk.Entry(pencere, width=12)
text_lat2 = tk.Entry(pencere, width=12)
text_lng2 = tk.Entry(pencere, width=12)

label_loc1.place(x=50, y=10)
label_lat1.place(x=50, y=50)
label_lng1.place(x=50, y=90)
text_lat1.place(x=50, y=70)
text_lng1.place(x=50, y=110)

label_loc2.place(x=200, y=10)
label_lat2.place(x=200, y=50)
label_lng2.place(x=200, y=90)
text_lat2.place(x=200, y=70)
text_lng2.place(x=200, y=110)

label_kilometre.place(x=50, y=160)
text_kilometre.place(x=110, y=160)

cevir_btn.place(x=140, y=200)

pencere.mainloop()
