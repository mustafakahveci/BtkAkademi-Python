sayilar = [1,3,5,7,9,12,19,21]
"""
1- sayilar listesini while ile ekrana yazdırın
"""
x = 0
while(x<len(sayilar)):
    print(sayilar[x])
    x+=1


"""
2- başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki
   tüm tek sayıları ekrana yazdırın
"""
baslangic = int(input("başlangıç değerini giriniz : "))
bitis = int(input("bitiş değerini giriniz : "))
i = baslangic
while(i < bitis):
    i+=1
    if(i % 2 == 1):
        print(i)

"""
3- 1-100 arasındaki sayıları azalan şekilde yazdırın.
"""
yuz = 100
while(0 < yuz):
    print(yuz)
    yuz-=1

"""
4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir 
   şekilde yazdırın.
"""
temp = 0
numbers = []
while(temp < 5):
    sayi = int(input("sayi giriniz : "))
    numbers.append(sayi)
    temp+=1
numbers.sort()
print(numbers)

"""
5- Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler
   listesi içinde saklayınız.
   **ürün sayısını kullanıcıya sorun
   **dictionary liste yapısı (name,price) şeklinde olsun.
   **ürün ekleme işlemi bittiğinde ürünleri ekranda while ile 
   listeleyin.
"""
i = 0
urunler = []
adet = int(input("kaç adet ürün eklemek istiyorsunuz : "))
while(i < adet):
    name = input(f"{i+1}. ürünün adını giriniz : ")
    price = input(f"{i+1}. ürünün fiyatını giriniz : ")
    urunler.append({
        "name" : name,
        "price" : price
    })
    i+=1

i=0
print(urunler)