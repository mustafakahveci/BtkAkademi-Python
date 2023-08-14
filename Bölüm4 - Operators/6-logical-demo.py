'''

1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

3- Email ve parola bilgileri ile giriş kontrolü yapınız.

4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

5- Kullanıcıdan vize (%40) ve final (%60) notunu alıp ortalama hesaplayınız.
   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
   a) Ortalama 50 olsa bile final notu en az 50 olmalıdır.

6- Kişinin ad, kilo ve boy bilgilerini alıp kilo endekslerini hesaplayınız.
   Formül: (Kilo) / (Boy**2)
   Aşağıdaki tabloya göre kişi hangi gruptadır ? 
   0-18   => Zayıf
   18 - 24.9 => Normal
   25-29.9 => Fazla Kilolu 
   30.0 - 34.9 => Şişman(obez)

'''

#1 
sayi = int(input("Sayi giriniz: "))
sonuc = (sayi > 0) and (sayi < 100)
print(f"sayı 0-100 arasında mı ? = {sonuc}")

#2
sonuc2 = (sayi > 0) and (sayi % 2 == 0)
print(f"Girilen sayı pozitif çift sayı mı ? = {sonuc2}")

#3
email = "email@gmail.com"
password = "abc123"
girilen_email = input("email giriniz : ")
girilen_password = input("şifreyi giriniz : ")
sonuc3 = (email == girilen_email) and (password == girilen_password)
print(f"Giriş işlemi başarılı mı ? = {sonuc3}")

#4
sayi1 = int(input("1. sayiyi giriniz : "))
sayi2 = int(input("2. sayiyi giriniz : "))
sayi3 = int(input("3. sayiyi giriniz : "))
print(f"{sayi1} en büyük sayıdır : {sayi1 > sayi2 and sayi1 > sayi3}")
print(f"{sayi2} en büyük sayıdır : {sayi2 > sayi1 and sayi2 > sayi3}")
print(f"{sayi3} en büyük sayıdır : {sayi3 > sayi2 and sayi3 > sayi1}")

#5
vize = int(input("Vize sonucunuzu giriniz : "))
final = int(input("Final sonucunuzu giriniz : "))
ortalama = (vize * 0.4) + (final * 0.6)
gectiMi = (ortalama >= 50) and (final >= 50)
print(f"Öğrenci dersten geçti mi ? = {gectiMi}")

#6
name = input("Adınızı giriniz : ")
kilo = int(input("Kilonuzu giriniz (kg) : "))
boy = float(input("Boyunuzu giriniz (m) : "))
bmi = kilo / (boy * boy)
zayif = bmi < 18
normal = bmi >= 18 and bmi < 25
kilolu = bmi >= 25 and bmi < 30
obez = bmi >= 30
print(f"{name} vücut kitle indeksin: {bmi} ve kilo değerlendirmen zayıf : {zayif}")
print(f"{name} vücut kitle indeksin: {bmi} ve kilo değerlendirmen normal : {normal}")
print(f"{name} vücut kitle indeksin: {bmi} ve kilo değerlendirmen kilolu : {kilolu}")
print(f"{name} vücut kitle indeksin: {bmi} ve kilo değerlendirmen obez : {obez}")