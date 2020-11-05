import pyautogui as pag

print(str(pag.size()))


pag.moveTo(750, 45, 0)
pag.click()
pag.typewrite("eybis")
pag.press('enter')
pag.moveTo(100, 200, 0.5)
buton_yeri = pag.locateOnScreen('tcdd.png')
buton_yerix, buton_yeriy = pag.center(buton_yeri)
pag.click(buton_yerix, buton_yeriy)
pag.moveTo(100, 200, 0.6)
buton_yeri = pag.locateOnScreen('nereden.png')
buton_yerix, buton_yeriy = pag.center(buton_yeri)
pag.click(buton_yerix, buton_yeriy+20)
pag.hotkey('ctrl', 'a')
pag.typewrite("izmit")
pag.moveTo(100, 200, 0.2)
pag.click(buton_yerix, buton_yeriy+60)

buton_yeri = pag.locateOnScreen('nereye.png')
buton_yerix, buton_yeriy = pag.center(buton_yeri)
pag.click(buton_yerix, buton_yeriy+20)
pag.hotkey('ctrl', 'a')
pag.typewrite("eski")
pag.moveTo(100, 200, 0.2)
pag.click(buton_yerix, buton_yeriy+60)



buton_yeri = pag.locateOnScreen('tarih.png')
buton_yerix, buton_yeriy = pag.center(buton_yeri)
pag.click(buton_yerix, buton_yeriy+20)
pag.hotkey('ctrl', 'a')
pag.typewrite("07.11.2020")

buton_yeri = pag.locateOnScreen('kapat.png')
buton_yerix, buton_yeriy = pag.center(buton_yeri)
pag.click(buton_yerix, buton_yeriy)
pag.moveTo(100, 200, 0.2)
buton_yeri = pag.locateOnScreen('ara.png')
buton_yerix, buton_yeriy = pag.center(buton_yeri)
pag.click(buton_yerix, buton_yeriy)
