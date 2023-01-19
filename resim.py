import random
import tkinter as tk
import time

resimlistesi = ['Meme1.png', 'Meme2.png', 'Meme3.png', 'Meme4.png', 'Meme5.png', 'Meme6.png', 'Meme7.png']
def resim_goster(resimlistesi):

    def resim_degistir():
        nonlocal current_resim
        current_resim = (current_resim + 1) % len(resimlistesi)
        image = tk.PhotoImage(file=resimlistesi[current_resim])
        label.config(image=image)
        label.image = image
        window.after(20000, resim_degistir) # 20 saniye sonra fonksiyonu tekrar çağır

    current_resim = 0
    window = tk.Tk()
    window.title("Resimler")
    window.geometry("700x700")

    image = tk.PhotoImage(file=resimlistesi[current_resim])
    label = tk.Label(window, image=image)
    label.pack()
    window.after(20000, resim_degistir) # 20 saniye sonra fonksiyonu çağır

    window.mainloop()


