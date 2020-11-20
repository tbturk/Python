import requests
from bs4 import BeautifulSoup
import urllib.request

URL = 'https://www.migros.com.tr/aydinlatma-elektrik-malzemeleri-c-520'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

ulList = soup.findAll("li")
uliststr = str(ulList)
ulist = uliststr.split("data-page=\"")
sayfaSayisi=None
if len(ulist)==2:
    sayfaSayisi=1
else:
    sayfaSayisi = int(ulist[len(ulist) - 2][0])
print(sayfaSayisi)
#sayfaSayisi=10
urun = 0
for i in range(sayfaSayisi):
    URL1 = URL+"?sayfa="+str(i+1)
    print(URL1)
    page = requests.get(URL1)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.findAll("img", {"class": "product-card-image lozad"})
    for link in results:
        indirilecek = str(link.get("data-src"))
        urllib.request.urlretrieve(indirilecek, "Elektronik/ELECTRONICS/" + str(urun) + ".jpg")
        urun += 1
