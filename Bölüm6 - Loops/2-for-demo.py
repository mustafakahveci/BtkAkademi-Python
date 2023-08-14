sayilar = [1,3,5,7,9,12,19,21]

#1- Sayılar listesindeki hangi sayılar 3'ün katıdır ?
print("üçe bölünen sayılar : ")
for sayi in sayilar:
    if(sayi % 3 == 0):
        print(sayi)

#2- Sayılar listesindeli sayıların toplamı kaçtır ? 
toplam = 0 
for sayi in sayilar:
    toplam+=sayi
print(f"Sayıların toplamı = {toplam}")

#3- Sayılar listesindeki tek sayıların karesini alınız.
print("Listedeki tek sayıların karesi : ")
for sayi in sayilar:
    if(sayi % 2 == 1):
        print(f"{sayi} 'nın karesi = {sayi ** 2}")



sehirler = ["kocaeli", "istanbul", "ankara", "izmir", "rize"]

#4- Şehirlerden hangileri en fazla 5 karakterlidir ? 
for sehir in sehirler:
    if(len(sehir) <= 5):
        print(sehir)

urunler = [
    {"name": "samsung S6", "price": "3000"},
    {"name": "samsung S7", "price": "4000"},
    {"name": "samsung S8", "price": "5000"},
    {"name": "samsung S9", "price": "6000"},
    {"name": "samsung S10", "price": "7000"},
]

#5- Ürünlerin fiyatları toplamı nedir ? 
urunToplam = 0
for urun in urunler:
    urunToplam += int(urun["price"])
print(urunToplam)

#6- Ürünlerin fiyatı en fazla 5000 olan ürünleri bulunuz.
for urun in urunler:
    if(int(urun["price"]) <= 5000):
        print(urun["name"])