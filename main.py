import tkinter as tk
import pyautogui
import random
from mesajYaz import mesaj_yaz
import time
import pygame


def resim_goster():
    global window, resimlistesi, label
    def move_window():
        current_x, current_y = window.winfo_x(), window.winfo_y()
        window.geometry("+{}+{}".format(current_x + 20, current_y))
        if current_x >= 400:
            window.geometry("+{}+{}".format(current_x, current_y))
        window.after(100, move_window)

    window = tk.Tk()
    window.title('ŞUNA BİR BAK')
    resimlistesi = ['Meme1.png', 'Meme2.png', 'Meme3.png',
                    'Meme4.png', 'Meme5.png', 'Meme6.png', 'Meme7.png']
    random_resim = random.randint(0, 6)
    image = tk.PhotoImage(file=resimlistesi[random_resim])
    width = image.width()
    height = image.height()
    window.geometry(f"{width}x{height}")
    label = tk.Label(window, image=image)
    label.pack()
    window.update()
    window.after(100, move_window)
    window.after(3000, change_image)
    window.mainloop()
    
    
def change_image():
    global resimlistesi

    random_resim = random.randint(0, 6)
    new_image = tk.PhotoImage(file=resimlistesi[random_resim])
    new_window = tk.Toplevel(window)
    new_label = tk.Label(new_window, image=new_image)
    new_label.pack()
    new_label.image = new_image  # Keep new image from being garbage collected
    new_window.update_idletasks()
    new_window.deiconify()
    new_window.after(3000,change_image)


resim_goster()


for i in range(True):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('effect.mp3')
    pygame.mixer.music.play(-1)

TRANS_COLOR = '#abcdef'

resimlistesi = ['Meme1.png', 'Meme2.png', 'Meme3.png', 'Meme4.png', 'Meme5.png', 'Meme6.png', 'Meme7.png']
root = tk.Tk()
root.overrideredirect(1) #kullanıcının pencereyle etkileşime girmemesini sağlar. pencere boyutunu ayarlayamaz, kapatamaz
root.attributes('-transparentcolor', TRANS_COLOR)
root.geometry("+1920+1080")

#ördek hareket ederken kullanılan resimler
image1 = tk.PhotoImage(file='ordek1.png')
image2 = tk.PhotoImage(file='ordek2.png')
image3 = tk.PhotoImage(file='ordek3.png')
image4 = tk.PhotoImage(file='ordek4.png')
resim_listesi=["ordek1.png","ordek2.png","ordek3.png","ordek4.png"]

label = tk.Label(root, image=image2, bg=TRANS_COLOR)
label.pack()

sayac=0
def fare_takip():
    global sayac
    global sayac1
    mouse_x, mouse_y = pyautogui.position() #mouse un x ve y koordinatlarını tutar
    x, y = root.winfo_x(), root.winfo_y() #pencerenin koordinatlarını tutar
    if x == mouse_x: #mouse ile pencerenin x koordinatları eşitse ördek mouse imlecini ekranın sol üst noktasına götürür
        root.geometry("+{}+{}".format(x - (x // 20), y - (y // 20)))
        pyautogui.moveTo(mouse_x - (mouse_x // 20), mouse_y - (mouse_y // 20), duration=0.01)
    else:
        root.geometry("+{}+{}".format(x + (mouse_x - x) // 20, y + (mouse_y - y) // 20)) # ördeğin mouse imlecine doğru gitmesini sağlar
    sayac += 1

    if sayac == 200:#200 kere hareket ettiğinde rasgele hareket için move_window fonksiyonuna gider
        sayac1 = 0
        sayac=0
        root.after(0, rasgele_hareket)
    else:
        root.after(100, fare_takip)

counter = 0
random_x=1000
random_y=0
sayac1=0
def rasgele_hareket():
    global sayac1
    global sayac
    x, y = root.winfo_x(), root.winfo_y()
    root.geometry("+{}+{}".format(x + (random_x - x) // 20, y + (random_y - y) // 20))
    sayac1 += 1

    if sayac1 == 200: #200 kere hareket ettiğinde
        sayac = 0

        root.after(0, fare_takip)
    else:
        root.after(100, rasgele_hareket)


def rasgele_koordinat():#rasgele_hareket fonksiyonu için 5 saniyede bir random koordinat üretir
    global random_x
    global random_y
    random_x = random.randint(0, root.winfo_screenwidth() - root.winfo_width())
    random_y = random.randint(0, root.winfo_screenheight() - root.winfo_height())
    root.after(5000, rasgele_koordinat)


def resim_degistir():#ördek resminin gittiği yere doğru bakmasını sağlar
    global counter
    mouse_x, _ = pyautogui.position()
    global resim_listesi
    global sayac,sayac1
    # Mouse'un x koordinatını al
    x, y = root.winfo_x(), root.winfo_y()
    if sayac>=1 and sayac<=200:#sayac 1 ile 200 arasındaysa yani fare_takip fonksiyonu çalışıyorsa

    # Ekranın yarısından sola mı yoksa sağa mı hareket ediyor güvercin
        if mouse_x <= x:#ördeğin x konumu mouse un x konumundan küçükse sol tarafa bakan ördekleri değilse sağ tarafa bakanları kullanıyoruz
            resim_listesi = [image1, image2]
        else:
            resim_listesi = [image3, image4]
    else:
        if random_x < x:#sayac 1-200 arası değilse rasgele_hareket çalışıyordur. aynı kontrolü random koordinat için kontrol ediyoruz
            resim_listesi = [image1, image2]
        else:
            resim_listesi = [image3, image4]

    # label'ın resmini değiştirme
    label.config(image=resim_listesi[counter])
    counter += 1
    #resimler arası geçiş yaparak ayak hareketi sağlar
    if counter >= len(resim_listesi):
        counter = 0
    root.after(200, resim_degistir)

def toggle_visibility():#pencerenin belli aralıklarla kaybolup geri gelmesini sağlar
    if root.state() == "normal":
        root.withdraw()
        root.after(30000, toggle_visibility)

    else:
        root.deiconify()
        root.after(30000, toggle_visibility)



#root.after(30000,resim_goster)
#root.after(3000, change_image)
root.attributes("-topmost", True)#ördeğin diğer programların üstünde durmasını sağlar
root.after(60000, toggle_visibility)
label.bind("<Button-1>", mesaj_yaz)#mesajYaz.py dosyasından import ettiğimiz mesaj_yaz fonksiyonunu çağırır. Eğer ördeğe tıklanırsa aktif olur
root.after(200,resim_degistir)
root.after(5000,rasgele_koordinat)

root.after(0, fare_takip)#belli aralıklarla fonksiyonları çağırdık
root.mainloop()

