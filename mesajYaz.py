import pyautogui

import time
import random
import os
import datetime
import psutil
import keyboard


# Open the text file
def mesaj_yaz(event):
    pyautogui.hotkey('winleft', 'r') #çalıştır penceresini açar
    pyautogui.typewrite('notepad') #çalıştır penceresine notepad yazar
    pyautogui.hotkey('enter') # enter
    time.sleep(1) # notepad in açılması için 1 saniye bekler

    with open("mesajlar.txt", "r") as f:
        satirlar = f.readlines()
        satir_sayisi = len(satirlar)
        rastgele_satir_numarasi = random.randint(0, satir_sayisi - 1)


    mesaj = str(satirlar[rastgele_satir_numarasi])
    print(satirlar[rastgele_satir_numarasi])
    typing_speed = len(mesaj) / 2 # yazma hızını belirler
    for char in mesaj:
        pyautogui.typewrite(char)
        time.sleep(1/typing_speed)

    time.sleep(1)
    dosyaadi="mesaj"
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")#dosyayı kaydederken aynı isimde dosya olmasın diye tarih saat bilgisini dosya adına yazdık
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),'OneDrive','Belgeler')#belgeler klasörünün yolunu belirler
    file_path = os.path.join(desktop.encode('utf-8').decode(), dosyaadi.encode('utf-8').decode() + "_" + current_time )#yazmak için dosya yolu oluşturur


    pyautogui.hotkey('ctrl','s') # dosyayı kaydet
    time.sleep(1) # kaydetme ekranı gelmesi için 1 saniye bekle
    pyautogui.typewrite(file_path) # dosya yolunu yaz
    pyautogui.hotkey('enter')



    for proc in psutil.process_iter():#
        if proc.name() == "Notepad.exe":
            proc.terminate()


