#1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

kelime = input("kelimeyi giriniz : ")
adet = int(input("kaç defa gösterilecek : "))

def kelimeGoster(kelime , adet): 
    for x in range(adet):
        print(kelime)

kelimeGoster(kelime,adet)





#2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon 

def convertList(*params):
    my_list = []
    for param in params:
        my_list.append(param)
    return my_list

my_list = convertList(1,5,7,9,5)
print(my_list)





#3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

def asalBul(sayi):
    asalMi = True
    for i in range(2,sayi):
        if(sayi % i == 0):
            asalMi = False
            break
    return asalMi

def aradakiAsallariBul(sayi1 , sayi2):
    asalListesi = []
    for i in range(sayi1+1 , sayi2):
        if(asalBul(i) == True):
            asalListesi.append(i)
    return asalListesi

sayi1 = int(input("1. sayiyi giriniz : "))
sayi2 = int(input("2. sayiyi giriniz : "))
asallar = aradakiAsallariBul(sayi1 , sayi2)
print(asallar)





#4- Kendisine gönderilen bir sayının pozitif tam bölenlerini bir liste şeklinde döndürün.

def bolenleriniBul(sayi):
    bolenlerListesi = []
    for i in range(1,sayi+1):
        if(sayi % i == 0):
            bolenlerListesi.append(i)
    return bolenlerListesi

sayi = int(input("bölenleri bulunacak sayıyı giriniz : "))
bolenleri = bolenleriniBul(sayi)
print(bolenleri)