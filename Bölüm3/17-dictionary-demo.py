'''

      ogrenciler = {
         '120' : {
         'ad' : 'Ali',
         'soyad' : 'Yılmaz',
         'telefon : '5320000001'
         },
         '125' : {
         'ad' : 'Can',
         'soyad' : 'Korkmaz',
         'telefon : '5320000002'
         },
         '128' : {
         'ad' : 'Volkan',
         'soyad' : 'Yükselen',
         'telefon : '5320000003'
         },
      }


      1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.

      2- Öğrenci numarasını kullancıdan alıp ilgili öğrenci bilgisini gösterin.

'''

#1

ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
tel = input("öğrenci telefonu: ")

ogrenciler[number] = {
    "ad" : name,
    "soyad" : surname,
    "telefon" : tel
    }

ogrenciler.update({
    number : {
        "ad" : name,
        "soyad" : surname,
        "telefon" : tel
    }
})

print(ogrenciler)


#2

numara = input("öğrenci numarası ? : ")
print(ogrenciler[numara])

