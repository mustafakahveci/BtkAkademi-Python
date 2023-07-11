"""
 
   1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

   Müşteri adı
   Müşteri soyadı
   Müşteri adı + soyadı
   Müşteri cinsiyet
   Müşteri tc kimlik 
   Müşteri doğum yılı
   Müşteri adres bilgisi
   Müşteri yaşı 

"""

#1


müsteriAdi = "Mustafa"
müsteriSoyadi = "Kahveci"
müsteri_ad_soyad = müsteriAdi+" "+müsteriSoyadi 
müsteriCinsiyet = True #Erkek
müsteriTc = "12345678912"
müsteriDogumYili = 1994
müsteriAdres = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
müsteriYasi = 2023 - müsteriDogumYili


"""
   
   2-Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.

   Sipariş 1 => 110 TL
   Sipariş 2 => 1100.5 TL
   Sipariş 3 => 356.95 TL

"""

siparis1 = 110
siparis2 = 1100.5
siparis3 = 356.95

toplamSiparis = siparis1+siparis2+siparis3

print(toplamSiparis)