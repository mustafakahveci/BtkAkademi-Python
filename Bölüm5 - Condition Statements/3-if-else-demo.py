"""
1- Kullanıcıdan isim,yaş ve eğitim bilgilerini isteyip ehliyet
   alabilme durumunu kontrol ediniz. Ehliyet alma koşulu en az
   18 ve eğitim durumu lise ya da üniversite olmalıdır.
"""

name = input("name: ")
age = int(input("age: "))
egitimDurumu = input("egitimDurumu : ")

if(age >= 18):
    if((egitimDurumu == "üniversite") or (egitimDurumu == "lise")):
        print(f"{name} ehliyet alabilir.")
    else:
        print(f"{name} ehliyet alamaz eğitim durumu tutmuyor.")
else:
    print(f"{name} ehliyet alamaz yaşı tutmuyor.")



"""
2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan
   ortalamaya göre not aralığına karşılık gelen not bilgisini
   yazdırınız.
   0-24   => 0
   25-44  => 1
   45-54  => 2
   55-69  => 3
   70-84  => 4
   85-100 => 5
"""

yazili1 = float(input("1. yazılı notunuzu giriniz : "))
yazili2 = float(input("2. yazılı notunuzu giriniz : "))
sozlu = float(input("sözlü notunuzu giriniz : "))

ort = (yazili1 + yazili2 + sozlu) / 3

if(ort >= 85 and ort <= 100):
    print(f"Ortalamanız: {ort} - Not bilginiz: 5")
elif(ort >= 70 and ort < 85):
    print(f"Ortalamanız: {ort} - Not bilginiz: 4")
elif(ort >= 55 and ort < 70):
    print(f"Ortalamanız: {ort} - Not bilginiz: 3")
elif(ort >= 45 and ort < 55):
    print(f"Ortalamanız: {ort} - Not bilginiz: 2")
elif(ort >= 25 and ort < 45):
    print(f"Ortalamanız: {ort} - Not bilginiz: 1")
else:
    print(f"Ortalamanız: {ort} - Not bilginiz: 0")



"""
3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını
   aşağıdaki bilgilere göre hesaplayınız.
   1. Bakım => 1.yıl
   2. Bakım => 2.yıl
   3. Bakım => 3.yıl
   *Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı
   hesaplayınız.
   **datetime modülünü kullanmanız gerekiyor.
"""

import datetime

cikisTarihi = input("Araç trafiğe ne zaman çıkıt (yıl/ay/gün) : ")
cikisTarihi = cikisTarihi.split("/")
trafigeCikis = datetime.datetime(int(cikisTarihi[0]),int(cikisTarihi[1]),int(cikisTarihi[2]))
timeNow = datetime.datetime.now()

fark = (timeNow - trafigeCikis).days

if(fark <= 365):
    print("1. servis aralığı")
elif(fark > 365 and fark <= 365*2):
    print("2. servis aralığı")
elif(fark > 365*2 and fark <= 365*3):
    print("3. servis aralığı")
else:
    print("hatalı süre")