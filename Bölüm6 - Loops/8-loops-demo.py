"""
   1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
   ** "random modulü" için "python random" şeklinde arama yapın.
   ** 100 üzerinden puanlama yapın.
   ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
"""
import random
rastgele_sayi = random.randint(1, 100)

hak_sayisi = int(input("Hak sayısını giriniz : "))
birimPuan = 100 / hak_sayisi

while(hak_sayisi > 0):
    print(f"Kalan tahmin sayınız : {hak_sayisi}")
    tahmin = int(input("Tahmininizi giriniz : "))

    if(tahmin == rastgele_sayi):
        print("Doğru cevap")
        print(f"Puanınız : {birimPuan * hak_sayisi}")
        break
    elif(tahmin > rastgele_sayi):
        print("Aşağı in")
    else:
        print("Yukarı çık")
    hak_sayisi-=1

